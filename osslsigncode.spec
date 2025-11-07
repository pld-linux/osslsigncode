Summary:	osslsigncode - simple Microsoft signtool.exe replacement
Summary(pl.UTF-8):	osslsigncode - prosty zastępnik Microsoftowego narzędzia signtool.exe
Name:		osslsigncode
Version:	2.10
Release:	1
License:	GPL v3+ with OpenSSL exception
Group:		Applications/Crypto
#Source0Download: https://github.com/mtrojnar/osslsigncode/releases
Source0:	https://github.com/mtrojnar/osslsigncode/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e23eeb2bd053aa7172b23b61f040509d
URL:		https://github.com/mtrojnar/osslsigncode
BuildRequires:	cmake >= 3.17
BuildRequires:	openssl-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	zlib-devel
Requires:	openssl >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
osslsigncode is a small tool that implements part of the functionality
of the Microsoft tool signtool.exe - more exactly the Authenticode
signing and timestamping. But osslsigncode is based on OpenSSL and
cURL, and thus should be able to compile on most platforms where these
exist.

%description -l pl.UTF-8
osslsigncode jest małym narzędziem udostępniającym funkcjonalność
narzędzia signtool.exe firmy Microsoft, służącego do cyfrowego
podpisywania i znakowania czasowego. osslsigncode bazuje jednakże
na bibliotekach OpenSSL i cURL więc może być używany na platformach
posiadających te biblioteki.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt NEWS.md README.md TODO.md
%attr(755,root,root) %{_bindir}/osslsigncode
%{bash_compdir}/osslsigncode.bash
