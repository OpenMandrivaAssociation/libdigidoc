%define	name	libdigidoc
%define	version	2.2.11
%define	release	%mkrel 3

%define realname digidoc

%define major 2
%define libname %mklibname %{realname} %major
%define libnamedev %mklibname %{realname} %major -d


Summary: Generic library implementing the XAdES digital signature standard
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Libraries
URL: http://sourceforge.net/projects/gdigidoc/
Source: http://heanet.dl.sourceforge.net/sourceforge/gdigidoc/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot

BuildRequires: pkgconfig openssl-devel libxml2-devel

%description
DigiDoc is a generic library implementing the XAdES digital signature standard.
It allows to create, sign, verify, and modify digidoc XML containers. Support
for doing hardware cryptographic signing operations is provided via PKCS#11
on all platforms and CSP on win32.

%package -n %{libname}
Summary: Generic library implementing the XAdES digital signature standard
Group: Development/Other
Provides: lib%{name} = %{version}

%description -n %{libname}
DigiDoc is a generic library implementing the XAdES digital signature standard.
It allows to create, sign, verify, and modify digidoc XML containers. Support
for doing hardware cryptographic signing operations is provided via PKCS#11
on all platforms and CSP on win32.


%package -n %{libnamedev}
Summary: Libdigidoc library headers and development libraries
Group: Development/Other
Requires: %{libname} = %{version}
Provides: lib%{name}-devel = %{version}
Provides: libdigidoc-devel

%description -n %{libnamedev}
DigiDoc is a generic library implementing the XAdES digital signature standard.
It allows to create, sign, verify, and modify digidoc XML containers. Support
for doing hardware cryptographic signing operations is provided via PKCS#11
on all platforms and CSP on win32.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %name-%{version}

%build

%configure  

make

%install

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%config(noreplace) %_sysconfdir/*.conf
%_datadir/libdigidoc

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%_libdir/pkgconfig/*.pc
%{_includedir}/*
%{_bindir}/*

