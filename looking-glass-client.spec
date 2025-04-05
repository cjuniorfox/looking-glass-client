Name:           looking-glass-client
Version:        B7
Release:        1%{?dist}
Summary:        Looking Glass Client

License:        GPL-2.0-or-later
URL:            https://looking-glass.io
Source0:        https://looking-glass.io/artifact/stable/source 

BuildRequires: cmake
BuildRequires: gcc 
BuildRequires: gcc-c++ 
BuildRequires: libglvnd-devel 
BuildRequires: fontconfig-devel 
BuildRequires: spice-protocol 
BuildRequires: make 
BuildRequires: nettle-devel
BuildRequires: pkgconf-pkg-config 
BuildRequires: binutils-devel 
BuildRequires: libXi-devel 
BuildRequires: libXinerama-devel 
BuildRequires: libXcursor-devel
BuildRequires: libXpresent-devel 
BuildRequires: libxkbcommon-x11-devel 
BuildRequires: wayland-devel 
BuildRequires: wayland-protocols-devel
BuildRequires: libXScrnSaver-devel 
BuildRequires: libXrandr-devel 
BuildRequires: dejavu-sans-mono-fonts
BuildRequires: pipewire-devel 
BuildRequires: libsamplerate-devel
BuildRequires: libdecor-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libsamplerate-devel

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

* Sat Apr 05 2025 Junior <cjuniorfox@gmail.com>
- initial release of Looking Glass
