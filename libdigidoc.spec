%define name	libdigidoc
%define version	2.7.0
%define release %mkrel 1

%define realname digidoc

%define major 2
%define libname %mklibname %{realname} %major
%define develname %mklibname %{realname} -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Library for handling digitally signed documents

Group:		System/Libraries
License:	LGPLv2+
URL:		http://code.google.com/p/esteid
Source:		http://esteid.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	cmake
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
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
Group:		Development/Libraries
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
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ../..
popd

make %{?_smp_mflags} -C %{_target_platform}/build


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}/build


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
