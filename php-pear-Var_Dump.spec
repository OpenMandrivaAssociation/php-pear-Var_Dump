%define		_class		Var_Dump
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.0.4
Release:	4
Summary:	Methods for dumping information about a variable
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Var_Dump/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Displays informations about the values of variables on a graphical
way:
- If given a simple variable (string, integer, double, ressource), the
  value itself is printed,
- If given an array, it is explored recursively and values are
  presented in a format that shows keys and elements,
- If given an object, informations about the object and the class are
  printed.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_bindir}/gen_php_doc.sh
%{_datadir}/pear/*.php
%{_datadir}/pear/%{upstream_name}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 667648
- mass rebuild

* Thu Sep 09 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 576961
- new version

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-6mdv2010.1
+ Revision: 466333
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.3-5mdv2010.0
+ Revision: 426674
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-4mdv2009.1
+ Revision: 321935
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-3mdv2009.0
+ Revision: 224890
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2008.1
+ Revision: 178556
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 81253
- Import php-pear-Var_Dump

* Sat Apr 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdk
- 1.0.3

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdk
- initial Mandriva package (PLD import)

