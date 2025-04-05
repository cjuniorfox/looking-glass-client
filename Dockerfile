from debian:bookworm

ENV VERSION=B7

RUN apt-get update && \
    apt-get install -y binutils-dev cmake fonts-dejavu-core libfontconfig-dev \
    gcc g++ pkg-config libegl-dev libgl-dev libgles-dev libspice-protocol-dev \
    nettle-dev libx11-dev libxcursor-dev libxi-dev libxinerama-dev \
    libxpresent-dev libxss-dev libxkbcommon-dev libwayland-dev wayland-protocols \
    libpipewire-0.3-dev libpulse-dev libsamplerate0-dev wget

RUN wget https://looking-glass.io/artifact/stable/source -O /looking-glass.tar.gz && \
    cd / && \
    tar -xzvf looking-glass.tar.gz && \
    cd looking-glass-${VERSION} && \
    mkdir client/build && \
    cd client/build && \
    cmake ../ && \
    make && \
    cp looking-glass-client /

RUN apt-get remove -y binutils-dev cmake libfontconfig-dev \
    gcc g++ pkg-config libegl-dev libgl-dev libgles-dev libspice-protocol-dev \
    nettle-dev libx11-dev libxcursor-dev libxi-dev libxinerama-dev \
    libxpresent-dev libxss-dev libxkbcommon-dev libwayland-dev \
    libpipewire-0.3-dev libpulse-dev libsamplerate0-dev wget

#RUN apt-get install -y libgl libgles libspice-protocol nettle libx11 libxcursor \ 
#    libxi libxinerama libxpresent libxss libxkbcommon libwayland libpipewire-0.3 \
#    libpulse libsamplerate

RUN apt-get install -y libfontconfig1 libwayland-cursor++1 libx11-6 libxi6 libxfixes3 libxss1 \
    libxinerama1 libxcursor1 libxpresent1 libxkbcommon0 libegl1 libwayland-egl1 libgl1 libsamplerate0 \
    libpipewire-0.3-0 libbinutils libpulse0

RUN apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN groupadd -g 999 appuser && \
    useradd -m -u 1000 -g appuser appuser

CMD /looking-glass-client
