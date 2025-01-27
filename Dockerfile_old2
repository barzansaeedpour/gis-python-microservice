FROM ubuntu:22.04

ENV PYTHONUNBUFFERED=1
ENV QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins/platforms/
ENV XDG_RUNTIME_DIR=/tmp/runtime-root  
ENV DISPLAY=:99                        

WORKDIR /app
COPY . /app/

# Install dependencies
RUN dpkg --add-architecture i386 && \
    apt-get update && apt-get install -y \
    wget \
    xvfb \
    gdebi-core \
    libxcb-util1 \
    libxkbcommon-x11-0 \
    libfontconfig1 \
    libfontconfig1:i386 \
    libx11-xcb1 \
    libxcb-cursor0 \
    libqt5gui5 \
    libqt5core5a \
    && gdebi -n /app/ODAFileConverter_QT6_lnxX64_8.3dll_25.11.deb \
    && rm -rf /var/lib/apt/lists/*

# Fix library compatibility
RUN ln -s /usr/lib/x86_64-linux-gnu/libxcb-util.so.1 /usr/lib/x86_64-linux-gnu/libxcb-util.so.0

# # Create runtime directory and test
# RUN mkdir -p ${XDG_RUNTIME_DIR} && chmod 700 ${XDG_RUNTIME_DIR} \
#     && xvfb-run -a -s "-screen 0 1280x1024x24" ODAFileConverter --version
# Create runtime directory and test with proper Xvfb cleanup
RUN mkdir -p ${XDG_RUNTIME_DIR} && chmod 700 ${XDG_RUNTIME_DIR} \
    && { Xvfb :99 -screen 0 1280x1024x24 -ac 2>/dev/null & } \
    && sleep 2 \
    && DISPLAY=:99 ODAFileConverter --version \
    && killall Xvfb