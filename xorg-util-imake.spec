Summary:	imake utilities - C preprocessor interface to the make utility
Summary(pl.UTF-8):	Narzędzia imake - interfejs preprocesora C do narzędzia make
Name:		xorg-util-imake
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/imake-%{version}.tar.bz2
# Source0-md5:	d5058b1317a85bedc1dc40c7e85c8d26
Patch0:		%{name}-format.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cpp >= 6:4.0.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	cpp >= 6:4.0.0
Requires:	xorg-cf-files
Obsoletes:	X11-imake < 1:7.0.0
Obsoletes:	XFree86-imake < 1:7.0.0
Obsoletes:	imake < 1:7.0.0
Obsoletes:	xorg-util-xmkmf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
imake utility plus the following support programs: ccmakedep,
mergelib, revpath, mkdirhier, makeg, cleanlinks, mkhtmlindex, xmkmf.

imake is used to generate Makefiles from a template, a set of cpp
macro functions, and a per-directory input file called an Imakefile.
This allows machine dependencies (such as compiler options, alternate
command names, and special make rules) to be kept separate from the
descriptions of the various items to be built.

%description -l pl.UTF-8
Narzędzie imake oraz następujące programy wspierające: ccmakedep,
mergelib, revpath, mkdirhier, makeg, cleanlinks, mkhtmlindex, xmkmf.

imake służy do generowania plików Makefile z szablonu, zbioru funkcji
makr cpp oraz plików wejściowych Imakefile umieszczonych w każdym
katalogu. Pozwala to na trzymanie elementów zależnych od maszyny
(takich jak opcje kompilatora, alternatywne nazwy poleceń oraz
specjalne reguły make) oddzielonych od opisów elementów do zbudoawnia.

%prep
%setup -q -n imake-%{version}
%patch0 -p1

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/ccmakedep
%attr(755,root,root) %{_bindir}/cleanlinks
%attr(755,root,root) %{_bindir}/imake
%attr(755,root,root) %{_bindir}/makeg
%attr(755,root,root) %{_bindir}/mergelib
%attr(755,root,root) %{_bindir}/mkdirhier
%attr(755,root,root) %{_bindir}/mkhtmlindex
%attr(755,root,root) %{_bindir}/revpath
%attr(755,root,root) %{_bindir}/xmkmf
%{_mandir}/man1/ccmakedep.1*
%{_mandir}/man1/cleanlinks.1*
%{_mandir}/man1/imake.1*
%{_mandir}/man1/makeg.1*
%{_mandir}/man1/mergelib.1*
%{_mandir}/man1/mkdirhier.1*
%{_mandir}/man1/mkhtmlindex.1*
%{_mandir}/man1/revpath.1*
%{_mandir}/man1/xmkmf.1*
