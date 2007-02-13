Summary:	Minolta PagePro 1[23]xxW printers driver
Summary(pl.UTF-8):	Sterownik dla drukarek Minolta PagePro 1[23]xxW
Name:		min12xxw
Version:	0.0.9
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.hinterbergen.de/mala/min12xxw/%{name}-%{version}.tar.gz
# Source0-md5:	3582da7bd8d2d612b1fbcbfdb8b3239a
URL:		http://www.hinterbergen.de/mala/min12xxw/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the driver for Minolta PagePro 1[23]xxW printers. Currently,
it is in beta state of development. The driver operates by reading a
stream in pbmraw format produced by ghostscript and converting it to
the language the printer can actually understand.

%description -l pl.UTF-8
To jest sterownik dla drukarek Minolta PagePro 1[23]xxW. Aktualnie
jest w fazie beta rozwoju. Sterownik czyta strumień w formacie pbmraw
wyprodukowany przez program ghostscript i konwertuje go do języka
zrozumiałego przez drukarkę.

%prep
%setup -q

%build
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
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
