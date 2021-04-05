#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hypothesis
Version  : 6.8.5
Release  : 499
URL      : https://files.pythonhosted.org/packages/e7/8d/1142e682e1db056b2a436d7ef2cd0c8bf21d0905773a8cbbca58d201f462/hypothesis-6.8.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/e7/8d/1142e682e1db056b2a436d7ef2cd0c8bf21d0905773a8cbbca58d201f462/hypothesis-6.8.5.tar.gz
Summary  : A library for property-based testing
Group    : Development/Tools
License  : MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: hypothesis-bin = %{version}-%{release}
Requires: hypothesis-license = %{version}-%{release}
Requires: hypothesis-python = %{version}-%{release}
Requires: hypothesis-python3 = %{version}-%{release}
Requires: Django
Requires: attrs
Requires: black
Requires: click
Requires: dpcontracts
Requires: importlib_metadata
Requires: lark-parser
Requires: numpy
Requires: pandas
Requires: python-dateutil
Requires: pytz
Requires: sortedcontainers
Requires: tzdata
BuildRequires : Django
BuildRequires : attrs
BuildRequires : black
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : dpcontracts
BuildRequires : lark-parser
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : python-dateutil
BuildRequires : pytz
BuildRequires : sortedcontainers
BuildRequires : tzdata

%description
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%package bin
Summary: bin components for the hypothesis package.
Group: Binaries
Requires: hypothesis-license = %{version}-%{release}

%description bin
bin components for the hypothesis package.


%package license
Summary: license components for the hypothesis package.
Group: Default

%description license
license components for the hypothesis package.


%package python
Summary: python components for the hypothesis package.
Group: Default
Requires: hypothesis-python3 = %{version}-%{release}

%description python
python components for the hypothesis package.


%package python3
Summary: python3 components for the hypothesis package.
Group: Default
Requires: python3-core
Provides: pypi(hypothesis)
Requires: pypi(attrs)
Requires: pypi(sortedcontainers)

%description python3
python3 components for the hypothesis package.


%prep
%setup -q -n hypothesis-6.8.5
cd %{_builddir}/hypothesis-6.8.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617635470
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
mkdir -p %{buildroot}/usr/share/package-licenses/hypothesis
cp %{_builddir}/hypothesis-6.8.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/hypothesis/cbc4c246c44ed63fb158856a846c0962ae22668d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hypothesis

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hypothesis/cbc4c246c44ed63fb158856a846c0962ae22668d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
