Summary:	EasyGTK - GTK+ wrapper library 
Summary(pl):	EasyGTK - nadzbiór funkcji GTK+
Name:		easygtk
Version:	1.1.5
Release:	2
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		http://www.linsupport.com/sw/%{name}-%{version}.tar
BuildRequires:	gtk+
BuildRequires:	imlib-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	XFree86-devel
BuildRequires:	glib-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
URL:		http://www.linsupport.com/sw/easygtk.html
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
EasyGTK is a wrapper library around GTK+ library to provide a much
easier and simplier Application Programming Interface to the developer.

%description -l pl
EasyGTK jest nadzbiorem funkcji GTK+ pozwalaj±cym na szybsze i ³atwiejsze
tworzenie aplikacju u¿ywaj±cych Graficznegi Interfejsu U¿ytkownika.

%prep
%setup -q -n %{name}

%build
./configure
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install -s libeasygtk.a $RPM_BUILD_ROOT%{_libdir}
install easygtk.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc manual.html example.c testtree.c
%attr(644,root,root) %{_includedir}/easygtk.h
%attr(755,root,root) %{_libdir}/libeasygtk.a
