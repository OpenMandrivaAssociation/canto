%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"
%define name    canto
%define version 0.7.6
%define release %mkrel 2

Name:           %name
Version:        %version
Release:        %release
Summary:        An Atom/RSS feed reader for the console
Group:          Networking/News
License:        GPLv2+
URL:            http://codezen.org/canto/
Source:         http://codezen.org/static/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
Requires:	python-chardet
Requires:	python-feedparser
BuildRequires:  python-devel
BuildRequires:  ncurses-devel
BuildRequires:  python-feedparser
BuildRequires:  python-chardet
BuildRequires:  ncursesw-devel

%description
Canto is an Atom/RSS feed reader for the console that is meant to be quick,
concise, and colorful. It's meant to allow you to crank through feeds like
you've never cranked before by providing a minimal, yet information packed
interface. No navigating menus. No dense blocks of unreadable white text.
An interface with almost infinite customization and extensibility using the
excellent Python programming language.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --prefix=%_prefix --root=%buildroot --no-compile
dir -d %{buildroot}%{py_platsitedir}/%{name}
%python_compile_opt
%python_compile
install *.pyc *.pyo %{buildroot}%{py_platsitedir}/%{name}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%{py_platsitedir}/%{name}/*.py
%{py_platsitedir}/%{name}/*.pyc
%{py_platsitedir}/%{name}/*.pyo
%{py_platsitedir}/%{name}/cfg/*.py
%{py_platsitedir}/%{name}/widecurse.so
%{py_platsitedir}/Canto-%{version}-py%{pyver}.egg-info
%_bindir/%{name}*
%_datadir/man/man1/%{name}*.1.lzma
