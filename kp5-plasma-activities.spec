#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.93.0
%define		qtver		5.15.2
%define		kpname		plasma-activities
%define		kf5ver		5.39.0

Summary:	plasma activities
Name:		kp5-%{kpname}
Version:	5.93.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	c2de09a34a1ac93be88a7b61716ee1ae
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= 5.15.0
BuildRequires:	Qt6Gui-devel >= 5.15.0
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.82
BuildRequires:	kf5-kauth-devel >= 5.82
BuildRequires:	kf5-kcoreaddons-devel >= 5.85.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.82
BuildRequires:	kf5-kdeclarative-devel >= 5.82
BuildRequires:	kf5-ki18n-devel >= 5.82
BuildRequires:	kf5-kio-devel >= 5.82
BuildRequires:	kf5-knotifications-devel >= 5.82
BuildRequires:	kf5-kservice-devel >= 5.85.0
BuildRequires:	kf5-solid-devel >= 5.85.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
plasma activities.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasma-activities-cli6
%attr(755,root,root)%{_libdir}/libPlasmaActivities.so.*.*
%ghost %{_libdir}/libPlasmaActivities.so.6
%dir %{_libdir}/qt6/qml/org/kde/activities
%{_libdir}/qt6/qml/org/kde/activities/kde-qmlmodule.version
%attr(755,root,root)%{_libdir}/qt6/qml/org/kde/activities/libplasmaactivitiesextensionplugin.so
%{_libdir}/qt6/qml/org/kde/activities/plasmaactivitiesextensionplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/activities/qmldir
%{_datadir}/qlogging-categories6/plasma-activities.categories
%{_datadir}/qlogging-categories6/plasma-activities.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/PlasmaActivities
%{_libdir}/cmake/PlasmaActivities
%{_libdir}/libPlasmaActivities.so
%{_pkgconfigdir}/PlasmaActivities.pc
