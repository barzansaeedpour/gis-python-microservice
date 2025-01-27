FROM ubuntu:22.04

EXPOSE 50051

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app/
# Install headless dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    fuse \
    libfuse2 \
    python3 \
    python3-pip \
    libqt6widgets6 \
    libqt6gui6 \
    libqt6core6 \
    libglvnd0 \
    libglx0 \
    xvfb \
    xauth \
    libxcb-xinerama0 \
    libxkbcommon-x11-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt



RUN wget https://www.opendesign.com/guestfiles/get?filename=ODAFileConverter_QT6_lnxX64_8.3dll_25.12.AppImage -O ODAFileConverter.AppImage
RUN chmod +x ODAFileConverter.AppImage
RUN xvfb-run --auto-servernum ./ODAFileConverter.AppImage --appimage-extract
ENV QT_QPA_PLATFORM="xcb"
ENV QT_DEBUG_PLUGINS=0
ENV QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt6/plugins/
# CMD ["xvfb-run", "--auto-servernum", "/app/squashfs-root/AppRun"]
CMD ["python3", "server.py"]




# FROM ubuntu:22.04
# # Install headless dependencies
# RUN apt-get update && \
#     DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
#     ca-certificates \
#     wget \
#     fuse \
#     libfuse2 \
#     libqt6widgets6 \
#     libqt6gui6 \
#     libqt6core6 \
#     libglvnd0 \
#     libglx0 \
#     xvfb \
#     xauth \
#     libxcb-xinerama0 \
#     libxkbcommon-x11-0 && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# WORKDIR /app
# COPY . /app/
# RUN wget https://www.opendesign.com/guestfiles/get?filename=ODAFileConverter_QT6_lnxX64_8.3dll_25.12.AppImage -O ODAFileConverter.AppImage
# RUN chmod +x ODAFileConverter.AppImage
# RUN xvfb-run --auto-servernum ./ODAFileConverter.AppImage --appimage-extract
# ENV QT_QPA_PLATFORM="xcb"
# ENV QT_DEBUG_PLUGINS=0
# ENV QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt6/plugins/
# CMD ["xvfb-run", "--auto-servernum", "/app/squashfs-root/AppRun"]