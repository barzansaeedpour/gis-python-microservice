# Use an appropriate base image
FROM ubuntu:20.04

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive
# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# # Install necessary packages
# RUN apt-get update && \
#     apt-get install -y wget wine rpm && \
#     rm -rf /var/lib/apt/lists/*
# Install necessary packages
WORKDIR /app
COPY . /app/

RUN apt-get update
RUN apt-get install fuse libfuse2
RUN apt-get install libglu1-mesa:i386
RUN apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 50051
# # Copy the ODA File Converter RPM to the container
# COPY ODAFileConverter_QT6_lnxX64_8.3dll_25.11.AppImage /app/

# Install ODA File Converter using rpm
# RUN rpm --install --nodeps /tmp/ODAFileConverter_QT6_lnxX64_8.3dll_25.11.rpm
# RUN apt-get install /app/

# Set working directory

# Copy input files and script to the container

# Run the conversion script
# CMD ["wine", "python3", "convert.py"]
CMD ["python3", "server.py"]


# docker build -t odaconverter .
# docker run -p 50051:50051 -v "./input:/app/input" -v "./output:/app/output" odaconverter


# sudo apt-get install libglu1-mesa:i386
# docker run -p 50051:50051 -v "./input:/app/input" -v "./output:/app/output" --privileged --cap-add=SYS_ADMIN --device /dev/fuse -it odaconverter