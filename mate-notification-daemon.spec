Summary:	MATE Notification Daemon
Name:		mate-notification-daemon
Version:	1.2.0
Release:	2
License:	GPLv2+
Group:		System/Servers
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libmatenotify)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(x11)

Provides:	virtual-notification-daemon
Conflicts:	xfce4-notifyd

Requires:	libmatenotify
Requires(post,preun): mate-conf

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec (http://galago.info/specs/notification/index.php).

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static

%make LIBS='-lgmodule-2.0'

%install
# this has to be an error with their make install
mkdir -p %{buildroot}%{_libdir}/mate-notification-daemon
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_sysconfdir}/mateconf/schemas/mate-notification-daemon.schemas
%{_bindir}/mate-notification-properties
%{_libexecdir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.mate.Notifications.service
%{_datadir}/mate-notification-daemon/mate-notification-properties.ui
%{_iconsdir}/hicolor/*/apps/*

