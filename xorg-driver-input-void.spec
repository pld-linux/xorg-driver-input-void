Summary:	X.org null input driver
Summary(pl.UTF-8):	Pusty sterownik wejściowy X.org
Name:		xorg-driver-input-void
Version:	1.4.0
Release:	6
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-void-%{version}.tar.bz2
# Source0-md5:	93821f21e807260b05431c62437a8b32
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.9.99.1
BuildRequires:	rpmbuild(macros) >= 1.389
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.9.99.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org dummy/null input driver. It doesn't connect to any physical
device, and it never delivers any events. It functions as both a
pointer and keyboard device, and may be used as X server's core
pointer and/or core keyboard. It's purpose is to allow the X server to
operate without a core pointer and/or core keyboard.

%description -l pl.UTF-8
Pusty sterownik wejściowy X.org. Nie łączy się z żadnym urządzeniem
fizycznym i nie dostarcza żadnych zdarzeń. Działa zarówno jako
urządzenie wskazujące jak i klawiatura; może być używany jako główne
urządzenie wskazujące i/lub główna klawiatura serwera X. Jego celem
jest umożliwienie działania serwera X bez głównego urządzenia
wskazujacego i/lub głównej klawiatury.

%prep
%setup -q -n xf86-input-void-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/void_drv.so
%{_mandir}/man4/void.4*
