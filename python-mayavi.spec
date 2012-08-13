%define module	mayavi
%define name	python-%{module}
%define version	4.2.0
%define	rel		1
%if %mdkversion < 201100
%define release	%mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Enthought Tool Suite - scientific data 3D visualizer
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/mayavi/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-mayavi2
Obsoletes:	python-enthought-mayavi
Obsoletes:	mayavi
Requires:	python-apptools >= 4.1.0
Requires:	python-envisage >= 4.2.0
Requires:	python-pyface >= 4.2.0
Requires:	python-traits >= 4.2.0
Requires:	python-traitsui >= 4.2.0
Requires:	python-numpy >= 1.1.0, python-vtk, python-configobj
BuildRequires:	x11-server-xvfb, procps
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-numpy-devel >= 1.1.0, python-vtk >= 5.0

%description
MayaVi2 seeks to provide easy and interactive visualization of 3D data. It does
this by the following:
     
- an (optional) rich user interface with dialogs to interact with all data
  and objects in the visualization.
- a simple and clean scripting interface in Python, including one-liners,
  a-la mlab, or object-oriented programming interface.
- harnesses the power of the VTK toolkit without forcing you to learn it.

Additionally Mayavi2 strives to be a reusable tool that can be embedded in your
applications in different ways or combined with the envisage
application-building framework to assemble domain-specific tools.

%prep
%setup -q -n %{module}-%{version}

%build
Xvfb :100 -ac &
XPID=$!
export DISPLAY=:100.0
%__python setup.py build
%__python setup.py build_docs
kill -9 $XPID || /bin/true
mkdir html
mv docs/build/mayavi/html html/mayavi
mv docs/build/tvtk/html html/tvtk

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc *.txt *.rst examples/ html/
%_bindir/mayavi2
%_bindir/tvtk_doc
%py_platsitedir/%{module}*
%py_platsitedir/tvtk*
