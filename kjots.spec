Name:           kjots
Version:        5.1.1
Release:        3
Summary:        Note Taker for Plasma 5
Group:          Office
License:        GPLv2 and LGPLv2+
Url:            https://www.kde.org/applications/utilities/kjots/
Source0:        http://download.kde.org/stable/kjots/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5TextWidgets)

BuildRequires:  xsltproc

%description
KJots organises all of your notes into separate books.

Features :
   - Multiple books handled.
   - Each book has many named pages.
   - Books and pages can be rearranged by drag-and-drop.
   - Keyboard shortcuts are available for many functions.
   - Automatic saving means your notes are safe from loss.

%files -f %{name}.lang
%doc README
%{_kde5_bindir}/kjots
%{_qt5_plugindir}/kjotspart.so
%{_qt5_plugindir}/kcm_kjots.so
%{_qt5_plugindir}/pim5/kontact/kontact_kjotsplugin.so
%{_kde5_applicationsdir}/org.kde.%{name}.desktop
%{_kde5_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_kde5_datadir}/config.kcfg/%{name}.kcfg
%{_kde5_datadir}/%{name}/
%{_kde5_datadir}/kxmlgui5/%{name}/
%{_kde5_services}/%{name}_config_misc.desktop
%{_kde5_services}/%{name}part.desktop
%{_kde5_iconsdir}/hicolor/*/apps/%{name}.*

#-------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name}

