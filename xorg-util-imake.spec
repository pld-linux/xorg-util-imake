Summary:	imake utility
Summary(pl):	Narz�dzie imake
Name:		xorg-util-imake
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/util/imake-%{version}.tar.bz2
# Source0-md5:	22d858e001283a82817db7629c29bbdb
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
imake utility.

%description -l pl
Narz�dzie imake.

%prep
%setup -q -n imake-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/imake
%{_mandir}/man1/imake.1*
