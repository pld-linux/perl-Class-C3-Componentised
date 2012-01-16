#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	C3-Componentised
Summary:	Class::C3::Componentised - Load mix-ins or components to your C3-based class
Summary(pl.UTF-8):	Class::C3::Componentised - wczytywanie komponentów do klas opartych na C3
Name:		perl-Class-C3-Componentised
Version:	1.0009
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a8a8db7e58f13043ec3658fc8cbd652d
URL:		http://search.cpan.org/dist/Class-C3-Componentised/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Load mix-ins or components to your C3-based class. This will inject
base classes to your module using the Class::C3 method resolution
order.

%description -l pl.UTF-8
Ten moduł wczytuje obiekty mieszane lub komponenty do klas opartych na
C3. Wstawia klasy bazowe do moduły w kolejności rozwiązywania metod
Class::C3.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/C3/*.pm
%{_mandir}/man3/*
