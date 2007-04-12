%define module  Devel-Cycle
%define name	perl-%{module}
%define version 1.07
%define release %mkrel 2

Name:		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Find memory cycles in objects
License: 	GPL or Artistic
Group: 		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Requires:	perl-PadWalker >= 1.0
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This is a simple developer's tool for finding circular references in objects
and other types of references. Because of Perl's reference-count based
memory management, circular references will cause memory leaks.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Devel
%{_mandir}/*/*

