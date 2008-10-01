Summary:	Flyer is a cool and fun 2D flight simulation
Summary(hu.UTF-8):	Flyer egy nagyszerű és szórakoztató 2D repülő szimulátor
Name:		flyer
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://flyer2d.googlecode.com/files/%{name}-%{version}-src.tar.gz
# Source0-md5:	fc923a6272512f7e207661e57a908b79
Patch0:		%{name}-box2d-include-string.patch
Patch1:		%{name}-limits.patch
URL:		http://code.google.com/p/flyer2d/
BuildRequires:	QtOpenGL-devel
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flyer is a cool and fun 2D flight simulation.

%description -l hu.UTF-8
Flyer egy nagyszerű és szórakoztató 2D repülő szimulátor

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
qmake-qt4
%{__make} CPPFLAGS="-include string.h"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
