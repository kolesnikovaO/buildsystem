Name:           HelloApp
Version:        curversion
Release:        0
Summary:        Some summary


BuildArch:      noarch
License:        GPL
Source:         appname.tar.gz

%description
Test app

%build
cmake .
cmake --build .


