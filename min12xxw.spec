Summary:	Minolta PagePro 1[23]xxW printers driver
Summary(pl):	Sterownik drukarek Minolta PagePro 1[23]xxW
Name:		min12xxw
Version:	0.0.7
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.hinterbergen.de/mala/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	b1dd30f2737396a40aeaf912c365686a
URL:		http://www.hinterbergen.de/mala/min12xxw/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the driver for Minolta PagePro 1[23]xxW printers. 
Currently, it is in beta state of development.
The driver operates by reading a stream in pbmraw format produced by 
ghostscript and converting it to the language the printer can actually 
understand. 

%description -l pl
To jest sterownik dla drukarek Minolta PagePro 1[23]xxW.
Aktualnie jest w fazie beta rozwoju.
Sterownik czyta strumieñ w formacie pbmraw wyprodukowanego przez program
ghostscript i konwertuje go do jêzyka zrozumia³ego przez drukarkê.

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
