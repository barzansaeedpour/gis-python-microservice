"# gis-python-microservice" 


To generate the grpc from protofile:

```
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. protos/dwg.proto
```