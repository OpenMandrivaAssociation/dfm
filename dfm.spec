Name:		dfm
Summary:	Dino file manager
Version:	0.5
Release:	1
License:	GPLv3+
Group:		Graphical desktop/Other
URL:		http://dfm.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/dfm/src/Dino_src-%{version}.tar.gz
BuildRequires:	qt4-devel
BuildRequires:	imagemagick

%description
Dino is an easy to use and powerful file manager built in Qt. It’s features
include symlinking files by mouse click, the usual features such as making
directories, run commands, copying & pasting..etc; drag and drop and even
a built in text editor.

%prep
%setup -q

%build
%qmake_qt4
%make
lrelease Dino.pro

%install
#make install INSTALL_ROOT=%{buildroot}

%__install -d %{buildroot}%{_datadir}/Dino/translations/
%__install -d %{buildroot}%{_datadir}/applications/

%__install -D -m 755 Dino %{buildroot}%{_bindir}/Dino
%__cp -a translations/Dino_*.qm %{buildroot}%{_datadir}/Dino/translations/
%__install -D -m 644 dino.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/dino.png
for size in 16 32 48
do
%__install -d -m 755 %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/
convert -resize ${size}x${size} dino.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/dino.png
done

cat > %{buildroot}%{_datadir}/applications/Dino.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Dino
GenericName=Dino
Comment=Simple File Manager
Exec=Dino
Icon=dino
Terminal=false
Type=Application
StartupNotify=false
Categories=FileTransfer;Utility;FileManager;Qt;
EOF

%if %{mdvver} >= 201200
%find_lang Dino --with-qt
%else
cat > Dino.lang << EOF
%lang(ru) /usr/share/Dino/translations/Dino_ru.qm
%lang(sr_BA) /usr/share/Dino/translations/Dino_sr_BA.qm
%lang(de) /usr/share/Dino/translations/Dino_de.qm
%lang(sr_RS) /usr/share/Dino/translations/Dino_sr_RS.qm
EOF
%endif

%files -f Dino.lang
%{_bindir}/Dino
%{_datadir}/applications/Dino.desktop
%{_iconsdir}/hicolor/*/apps/dino.*
%doc CHANGELOG README
