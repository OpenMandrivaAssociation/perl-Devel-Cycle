%define upstream_name    Devel-Cycle
%define upstream_version 1.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Find memory cycles in objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
Requires:	perl-PadWalker >= 1.0
BuildArch:	noarch

%description
This is a simple developer's tool for finding circular references in objects
and other types of references. Because of Perl's reference-count based
memory management, circular references will cause memory leaks.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Devel
%{_mandir}/*/*


%changelog
* Tue Jan 24 2012 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-3mdv2012.0
+ Revision: 767809
- rebuild

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.110.0-2
+ Revision: 681398
- mass rebuild

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2011.0
+ Revision: 420895
- update to 1.11

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 403098
- rebuild using %%perl_convert_version

* Thu Jul 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2009.0
+ Revision: 233397
- update to new version 1.10

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2009.0
+ Revision: 194846
- update to new version 1.09
- update to new version 1.09

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-3mdv2008.0
+ Revision: 86352
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-2mdv2007.0
- Rebuild

* Wed May 24 2006 Scott Karns <scottk@mandriva.org> 1.07-1mdk
- New release 1.07

* Tue May 23 2006 Scott Karns <scottk@mandriva.org> 1.05-3mdk
- Added BuildRequires perl-version

* Tue May 23 2006 Scott Karns <scottk@mandriva.org> 1.05-2mdk
- Added patch to fix Test::Memory::Cycle broken by Devel-Cycle-1.05
  and to verify that when available, PadWalker version is at least 1.0
  (http://rt.cpan.org/Public/Bug/Display.html?id=19414)
  (http://rt.cpan.org/Public/Bug/Display.html?id=19451)

* Fri May 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdk
- New release 1.05

* Fri May 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-2mdk
- rpmbuildupdate aware
- spec cleanup

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.04-1mdk
- 1.04

* Wed Feb 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-1mdk
- 1.03
- put back "make test" in build phase

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.02-3mdk
- fix buildrequires in a backward compatible way

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.02-2mdk 
- fix directory ownership (distlint)

* Mon Mar 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.02-1mdk
- first mdk release

