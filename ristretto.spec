Summary:	Picture-viewer for the Xfce desktop environment
Summary(pl.UTF-8):	Przeglądarka obrazów dla środowiska Xfce
Name:		ristretto
Version:	0.0.91
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://archive.xfce.org/src/apps/ristretto/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	1df541b920f044ac9f3731b2a0fe02d1
Patch0:		%{name}-desktop.patch
URL:		http://goodies.xfce.org/projects/applications/ristretto/
BuildRequires:	Thunar-devel >= 1.1.0
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.31
BuildRequires:	libexif-devel >= 0.6.0
BuildRequires:	libxfce4util-devel >= 4.7.0
BuildRequires:	libxfcegui4-devel >= 4.7.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.7.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ristretto is a fast and lightweight picture-viewer for the Xfce
desktop environment.

%description -l pl.UTF-8
Ristretto jest szybką i lekką przeglądarką obrazów dla środowiska
Xfce.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/*
