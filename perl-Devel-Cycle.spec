%define modname    Devel-Cycle
%define modver 1.12

Summary:	Find memory cycles in objects
Name:		perl-%{modname}
Version:	%{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Devel-Cycle
Source0:	https://cpan.metacpan.org/authors/id/L/LD/LDS/Devel-Cycle-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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
