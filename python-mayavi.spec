%define module	mayavi

Summary:	Enthought Tool Suite - scientific data 3D visualizer
Name:	    python-%{module}
Version:	4.3.1
Release:	2
Source0:	http://www.enthought.com/repo/ets/mayavi-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/mayavi/
Obsoletes:	python-enthought-mayavi2
Obsoletes:	python-enthought-mayavi
Obsoletes:	mayavi
Requires:	python-apptools >= 4.1.0
Requires:	python-envisage >= 4.2.0
Requires:	python-pyface >= 4.2.0
Requires:	python-traits >= 4.2.0
Requires:	python-traitsui >= 4.2.0
Requires:	python-numpy >= 1.1.0
Requires:	python-vtk
Requires:	python-configobj
BuildRequires:	x11-server-xvfb
BuildRequires:	procps
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-numpy-devel >= 1.1.0
BuildRequires:	python-vtk >= 5.0
BuildRequires:	pkgconfig(lapack)

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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files 
%doc *.txt *.rst examples/ html/
%{_bindir}/mayavi2
%{_bindir}/tvtk_doc
%py_platsitedir/%{module}*
%py_platsitedir/tvtk*


%changelog
* Tue Aug 14 2012 Lev Givon <lev@mandriva.org> 4.2.0-1
+ Revision: 814739
- Update to 4.2.0.

* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.1.0-1
+ Revision: 745716
- Update to 4.1.0.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689256
- import python-mayavi




