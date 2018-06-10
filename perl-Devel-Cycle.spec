%define modname    Devel-Cycle
%define modver 1.12

Summary:	Find memory cycles in objects
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Devel/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
Requires:	perl-PadWalker >= 1.0
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
This is a simple developer's tool for finding circular references in objects
and other types of references. Because of Perl's reference-count based
memory management, circular references will cause memory leaks.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Devel
%{_mandir}/man3/*
