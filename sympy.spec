#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sympy
Version  : 1.8
Release  : 25
URL      : https://github.com/sympy/sympy/releases/download/sympy-1.8/sympy-1.8.tar.gz
Source0  : https://github.com/sympy/sympy/releases/download/sympy-1.8/sympy-1.8.tar.gz
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
This directory contains SymPy example programs.
-------------------------------------------------------------------------------
DIRECTORY STRUCTURE

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
Provides: pypi(sympy)
Requires: pypi(mpmath)

%description python3
python3 components for the sympy package.


%prep
%setup -q -n sympy-1.8
cd %{_builddir}/sympy-1.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619280318
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sympy
cp %{_builddir}/sympy-1.8/data/TeXmacs/LICENSE %{buildroot}/usr/share/package-licenses/sympy/d5697996ec5fa9d54542ad3189150198bdcb5181
cp %{_builddir}/sympy-1.8/sympy/parsing/latex/LICENSE.txt %{buildroot}/usr/share/package-licenses/sympy/e5e9ad6789d8819370e261964212879d59e314b9
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
/usr/share/package-licenses/sympy/d5697996ec5fa9d54542ad3189150198bdcb5181
/usr/share/package-licenses/sympy/e5e9ad6789d8819370e261964212879d59e314b9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/isympy.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
