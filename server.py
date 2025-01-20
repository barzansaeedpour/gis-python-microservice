import grpc
from concurrent import futures
import dwg_pb2
import dwg_pb2_grpc
import subprocess
import geopandas as gpd
from shapely.geometry import box, Point
from shapely.affinity import translate, scale
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
        # cmd = [TEIGHA_PATH, INPUT_FOLDER, OUTPUT_FOLDER, OUTVER, OUTFORMAT, RECURSIVE, AUDIT, INPUTFILTER]
        # subprocess.run(cmd, shell=True)
        # data = gpd.read_file("./output/file.dxf")
        # data['geom_type'] = data.geometry.type
        # data.set_crs(epsg=4326, inplace=True)
        # bounding_box_polygon = box(637000, 3902000, 672000, 3919000)
        # cropped_data = data[data.geometry.intersects(bounding_box_polygon)]
        # data_lines = cropped_data[cropped_data['geom_type'] == 'LineString']
        # data_points = cropped_data[cropped_data['geom_type'] == 'Point']
        # data_lines.to_file("./output/cropped_lines.shp")
        # data_points.to_file("./output/cropped_points.shp")
        
        # Convert DWG to DXF using ODA File Converter
        cmd = [TEIGHA_PATH, INPUT_FOLDER, OUTPUT_FOLDER, OUTVER, OUTFORMAT, RECURSIVE, AUDIT, INPUTFILTER]
        subprocess.run(cmd, shell=True)

        # Load the converted DXF file using GeoPandas
        data = gpd.read_file("./output/Khoroseh Var-Plan & Profile.dxf")
        data['geom_type'] = data.geometry.type
        data.set_crs(epsg=3857, inplace=True)

        # Calculate the bounding box and crop the data
        bounding_box = data.total_bounds  # Returns (minx, miny, maxx, maxy)
        print(f"Bounding Box: {bounding_box}")
        bounding_box_polygon = box(637000, 3902000, 672000, 3919000)
        cropped_data = data[data.geometry.intersects(bounding_box_polygon)]

        # Translate the cropped data to the new center coordinates (5715364, 4261022)
        data_lines = cropped_data[cropped_data['geom_type'] == 'LineString']
        data_points = cropped_data[cropped_data['geom_type'] == 'Point']

        current_center_x, current_center_y = (bounding_box[0] + bounding_box[2]) / 2, (bounding_box[1] + bounding_box[3]) / 2
        new_center_x, new_center_y = 5715364, 4261022
        delta_x, delta_y = new_center_x - current_center_x, new_center_y - current_center_y

        data_lines['geometry'] = data_lines['geometry'].apply(lambda geom: translate(geom, xoff=delta_x, yoff=delta_y))
        data_points['geometry'] = data_points['geometry'].apply(lambda geom: translate(geom, xoff=delta_x, yoff=delta_y))

        # Scale the geometries around the new center
        scale_factor = 3  # >1 for zooming in, <1 for zooming out
        center_point = Point(new_center_x, new_center_y)
        data_lines['geometry'] = data_lines['geometry'].apply(lambda geom: scale(geom, xfact=scale_factor, yfact=scale_factor, origin=center_point))
        data_points['geometry'] = data_points['geometry'].apply(lambda geom: scale(geom, xfact=scale_factor, yfact=scale_factor, origin=center_point))

        # Save the shapefiles
        # data_lines.to_file("./output/cropped_lines_stretched.shp")
        # data_points.to_file("./output/cropped_points_stretched.shp")
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
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        options=[
            ('grpc.max_send_message_length', 50 * 1024 * 1024),  # 50 MB
            ('grpc.max_receive_message_length', 50 * 1024 * 1024),  # 50 MB
        ]
    )
    dwg_pb2_grpc.add_FileServiceServicer_to_server(FileService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
