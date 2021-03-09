%define realname digidoc

%define major 2
%define libname %mklibname %{realname} %major
%define develname %mklibname %{realname} -d

Name:		libdigidoc
Version:	3.10.5
Release:	1
Summary:	Library for handling digitally signed documents

Group:		System/Libraries
License:	LGPLv2+
URL:		https://github.com/open-eid/libdigidoc/
Source:		https://github.com/open-eid/libdigidoc/releases/download/v%{version}/libdigidoc-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
Requires:	opensc

%description
libDigiDoc is a library implementing a subset of the XAdES digital
signature standard on top of Estonian specific .ddoc container format.
It allows to create, sign, verify, and modify digidoc XML containers.

%package	-n %{libname}
Group:		System/Libraries
Summary:	Library for handling digitally signed documents
Provides:	%name = %version-%release

%description	-n %{libname}
This package contains libraries and header files for
developing applications that use %{name}.


%package	-n %{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Requires:	libxml2-devel
Requires:	openssl-devel
Requires:	zlib-devel
Requires:	pkgconfig
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{develname}
This package contains libraries and header files for
developing applications that use %{libname}.


%prep
%setup -q

%build

%cmake

%make_build


%install

%make_install -C build


%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig


%files -n %{libname}
%defattr(-,root,root,-)
%config %{_sysconfdir}/digidoc.conf
%{_bindir}/cdigidoc
%{_libdir}/*.so.*
%{_datadir}/libdigidoc/
%doc AUTHORS COPYING ChangeLog README

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/libdigidoc/
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/*.so


%changelog
* Sun Oct 10 2010 Sander Lepik <sander85@mandriva.org> 2.7.0-1mdv2011.0
+ Revision: 584857
- fix group
- New release 2.7.0
- Imported libdigidoc 2.6.0.17 library from openxades.org
- Ported build system from autoconf to CMake
- Changed default save format to 1.3, 1.4 should not be widely used.
- Use FILENAME_MAX for maximum file name length
- Release pkcs11 lib on error and failed pin
- Install public headers in include/digidoc
- Fixed default pkcs11 module path
- Fixed a number of crashes
- Fixed a lot of compiler warnings
- Optionally link against libdl in unix
- Marked extern functions as extern 'C'
- Fixed openssl-1.0.0 compatibility
- Removed reference to SK's internal service from digidoc.conf
- Updated config and certificates to match with the names in
  libdigidocpp
- added 'ESTEID-SK 2007 OCSP 2010' and 'EID-SK 2007 OCSP 2010'
  certificates

* Wed Apr 28 2010 Funda Wang <fwang@mandriva.org> 2.2.11-5mdv2010.1
+ Revision: 539932
- fix build with openssl 1.0

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 2.2.11-4mdv2010.1
+ Revision: 508568
- fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.2.11-1mdv2008.1
+ Revision: 136550
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import libdigidoc


* Sun Jul 02 2006 Emmanuel Andry <eandry@mandriva.org> 2.2.11-1mdv2007.0
- 2.2.11
- buildrequires openssl-devel libxml2-devel

* Mon Nov 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.1.21-2mdk
- Fix BuildRequires
- %%mkrel 

* Thu Oct 20 2005 Lenny Cartier <lenny@mandriva.com> 2.1.21-1mdk
- 2.1.21

* Tue Sep 21 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.93.0-1mdk
- from Veiko Sinivee <veiko.sinivee@solo.delfi.ee> :
	- updated to libdigidoc release 1.93

* Mon Jun 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.90.0-1mdk
- new
