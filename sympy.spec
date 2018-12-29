#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sympy
Version  : 1.3
Release  : 5
URL      : https://github.com/sympy/sympy/releases/download/sympy-1.3/sympy-1.3.tar.gz
Source0  : https://github.com/sympy/sympy/releases/download/sympy-1.3/sympy-1.3.tar.gz
Summary  : Computer algebra system (CAS) in Python
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: sympy-bin
Requires: sympy-python3
Requires: sympy-license
Requires: sympy-man
Requires: sympy-python
Requires: mpmath
BuildRequires : buildreq-distutils3
BuildRequires : mpmath

%description
SymPy is a Python library for symbolic mathematics. It aims to become a
        full-featured computer algebra system (CAS) while keeping the code as simple
        as possible in order to be comprehensible and easily extensible.  SymPy is
        written entirely in Python. It depends on mpmath, and other external libraries
        may be optionally for things like plotting support.

%package bin
Summary: bin components for the sympy package.
Group: Binaries
Requires: sympy-license
Requires: sympy-man

%description bin
bin components for the sympy package.


%package license
Summary: license components for the sympy package.
Group: Default

%description license
license components for the sympy package.


%package man
Summary: man components for the sympy package.
Group: Default

%description man
man components for the sympy package.


%package python
Summary: python components for the sympy package.
Group: Default
Requires: sympy-python3

%description python
python components for the sympy package.


%package python3
Summary: python3 components for the sympy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sympy package.


%prep
%setup -q -n sympy-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536975260
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/sympy
cp data/TeXmacs/LICENSE %{buildroot}/usr/share/doc/sympy/data_TeXmacs_LICENSE
cp sympy/parsing/latex/LICENSE.txt %{buildroot}/usr/share/doc/sympy/sympy_parsing_latex_LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/isympy

%files license
%defattr(-,root,root,-)
/usr/share/doc/sympy/data_TeXmacs_LICENSE
/usr/share/doc/sympy/sympy_parsing_latex_LICENSE.txt

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/isympy.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
