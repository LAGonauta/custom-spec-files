%{?mingw_package_header}

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-glib-networking
Version:        2.62.3
Release:        2%{?dist}
Summary:        MinGW Windows glib-networking library

License:        LGPLv2+
URL:            http://www.gnome.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glib-networking/%{release_version}/glib-networking-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-gnutls >= 2.10
BuildRequires:  mingw64-gnutls >= 2.10
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  intltool
BuildRequires:  meson

%description
This package contains modules that extend the networking support in GIO.


%package -n mingw32-glib-networking
Summary:        MinGW Windows glib-networking library

%description -n mingw32-glib-networking
This package contains modules that extend the networking support in GIO.


%package -n mingw64-glib-networking
Summary:        MinGW Windows glib-networking library

%description -n mingw64-glib-networking
This package contains modules that extend the networking support in GIO.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n glib-networking-%{version}


%build
%mingw_meson -Dlibproxy_support=false -Dgnome_proxy_support=false -Dopenssl=enabled

%install
%mingw_ninja_install

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gio/modules/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gio/modules/*.dll.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/gio/modules/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/gio/modules/*.la

%mingw_find_lang glib-networking


%files -n mingw32-glib-networking -f mingw32-glib-networking.lang
%license COPYING
%{mingw32_libdir}/gio/modules/*.dll
                                                                                                                     %files -n mingw64-glib-networking -f mingw64-glib-networking.lang
%license COPYING
%{mingw64_libdir}/gio/modules/*.dll


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.62.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Sandro Mani <manisandro@gmail.com> - 2.62.3-1
- Update to 2.62.3

* Tue Dec 10 2019 Sandro Mani <manisandro@gmail.com> - 2.62.2-1
- Update to 2.62.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.62.1-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.62.1-1
- Update to 2.62.1

* Mon Sep 16 2019 Sandro Mani <manisandro@gmail.com> - 2.62.0-1
- Update to 2.62.0

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 2.61.2-1
- Update to 2.61.2
