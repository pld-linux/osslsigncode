Summary:	osslsigncode - simple Microsoft signtool.exe replacement
Summary(pl.UTF-8):	osslsigncode - prosty zastępnik Microsoftowego narzędzia signtool.exe
Name:		osslsigncode
Version:	2.0
Release:	2
License:	GPL v3+ with OpenSSL exception
Group:		Applications/Crypto
#Source0Download: https://github.com/mtrojnar/osslsigncode/releases
Source0:	https://github.com/mtrojnar/osslsigncode/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4ff4c4e9678af04fb7ba1b2baed048d7
URL:		https://github.com/mtrojnar/osslsigncode
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.12.0
BuildRequires:	libgsf-devel
BuildRequires:	openssl-devel >= 1.1.0
BuildRequires:	pkgconfig
Requires:	curl-libs >= 7.12.0
Requires:	openssl >= 1.1.0
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.txt README.md README.unauthblob.md TODO.md
%attr(755,root,root) %{_bindir}/osslsigncode
