Summary:	Picture-viewer for the Xfce desktop environment
Summary(pl.UTF-8):	Przeglądarka obrazów dla środowiska Xfce
Name:		ristretto
Version:	0.6.3
Release:	2
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://archive.xfce.org/src/apps/ristretto/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	6b8c9a5d7ed319e4c84a9fefaa18792c
Patch0:		%{name}-desktop.patch
URL:		http://goodies.xfce.org/projects/applications/ristretto/
BuildRequires:	Thunar-devel >= 1.2.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.31
BuildRequires:	libexif-devel >= 0.6.0
BuildRequires:	libxfce4util-devel >= 4.11.0
BuildRequires:	libxfce4ui-devel >= 4.11.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.11.0
Requires(post,postun):	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
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
%{__intltoolize}
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

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

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
