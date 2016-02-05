Summary:	osslsigncode - simple Microsoft signtool.exe replacement
Summary(pl.UTF-8):	osslsigncode - prosty zastępnik Microsoftowego narzędzia signtool.exe
Name:		osslsigncode
Version:	1.7.1
Release:	1
License:	GPL v3+
Group:		Applications/Crypto
Source0:	http://downloads.sourceforge.net/osslsigncode/%{name}-%{version}.tar.gz
# Source0-md5:	ac5655b9281b692423ecb2e9185f09d7
URL:		http://osslsigncode.sourceforge.net/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	libgsf-devel
BuildRequires:	openssl-devel
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

%{__rm} aclocal.m4

%build
%{__libtoolize}
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
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/osslsigncode
