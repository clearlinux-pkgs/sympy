#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sympy
Version  : 1.4
Release  : 6
URL      : https://github.com/sympy/sympy/releases/download/sympy-1.4/sympy-1.4.tar.gz
Source0  : https://github.com/sympy/sympy/releases/download/sympy-1.4/sympy-1.4.tar.gz
Summary  : Computer algebra system (CAS) in Python
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: sympy-bin = %{version}-%{release}
Requires: sympy-license = %{version}-%{release}
Requires: sympy-man = %{version}-%{release}
Requires: sympy-python = %{version}-%{release}
Requires: sympy-python3 = %{version}-%{release}
Requires: mpmath
BuildRequires : buildreq-distutils3
BuildRequires : mpmath

%description
SymPy
=====
|pypi version| |Build status| |Gitter Badge| |Zenodo Badge|
.. |pypi version| image:: https://img.shields.io/pypi/v/sympy.svg
:target: https://pypi.python.org/pypi/sympy
.. |Build status| image:: https://secure.travis-ci.org/sympy/sympy.svg?branch=master
:target: https://travis-ci.org/sympy/sympy
.. |Gitter Badge| image:: https://badges.gitter.im/Join%20Chat.svg
:alt: Join the chat at https://gitter.im/sympy/sympy
:target: https://gitter.im/sympy/sympy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Zenodo Badge| image:: https://zenodo.org/badge/18918/sympy/sympy.svg
:target: https://zenodo.org/badge/latestdoi/18918/sympy/sympy

%package bin
Summary: bin components for the sympy package.
Group: Binaries
Requires: sympy-license = %{version}-%{release}

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
Requires: sympy-python3 = %{version}-%{release}

%description python
python components for the sympy package.


%package python3
Summary: python3 components for the sympy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sympy package.


%prep
%setup -q -n sympy-1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555080191
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sympy
cp data/TeXmacs/LICENSE %{buildroot}/usr/share/package-licenses/sympy/data_TeXmacs_LICENSE
cp sympy/parsing/latex/LICENSE.txt %{buildroot}/usr/share/package-licenses/sympy/sympy_parsing_latex_LICENSE.txt
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sympy/data_TeXmacs_LICENSE
/usr/share/package-licenses/sympy/sympy_parsing_latex_LICENSE.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/isympy.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
