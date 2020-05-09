%?mingw_package_header

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qrencode-libs
Version:        4.0.2
Release:        5%{?dist}
Summary:        Generate QR 2D barcodes

License:        LGPLv2+
URL:            http://fukuchi.org/works/qrencode/
Source0:        http://fukuchi.org/works/qrencode/qrencode-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  chrpath
BuildRequires:  libpng-devel
BuildRequires:  SDL-devel
## For ARM 64 support (RHBZ 926414)
BuildRequires:  autoconf >= 2.69

%description
Qrencode is a utility software using libqrencode to encode string data in
a QR Code and save as a PNG image.

%package -n mingw32-qrencode-libs
Summary:        QR Code encoding library - Shared libraries

%description -n mingw32-qrencode-libs
The qrencode-libs package contains the shared libraries and header files for
applications that use qrencode.

%package -n mingw64-qrencode-libs
Summary:        QR Code encoding library - Shared libraries

%description -n mingw64-qrencode-libs
The qrencode-libs package contains the shared libraries and header files for
applications that use qrencode.

%?mingw_debug_package

%prep
%autosetup -Tb 0 -p 1 -n qrencode-%{version}

%build
autoconf
%mingw_configure --without-tools
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-qrencode-libs
%{mingw32_bindir}/libqrencode.dll
%{mingw32_libdir}/libqrencode.dll.a
%{mingw32_libdir}/pkgconfig/libqrencode.pc
%{mingw32_includedir}/qrencode.h

%files -n mingw64-qrencode-libs
%{mingw64_bindir}/libqrencode.dll
%{mingw64_libdir}/libqrencode.dll.a
%{mingw64_libdir}/pkgconfig/libqrencode.pc
%{mingw64_includedir}/qrencode.h

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 4.0.2-3
- Disable bootstrap after systemd rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 4.0.2-2
- Implement bootstrap logic for so-name bumps

* Tue Jun 25 2019 Paul Wouters <pwouters@redhat.com> - 4.0.2-1
- Update to 4.0.2 and cleanup by Vasiliy N. Glazov <vascom2@gmail.com>

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 3.4.4-7
- Remove French translation in spec file

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4.4-4
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Peter Gordon <peter@thecodergeek.com> - 3.4.4-1
- Update to new upstream bug-fix release (3.4.4).
