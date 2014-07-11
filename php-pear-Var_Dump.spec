%define	_class	Var_Dump
%define	modname	%{_class}

Summary:	Methods for dumping information about a variable
Name:		php-pear-%{modname}
Version:	1.0.4
Release:	10
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Var_Dump/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

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
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/docs/*
%{_bindir}/gen_php_doc.sh
%{_datadir}/pear/*.php
%{_datadir}/pear/%{modname}
%{_datadir}/pear/data/%{modname}
%{_datadir}/pear/packages/%{modname}.xml

