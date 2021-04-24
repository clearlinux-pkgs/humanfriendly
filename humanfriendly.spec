#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : humanfriendly
Version  : 9.1
Release  : 18
URL      : https://files.pythonhosted.org/packages/31/0e/a2e882aaaa0a378aa6643f4bbb571399aede7dbb5402d3a1ee27a201f5f3/humanfriendly-9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/0e/a2e882aaaa0a378aa6643f4bbb571399aede7dbb5402d3a1ee27a201f5f3/humanfriendly-9.1.tar.gz
Summary  : Human friendly output for text interfaces using Python
Group    : Development/Tools
License  : MIT
Requires: humanfriendly-bin = %{version}-%{release}
Requires: humanfriendly-license = %{version}-%{release}
Requires: humanfriendly-python = %{version}-%{release}
Requires: humanfriendly-python3 = %{version}-%{release}
Requires: monotonic
Requires: pyreadline
BuildRequires : buildreq-distutils3
BuildRequires : monotonic
BuildRequires : pyreadline

%description
====================================================

%package bin
Summary: bin components for the humanfriendly package.
Group: Binaries
Requires: humanfriendly-license = %{version}-%{release}

%description bin
bin components for the humanfriendly package.


%package license
Summary: license components for the humanfriendly package.
Group: Default

%description license
license components for the humanfriendly package.


%package python
Summary: python components for the humanfriendly package.
Group: Default
Requires: humanfriendly-python3 = %{version}-%{release}

%description python
python components for the humanfriendly package.


%package python3
Summary: python3 components for the humanfriendly package.
Group: Default
Requires: python3-core
Provides: pypi(humanfriendly)

%description python3
python3 components for the humanfriendly package.


%prep
%setup -q -n humanfriendly-9.1
cd %{_builddir}/humanfriendly-9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608134469
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/humanfriendly
cp %{_builddir}/humanfriendly-9.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/humanfriendly/4533bebc7b149028bc2932234fc49ca4d1a61d07
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/humanfriendly

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/humanfriendly/4533bebc7b149028bc2932234fc49ca4d1a61d07

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
