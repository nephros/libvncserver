# Note that this is NOT a relocatable package
Name:           libvncserver
Version:        0.9.13
Release:        1
License:        GPLv2+ and MIT and BSD-2-Clause
URL:            https://github.com/mer-qa/libvncserver
Source:         %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  libtool
Summary: a library to make writing a vnc server easy

%description
LibVNCServer makes writing a VNC server (or more correctly, a program
exporting a framebuffer via the Remote Frame Buffer protocol) easy.

It is based on OSXvnc, which in turn is based on the original Xvnc by
ORL, later AT&T research labs in UK.

It hides the programmer from the tedious task of managing clients and
compression schemata.

LibVNCServer was put together and is (actively ;-) maintained by
Johannes Schindelin <Johannes.Schindelin@gmx.de>

%package devel
Summary:      Header Files for %{name} 
Requires:     %{name} = %{version}

%description devel
Header Files for %{name}.

%prep
%setup -q -n %{name}-%{version}/libvncserver

%build
%cmake . \
    -DLIBVNCSERVER_INSTALL=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DWITH_ZLIB=ON \
    -DWITH_LZO=ON \
    -DWITH_JPEG=ON \
    -DWITH_PNG=ON \
    -DWITH_SDL=OFF \
    -DWITH_GTK=OFF \
    -DWITH_THREADS=ON \
    -DWITH_GNUTLS=OFF \
    -DWITH_GCRYPT=OFF \
    -DWITH_FFMPEG=OFF \
    -DWITH_24BPP=OFF \
    -DWITH_WEBSOCKETS=OFF \
    -DWITH_SASL=OFF


%make_build

%install
rm -rf %{buildroot}
%make_install includedir="%{buildroot}%{_includedir}/rfb"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
#%%doc README.md AUTHORS ChangeLog NEWS.md TODO.md
%{_libdir}/libvncclient.so.*
%{_libdir}/libvncserver.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/rfb/*
%{_libdir}/libvncclient.so
%{_libdir}/libvncserver.so
#%%{_bindir}/libvncserver-config
%{_libdir}/pkgconfig/libvncclient.pc
%{_libdir}/pkgconfig/libvncserver.pc

