%?mingw_package_header

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-libgee
Version:        0.20.3
Release:        1%{?dist}
Summary:        MinGW GObject collection library

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://live.gnome.org/Libgee
#VCS:           git:git://git.gnome.org/libgee
Source0:        http://download.gnome.org/sources/libgee/%{release_version}/libgee-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2

%description
libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

%package -n mingw32-libgee
Summary:        MinGW GObject collection library
Requires:       pkgconfig

%description -n mingw32-libgee
libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package contains the MinGW Windows cross compiled libgee library.

%package -n mingw64-libgee
Summary:        MinGW GObject collection library
Requires:       pkgconfig

%description -n mingw64-libgee
libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

This package contains the MinGW Windows cross compiled libgee library.


%?mingw_debug_package


%prep
%setup -q -n libgee-%{version}


%build
%mingw_configure
%mingw_make %{?_smp_mflags} V=1

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Drop all .la and .vapi files
find $RPM_BUILD_ROOT -name "*.la" -delete
find $RPM_BUILD_ROOT -name "*.vapi" -delete


%files -n mingw32-libgee
%doc AUTHORS ChangeLog COPYING MAINTAINERS NEWS README
%{mingw32_bindir}/libgee-0.8-2.dll
%{mingw32_includedir}/gee-0.8
%{mingw32_libdir}/libgee-0.8.dll.a
%{mingw32_libdir}/pkgconfig/gee-0.8.pc


%files -n mingw64-libgee
%doc AUTHORS ChangeLog COPYING MAINTAINERS NEWS README
%{mingw64_bindir}/libgee-0.8-2.dll
%{mingw64_includedir}/gee-0.8
%{mingw64_libdir}/libgee-0.8.dll.a
%{mingw64_libdir}/pkgconfig/gee-0.8.pc


%changelog
* Sun Jul 27 2014 Marc-André Lureau <marcandre.lureau@gmail.com> - 0.15.3-1
- Initial mingw-fedora packaging.
