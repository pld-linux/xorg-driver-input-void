Summary:	X.org null input driver
Summary(pl):	Pusty sterownik wej¶ciowy X.org
Name:		xorg-driver-input-void
Version:	1.0.0.5
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/driver/xf86-input-void-%{version}.tar.bz2
# Source0-md5:	bfa5e6c582638837efd6b4fc7d77d35b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org dummy/null input driver. It doesn't connect to any physical
device, and it never delivers any events. It functions as both a
pointer and keyboard device, and may be used as X server's core
pointer and/or core keyboard. It's purpose is to allow the X server to
operate without a core pointer and/or core keyboard.

%description -l pl
Pusty sterownik wej¶ciowy X.org. Nie ³±czy siê z ¿adnym urz±dzeniem
fizycznym i nie dostarcza ¿adnych zdarzeñ. Dzia³a zarówno jako
urz±dzenie wskazuj±ce jak i klawiatura; mo¿e byæ u¿ywany jako g³ówne
urz±dzenie wskazuj±ce i/lub g³ówna klawiatura serwera X. Jego celem
jest umo¿liwienie dzia³ania serwera X bez g³ównego urz±dzenia
wskazujacego i/lub g³ównej klawiatury.

%prep
%setup -q -n xf86-input-void-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/void_drv.so
%{_mandir}/man4/void.4*
