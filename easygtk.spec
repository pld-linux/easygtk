Summary:	EasyGTK - GTK+ wrapper library
Summary(pl):	EasyGTK - nadzbiór funkcji GTK+
Name:		easygtk
Version:	1.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	%{name}-%{version}.tar
# Source0-md5:	04bf9844bed30d34c6e6cb6416cadced
Patch0:		%{name}-Makefile.patch
BuildRequires:	gtk+
BuildRequires:	imlib-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	XFree86-devel
BuildRequires:	glib-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
EasyGTK is a wrapper library around GTK+ library to provide a much
easier and simplier Application Programming Interface to the
developer.

%description -l pl
EasyGTK jest nadzbiorem funkcji GTK+ pozwalaj±cym na szybsze i
³atwiejsze tworzenie aplikacji u¿ywaj±cych Graficznego Interfejsu
U¿ytkownika.

%prep
%setup -q -n %{name}

%patch

%build
./configure
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

# make shared library
%{__make} easygtk.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install libeasygtk.a $RPM_BUILD_ROOT%{_libdir}
install easygtk.so $RPM_BUILD_ROOT%{_libdir}/libeasygtk.so.%{version}
install easygtk.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc manual.html README example.c testtree.c
%attr(644,root,root) %{_includedir}/easygtk.h
%attr(755,root,root) %{_libdir}/libeasygtk.a
%attr(755,root,root) %{_libdir}/libeasygtk.so.%{version}
