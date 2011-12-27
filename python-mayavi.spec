%define module	mayavi
%define name	python-%{module}
%define version	4.1.0
%define release	%mkrel 1

Summary:	Enthought Tool Suite - mayavi project
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
Source1:	html.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://code.enthought.com/projects/mayavi/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-mayavi2
Obsoletes:	python-enthought-mayavi
Obsoletes:	mayavi
Requires:	python-apptools >= 4.0.1
Requires:	python-envisage >= 4.1.0
Requires:	python-pyface >= 4.1.0
Requires:	python-traits >= 4.1.0
Requires:	python-traitsui >= 4.1.0
Requires:	python-numpy >= 1.1.0, python-vtk, python-configobj
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

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

mkdir tmp
pushd tmp
tar zxf %SOURCE1

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst examples/ tmp/mayavi tmp/tvtk/

