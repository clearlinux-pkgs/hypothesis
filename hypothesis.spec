#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hypothesis
Version  : 1.16.0
Release  : 6
URL      : https://pypi.python.org/packages/source/h/hypothesis/hypothesis-1.16.0.tar.gz
Source0  : https://pypi.python.org/packages/source/h/hypothesis/hypothesis-1.16.0.tar.gz
Summary  : A library for property based testing
Group    : Development/Tools
License  : MPL-2.0
Requires: hypothesis-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==========
Hypothesis
==========
Hypothesis is a library for testing your Python code against a much larger range
of examples than you would ever want to write by hand. It's based on the Haskell
library, Quickcheck, and is designed to integrate seamlessly into your existing
Python unit testing work flow.

%package python
Summary: python components for the hypothesis package.
Group: Default

%description python
python components for the hypothesis package.


%prep
%setup -q -n hypothesis-1.16.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
