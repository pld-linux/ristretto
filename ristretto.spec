Summary:	Picture-viewer for the Xfce desktop environment
Summary(pl.UTF-8):	Przeglądarka obrazów dla środowiska Xfce
Name:		ristretto
Version:	0.13.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	https://archive.xfce.org/src/apps/ristretto/0.13/%{name}-%{version}.tar.xz
# Source0-md5:	680765bdecaf1b465ca3af7fbea7f6c4
Patch0:		%{name}-desktop.patch
URL:		https://goodies.xfce.org/projects/applications/ristretto/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libexif-devel >= 0.6.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfconf-devel >= 4.16.0
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
%patch -P0 -p1

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie,ur_PK}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

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
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/org.xfce.%{name}.desktop
%{_datadir}/metainfo/org.xfce.ristretto.appdata.xml
%{_iconsdir}/hicolor/*/*/*
