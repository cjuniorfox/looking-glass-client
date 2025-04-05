Name:           looking-glass-client
Version:        B7
Release:        1%{?dist}
Summary:        Looking Glass Client

License:        GPL-2.0-or-later
URL:            https://looking-glass.io
Source0:        https://looking-glass.io/artifact/stable/source 

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXi-devel
BuildRequires:  libXpresent-devel
BuildRequires:  wayland-devel
BuildRequires:  SDL2-devel
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  libdrm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  pipewire-devel
BuildRequires:  pkgconfig

Requires:       hicolor-icon-theme

%description
Looking Glass is a KVM Frame Relay (KVMFR) implementation for Linux that allows you to interact with a QEMU Windows guest using a low-latency client.

%prep
%autosetup -n looking-glass-%{version}

%build
%cmake -S client
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/looking-glass-client
%{_datadir}/applications/looking-glass-client.desktop
%{_datadir}/icons/hicolor/scalable/apps/looking-glass.svg

%changelog
* Sat Apr 05 2025 Junior <cjuniorfox@gmail.com> B7-1
- new package built with tito

* Sat Apr 05 2025 Junior <cjuniorfox@gmail.com> B7-1
- new package built with tito

* Fri Apr 04 2025 Junior <cjuniorfox@gmail.com> B7-1
- new package built with tito

* Fri Apr 04 2025 Your Name <you@example.com> - B7-1
- Initial RPM release for Looking Glass client

