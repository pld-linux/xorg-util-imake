Summary:	imake utilities - C preprocessor interface to the make utility
Summary(pl):	Narzêdzia imake - interfejs preprocesora C do narzêdzia make
Name:		xorg-util-imake
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/imake-%{version}.tar.bz2
# Source0-md5:	02fea5a02ba2857c7d81820c8e8b8e6f
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	cpp
Obsoletes:	xorg-util-xmkmf
Obsoletes:	XFree86-imake
Obsoletes:	X11-imake
Obsoletes:	imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
imake utility plus the following support programs: ccmakedep,
mergelib, revpath, mkdirhier, makeg, cleanlinks, mkhtmlindex, xmkmf.

imake is used to generate Makefiles from a template, a set of cpp
macro functions, and a per-directory input file called an Imakefile.
This allows machine dependencies (such as compiler options, alternate
command names, and special make rules) to be kept separate from the
descriptions of the various items to be built.

%description -l pl
Narzêdzie imake oraz nastêpuj±ce programy wspieraj±ce: ccmakedep,
mergelib, revpath, mkdirhier, makeg, cleanlinks, mkhtmlindex, xmkmf.

imake s³u¿y do generowania plików Makefile z szablonu, zbioru funkcji
makr cpp oraz plików wej¶ciowych Imakefile umieszczonych w ka¿dym
katalogu. Pozwala to na trzymanie elementów zale¿nych od maszyny
(takich jak opcje kompilatora, alternatywne nazwy poleceñ oraz
specjalne regu³y make) oddzielonych od opisów elementów do zbudoawnia.

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
%{_mandir}/man1/ccmakedep.1x*
%{_mandir}/man1/cleanlinks.1x*
%{_mandir}/man1/imake.1x*
%{_mandir}/man1/makeg.1x*
%{_mandir}/man1/mergelib.1x*
%{_mandir}/man1/mkdirhier.1x*
%{_mandir}/man1/mkhtmlindex.1x*
%{_mandir}/man1/revpath.1x*
%{_mandir}/man1/xmkmf.1x*
