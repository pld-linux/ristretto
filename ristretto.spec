Summary:	Picture-viewer for the Xfce desktop environment
Summary(pl):	Przegl±darka obrazów dla ¶rodowiska Xfce
Name:		ristretto
Version:	0.0.9
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://goodies.xfce.org/releases/ristretto/%{name}-%{version}.tar.gz
# Source0-md5:	67c7b6b33b4227a33bbbc787b15dafb2
URL:		http://goodies.xfce.org/projects/applications/ristretto
BuildRequires:	Thunar-devel >= 0.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.12
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libexif-devel >= 0.6
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ristretto is a fast and lightweight picture-viewer for the Xfce
desktop environment.

%description -l pl
Ristretto jest szybk± i lekk± przegladark± obrazów dla ¶rodowiska
Xfce.

%prep
%setup -q

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

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{nb_NO,nb}
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
