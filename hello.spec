Name:           Hello App
Version:        curversion
Release:        0
Summary:        Some summary


BuildArch:      noarch
License:        GPL
Source:         hello.tar.gz

%description
Test app

%build
cp -r /home/agent/rpmbuild/SOURCES/hello/* /home/agent/rpmbuild/BUILD/
cmake .
