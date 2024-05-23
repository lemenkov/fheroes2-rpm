Name: fheroes2
Version: 1.1.0
Release: %autorelease
Summary: Free implementation of the popular game engine
License: GPL-2.0-or-later
URL: https://github.com/ihhub/fheroes2
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1: fheroes2-0001-Don-t-install-docs.patch
Patch2: fheroes2-0002-Don-t-install-scripts.patch
BuildRequires: SDL2_image-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_net-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: cmake
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: libpng-devel

%description
Free implementation of the popular game engine. You need to copy files from
data and maps directories from original game into your
/usr/share/games/fheroes2/{maps,data} directories respectively

%prep
%autosetup -p1

%build
export LANG=en_US.UTF-8
%cmake \
    -DFHEROES2_DATA="%{_datadir}/%{name}" \
    -DUSE_SDL_VERSION=SDL2 \
    -DENABLE_IMAGE=ON

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/%{name}/files/data/
mkdir -p %{buildroot}%{_datadir}/%{name}/maps/

%files
%license LICENSE
%doc README.md changelog.txt
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/files/
%dir %{_datadir}/%{name}/files/data/
%dir %{_datadir}/%{name}/files/lang/
%dir %{_datadir}/%{name}/maps/
%{_datadir}/%{name}/files/data/resurrection.h2d
%{_datadir}/%{name}/files/lang/*.mo

%changelog
%autochangelog
