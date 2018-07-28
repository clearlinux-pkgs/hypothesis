#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hypothesis
Version  : 3.66.10
Release  : 126
URL      : https://files.pythonhosted.org/packages/62/84/f6b606a94f8b6c0aa37b664cae49e76188474e259c9858dbc6d6e9af3463/hypothesis-3.66.10.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/84/f6b606a94f8b6c0aa37b664cae49e76188474e259c9858dbc6d6e9af3463/hypothesis-3.66.10.tar.gz
Summary  : A library for property based testing
Group    : Development/Tools
License  : MPL-2.0
Requires: hypothesis-python3
Requires: hypothesis-python
Requires: attrs
Requires: coverage
Requires: enum34
Requires: numpy
Requires: python-dateutil
Requires: pytz
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : setuptools-python

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
Requires: python-core

%description legacypython
legacypython components for the hypothesis package.


%package python
Summary: python components for the hypothesis package.
Group: Default
Requires: hypothesis-python3

%description python
python components for the hypothesis package.


%package python3
Summary: python3 components for the hypothesis package.
Group: Default
Requires: python3-core

%description python3
python3 components for the hypothesis package.


%prep
%setup -q -n hypothesis-3.66.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532766793
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1532766793
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

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
