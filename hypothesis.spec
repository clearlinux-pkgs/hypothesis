#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hypothesis
Version  : 3.24.0
Release  : 47
URL      : http://pypi.debian.net/hypothesis/hypothesis-3.24.0.tar.gz
Source0  : http://pypi.debian.net/hypothesis/hypothesis-3.24.0.tar.gz
Summary  : A library for property based testing
Group    : Development/Tools
License  : MPL-2.0
Requires: hypothesis-legacypython
Requires: hypothesis-python
Requires: enum34
Requires: numpy
Requires: pytest
Requires: pytz
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Hypothesis
        ==========
        
        Hypothesis is an advanced testing library for Python. It lets you write tests which
        are parametrized by a source of examples, and then generates simple and comprehensible
        examples that make your tests fail. This lets you find more bugs in your code with less
        work.
        
        e.g.

%package legacypython
Summary: legacypython components for the hypothesis package.
Group: Default

%description legacypython
legacypython components for the hypothesis package.


%package python
Summary: python components for the hypothesis package.
Group: Default
Requires: hypothesis-legacypython

%description python
python components for the hypothesis package.


%prep
%setup -q -n hypothesis-3.24.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1504681063
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1504681063
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
