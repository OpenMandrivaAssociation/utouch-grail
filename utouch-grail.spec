%define major 6
%define libname %mklibname  %{name} %{major}
%define develname   %mklibname  %{name} -d

Name:           utouch-grail
Version:        3.1.1
Release:        1
License:        GPL-3.0
Summary:        Gesture recognition library
Url:            http://launchpad.net/utouch-grail
Group:          Graphical desktop/Other
Source:         https://launchpad.net/grail/trunk/%{version}/+download/grail-%{version}.tar.bz2
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(evemu)
BuildRequires:  pkgconfig(frame)
 
%description
This tree consists of an interface and tools for handling gesture recognition
and gesture instantiation.

When a multitouch gesture is performed on a device, the recognizer emits one or
several possible gestures. Once the context of the gesture is known, i.e., in
what window the touches land and what gestures the clients of that window
listen to, the instantiator delivers the matching set of gestures.
 
The library handles tentative getures, i.e., buffering of events for several
alternative gestures until a match is confirmed.
 
%package -n %{libname}
Summary:    Gesture recognition library
Group:		System/Libraries
 
%description -n %{libname}
This tree consists of an interface and tools for handling gesture recognition
and gesture instantiation.

When a multitouch gesture is performed on a device, the recognizer emits one or
several possible gestures. Once the context of the gesture is known, i.e., in
what window the touches land and what gestures the clients of that window
listen to, the instantiator delivers the matching set of gestures.
 
The library handles tentative getures, i.e., buffering of events for several
alternative gestures until a match is confirmed.
 
%package -n %{develname}
Summary:        Development files for gesture recognition library
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
 
%description -n %{develname}
Development files for the gesture recognition library (grail).

The library handles tentative getures, i.e., buffering of events for several
alternative gestures until a match is confirmed.
 
%prep
%autosetup -n grail-%{version} -p1
 
%build
export CC=gcc
export CXX=g++
%configure \
  --disable-static
%make_build
 
%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
 
 
%files
%defattr(-,root,root)
%doc README COPYING
#{_bindir}/grail-*
 
%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
 
%files -n %{develname}
%defattr(-,root,root)
#{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
 


%changelog
* Tue Nov 01 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.0.1-1
+ Revision: 709356
- imported package utouch-grail


* Sun Oct 30 2011 Matthew Dawkins <mdawkins@unity-linux.org> 2.0.1-1-unity2011
- import for Unity
