Name:           HelloApp
Version:        curversion
Release:        0
Summary:        Some summary
License:        GPL
Source:         appname.tar.gz

%description
Test app

%build
cmake .
cmake --build .

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -m755 -D hello_app $RPM_BUILD_ROOT%{_libdir}/hello_app

%files
%{_libdir}/hello_app


