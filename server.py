import grpc
from concurrent import futures
import dwg_pb2
import dwg_pb2_grpc
import subprocess
import geopandas as gpd
from shapely.geometry import box
import os

class FileService(dwg_pb2_grpc.FileServiceServicer):
    def Upload(self, request_iterator, context):
        # Save the uploaded file
        file_path = 'input/file.dwg'
        with open(file_path, 'wb') as file:
            for request in request_iterator:
                file.write(request.data)
        
        # Convert the DWG file
        INPUT_FOLDER = "./input/"
        OUTPUT_FOLDER = "./output"
        TEIGHA_PATH = "C:/Program Files/ODA/ODAFileConverter 25.11.0/ODAFileConverter.exe"
        OUTVER = "ACAD2018"
        OUTFORMAT = "DXF"
        RECURSIVE = "0"
        AUDIT = "1"
        INPUTFILTER = "*.DWG"
        cmd = [TEIGHA_PATH, INPUT_FOLDER, OUTPUT_FOLDER, OUTVER, OUTFORMAT, RECURSIVE, AUDIT, INPUTFILTER]
        subprocess.run(cmd, shell=True)
        data = gpd.read_file("./output/file.dxf")
        data['geom_type'] = data.geometry.type
        data.set_crs(epsg=4326, inplace=True)
        bounding_box = data.total_bounds  # Returns (minx, miny, maxx, maxy)
        min_x, min_y, max_x, max_y = bounding_box
        print(f"Bounding Box: {bounding_box}")
        bounding_box_polygon = box(637000, 3902000, 672000, 3919000)
        cropped_data = data[data.geometry.intersects(bounding_box_polygon)]
        data_lines = cropped_data[cropped_data['geom_type'] == 'LineString']
        data_points = cropped_data[cropped_data['geom_type'] == 'Point']
        data_lines.to_file("./output/cropped_lines.shp")
        data_points.to_file("./output/cropped_points.shp")

        # Gather the converted files
        file_names = [
            "cropped_lines.cpg", "cropped_lines.dbf", "cropped_lines.prj", "cropped_lines.shp", "cropped_lines.shx",
            "cropped_points.cpg", "cropped_points.dbf", "cropped_points.prj", "cropped_points.shp", "cropped_points.shx"
        ]
        
        converted_files = []
        for file_name in file_names:
            with open(f"./output/{file_name}", "rb") as f:
                file_data = f.read()
                converted_files.append(dwg_pb2.ConvertedFile(filename=file_name, data=file_data))
        
        return dwg_pb2.UploadResponse(status=dwg_pb2.UploadResponse.SUCCESS, files=converted_files)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dwg_pb2_grpc.add_FileServiceServicer_to_server(FileService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
