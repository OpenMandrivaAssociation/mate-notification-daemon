%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Notification Daemon
Name:		mate-notification-daemon
Version:	1.18.0
Release:	1
License:	GPLv2+
Group:		System/Servers
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libwnck-3.0)
#BuildRequires:	pkgconfig(mate-desktop-2.0)
Requires:	libnotify
Provides:	virtual-notification-daemon
#Conflicts:	xfce4-notifyd

%description
A daemon that displays passive pop-up notifications as per the
Desktop Notifications spec (http://galago.info/specs/notification/index.php).

%prep
%setup -q
%apply_patches

%build
#NOCONFIGURE=yes ./autogen.sh
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/mate-notification-properties
%{_libexecdir}/%{name}
%dir %{_libdir}/mate-notification-daemon
%dir %{_libdir}/mate-notification-daemon/engines
%{_libdir}/mate-notification-daemon/engines/libcoco.so
%{_libdir}/mate-notification-daemon/engines/libnodoka.so
%{_libdir}/mate-notification-daemon/engines/libslider.so
%{_libdir}/mate-notification-daemon/engines/libstandard.so
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.mate.Notifications.service
%{_datadir}/glib-2.0/schemas/org.mate.NotificationDaemon.gschema.xml
%{_datadir}/mate-notification-daemon/mate-notification-properties.ui
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/mate-notification-properties.1*

