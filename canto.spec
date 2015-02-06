%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

Name:		canto
Version:	0.7.10
Release:	4
Summary:	An Atom/RSS feed reader for the console
Group:		Networking/News
License:	GPLv2+
URL:		http://codezen.org/canto/
Source:		http://codezen.org/static/%{name}-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-chardet
BuildRequires:	python-feedparser
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)
Requires:	python-chardet
Requires:	python-feedparser
Requires:	xclip

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
python setup.py install --prefix=%{_prefix} --root=%{buildroot} --no-compile
dir -d %{buildroot}%{py_platsitedir}/%{name}
%python_compile_opt
%python_compile
install *.pyc *.pyo %{buildroot}%{py_platsitedir}/%{name}

%files
%doc ChangeLog COPYING README
%{py_platsitedir}/%{name}/*.py
%{py_platsitedir}/%{name}/*.pyc
%{py_platsitedir}/%{name}/*.pyo
%{py_platsitedir}/%{name}/cfg/*.py
%{py_platsitedir}/%{name}/widecurse.so
%{py_platsitedir}/Canto-%{version}-py%{py_ver}.egg-info
%{_bindir}/%{name}*
%{_datadir}/man/man1/%{name}*.1.*

