Name:           cromite
Version:        %(curl -s https://api.github.com/repos/uazo/cromite/tags | jq -r '.[0].name' | cut -f2 -dv | cut -f1 -d.)
Release:        %(curl -s https://api.github.com/repos/uazo/cromite/tags | jq -r '.[0].name' | cut -f2 -dv | cut -f2-4 -d. | cut -f1 -d-)
Summary:        Secure and private web browser
BuildRequires:  jq curl

License:        GPL-3.0-only
URL:            https://www.cromite.org/
Source0:        https://github.com/uazo/cromite/releases/latest/download/chrome-lin64.tar.gz

%global debug_package %{nil}

%description
Cromite is a secure and private web browser.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}/opt
tar -xzf %{SOURCE0} -C %{buildroot}/opt
mkdir -p %{buildroot}/usr/share/applications
cat > %{buildroot}/usr/share/applications/cromite.desktop << CROMITEEOF
[Desktop Entry]
Name=Cromite
Comment=Surf the web
Exec=/opt/chrome-lin/chrome %u
Icon=/opt/chrome-lin/product_logo_48.png
MimeType=text/html;application/xhtml_xml;x-scheme-handler/http;x-scheme-handler/https;
Terminal=false
Type=Application
Categories=Network;WebBrowser;
CROMITEEOF

%files
/opt/chrome-lin/*
/usr/share/applications/cromite.desktop
