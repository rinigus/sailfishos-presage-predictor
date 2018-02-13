# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       presage_predictor

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    PresagePredictor
Version:    1.0
Release:    7
Group:      Applications/Text
License:    GPLv3
URL:        https://github.com/martonmiklos/sailfishos-presage-predictor
Source0:    %{name}-%{version}.tar.bz2
Source100:  presage_predictor.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   jolla-keyboard
Requires:   presage-data
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  libpresage-devel
BuildRequires:  libmarisa-devel

%description
Keyboard prediction plugin based on the Presage prediction engine

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%post
# >> post
su - nemo -c "/bin/systemctl --user restart maliit-server.service"
# << post

%postun
# >> postun
su - nemo -c "/bin/systemctl --user restart maliit-server.service"
# << postun

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/hu/mm/presagepredictor/libPresagePredictor.so
%{_libdir}/qt5/qml/hu/mm/presagepredictor/qmldir
%{_datadir}/maliit/plugins/com/jolla/PresageInputHandler.qml
# >> files
# << files
