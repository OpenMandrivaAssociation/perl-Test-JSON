%define upstream_name    Test-JSON
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Test JSON data
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(JSON)
BuildRequires:	perl(JSON::Any)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Test::Tester)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
JavaScript Object Notation (JSON) is a lightweight data interchange format.
the Test::JSON manpage makes it easy to verify that you have built valid
JSON and that it matches your expected output.

See the http://www.json.org/ manpage for more information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 656838
- br json
- rebuild for updated spec-helper

* Fri Aug 27 2010 Shlomi Fish <shlomif@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 573481
- import perl-Test-JSON

