#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hypothesis
Version  : 4.4.4
Release  : 229
URL      : https://files.pythonhosted.org/packages/81/f1/6542bd7fd9a7c4ac8f9f4f617d31f8837f3ffe9a685b143f8fd9f6a7151f/hypothesis-4.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/81/f1/6542bd7fd9a7c4ac8f9f4f617d31f8837f3ffe9a685b143f8fd9f6a7151f/hypothesis-4.4.4.tar.gz
Summary  : A library for property based testing
Group    : Development/Tools
License  : MPL-2.0
Requires: hypothesis-python = %{version}-%{release}
Requires: hypothesis-python3 = %{version}-%{release}
Requires: attrs
Requires: dpcontracts
Requires: enum34
Requires: numpy
Requires: pandas
BuildRequires : attrs
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : setuptools-legacypython
BuildRequires : setuptools-python

%description
==========
Hypothesis
==========
Hypothesis is an advanced testing library for Python. It lets you write tests which
are parametrized by a source of examples, and then generates simple and comprehensible
examples that make your tests fail. This lets you find more bugs in your code with less
work.

%package legacypython
Summary: legacypython components for the hypothesis package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the hypothesis package.


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

%description python3
python3 components for the hypothesis package.


%prep
%setup -q -n hypothesis-4.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549120889
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1549120889
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
