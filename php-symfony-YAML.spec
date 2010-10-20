%include	/usr/lib/rpm/macros.php
%define		status		stable
%define		pearname	YAML
Summary:	%{pearname} - The Symfony YAML Component
Name:		php-symfony-YAML
Version:	1.0.3
Release:	1
License:	MIT license
Group:		Development/Languages/PHP
Source0:	http://pear.symfony-project.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	fc318d227896fcb3df95229cd9dd8479
URL:		http://pear.symfony-project.com/package/YAML/
BuildRequires:	php-channel(pear.symfony-project.com)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.symfony-project.com)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Symfony YAML Component.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/YAML/*
%{php_pear_dir}/.registry/.channel.*/*.reg
# XXX: who owns
%dir %{php_pear_dir}/SymfonyComponents
%{php_pear_dir}/SymfonyComponents/YAML
