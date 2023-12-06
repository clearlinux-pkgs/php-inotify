#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-inotify
Version  : 3.0.0
Release  : 41
URL      : https://pecl.php.net/get/inotify-3.0.0.tgz
Source0  : https://pecl.php.net/get/inotify-3.0.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-inotify-lib = %{version}-%{release}
Requires: php-inotify-license = %{version}-%{release}
BuildRequires : buildreq-php

%description
# PHP Inotify
Inotify bindings for PHP 5 and PHP 7
This extension exposes the inotify API and some additional functions.

%package lib
Summary: lib components for the php-inotify package.
Group: Libraries
Requires: php-inotify-license = %{version}-%{release}

%description lib
lib components for the php-inotify package.


%package license
Summary: license components for the php-inotify package.
Group: Default

%description license
license components for the php-inotify package.


%prep
%setup -q -n inotify-3.0.0
cd %{_builddir}/inotify-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-inotify
cp %{_builddir}/inotify-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-inotify/216829693731f720e978b2edac4b652864d2a3bf
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/inotify.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-inotify/216829693731f720e978b2edac4b652864d2a3bf
