# TODO
# - save config to /etc:
# $ phpcs --config-set default_standard PEAR
# PHP Warning:  file_put_contents(/usr/share/pear/data/PHP_CodeSniffer/CodeSniffer.conf): failed to open stream: Permission denied in /usr/share/pear/PHP/CodeSniffer.php on line 1532
%define		pearname	PHP_CodeSniffer
%define		php_min_version 5.4.0
%include	/usr/lib/rpm/macros.php
Summary:	PHP_CodeSniffer tokenises PHP code and detects violations of a defined set of coding standards
Summary(pl.UTF-8):	PHP_CodeSniffer analizuje kod PHP pod kątem naruszeń zdefiniowanych standardów kodowania
Name:		phpcs
Version:	3.4.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	https://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	70c7edd0eb218df10e18d58a669aada7
Patch0:		case-sensitive.patch
URL:		https://github.com/squizlabs/PHP_CodeSniffer
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(dom)
Requires:	php(iconv)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php(tokenizer)
Requires:	php(xmlwriter)
Requires:	php-pear
Provides:	php-pear-PHP_CodeSniffer = 1:%{version}-%{release}
Obsoletes:	php-pear-PHP_CodeSniffer
Obsoletes:	php-pear-PHP_CodeSniffer-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install -p .%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/phpcs
%attr(755,root,root) %{_bindir}/phpcbf
%{php_pear_dir}/PHP/CodeSniffer
%{php_pear_dir}/data/PHP_CodeSniffer
