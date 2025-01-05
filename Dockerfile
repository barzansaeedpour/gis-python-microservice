# Use an appropriate base image
FROM ubuntu:20.04

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get install -y wget wine rpm && \
    rm -rf /var/lib/apt/lists/*

# Copy the ODA File Converter RPM to the container
COPY ODAFileConverter_QT6_lnxX64_8.3dll_25.11.rpm /tmp/

# Install ODA File Converter using rpm
RUN rpm --install --nodeps /tmp/ODAFileConverter_QT6_lnxX64_8.3dll_25.11.rpm

# Set working directory
WORKDIR /app

# Copy input files and script to the container
COPY input/ ./input/
COPY convert.py ./

# Run the conversion script
# CMD ["wine", "python3", "convert.py"]
CMD ["python3", "convert.py"]


# docker build -t odaconverter .
# docker run -v "./input:/app/input" -v "./output:/app/output" odaconverter
