# TODO
# - save config to /etc:
# $ phpcs --config-set default_standard PEAR
# PHP Warning:  file_put_contents(/usr/share/pear/data/PHP_CodeSniffer/CodeSniffer.conf): failed to open stream: Permission denied in /usr/share/pear/PHP/CodeSniffer.php on line 1532
%define		pearname	PHP_CodeSniffer
%define		php_min_version 5.2.1
%include	/usr/lib/rpm/macros.php
Summary:	PHP_CodeSniffer tokenises PHP code and detects violations of a defined set of coding standards
Summary(pl.UTF-8):	PHP_CodeSniffer analizuje kod PHP pod kątem naruszeń zdefiniowanych standardów kodowania
Name:		phpcs
Version:	2.7.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	40e5d70ab9aa4cc1a15091ddcc14c609
Patch0:		case-sensitive.patch
Patch1:		peardeps.patch
URL:		https://github.com/squizlabs/PHP_CodeSniffer
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(tokenizer)
Requires:	php-pear
Suggests:	php(simplexml)
Suggests:	php(xmlwriter)
Suggests:	php-phpunit-PHP_Timer
Provides:	php-pear-PHP_CodeSniffer = 1:%{version}-%{release}
Obsoletes:	php-pear-PHP_CodeSniffer
Obsoletes:	php-pear-PHP_CodeSniffer-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional php dependencies
%define		_noautophp	php-xmlwriter

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp}

%description
PHP_CodeSniffer is a set of two PHP scripts; the main phpcs script
that tokenizes PHP, JavaScript and CSS files to detect violations of a
defined coding standard, and a second phpcbf script to automatically
correct coding standard violations. PHP_CodeSniffer is an essential
development tool that ensures your code remains clean and consistent.

%description -l pl.UTF-8
PHP_CodeSniffer jest skryptem PHP5 służącym do rozkładu tekstu kodu
PHP w celu wykrycia naruszeń pewnych zdefiniowanych standardów
kodowania. Jest to istotne narzędzie, dzięki któremu można zapewnić
czystość i spójność kodu. Może także pomóc w zapobieganiu popełniania
przez programistów pewnych częstych błędów semantycznych.

%prep
%pear_package_setup
%patch0 -p1
%patch1 -p1

mv .%{_bindir}/scripts .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install -p .%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log scripts
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/phpcs
%attr(755,root,root) %{_bindir}/phpcbf
%{php_pear_dir}/PHP/CodeSniffer
%{php_pear_dir}/PHP/CodeSniffer.php
%{php_pear_dir}/data/PHP_CodeSniffer
