#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Const-Fast
Version  : 0.014
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Const-Fast-0.014.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Const-Fast-0.014.tar.gz
Summary  : 'Facility for creating read-only scalars, arrays, and hashes'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Const-Fast-license = %{version}-%{release}
Requires: perl-Const-Fast-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
This archive contains the distribution Const-Fast,
version 0.014:
Facility for creating read-only scalars, arrays, and hashes

%package dev
Summary: dev components for the perl-Const-Fast package.
Group: Development
Provides: perl-Const-Fast-devel = %{version}-%{release}
Requires: perl-Const-Fast = %{version}-%{release}

%description dev
dev components for the perl-Const-Fast package.


%package license
Summary: license components for the perl-Const-Fast package.
Group: Default

%description license
license components for the perl-Const-Fast package.


%package perl
Summary: perl components for the perl-Const-Fast package.
Group: Default
Requires: perl-Const-Fast = %{version}-%{release}

%description perl
perl components for the perl-Const-Fast package.


%prep
%setup -q -n Const-Fast-0.014
cd %{_builddir}/Const-Fast-0.014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Const-Fast
cp %{_builddir}/Const-Fast-0.014/LICENSE %{buildroot}/usr/share/package-licenses/perl-Const-Fast/157b00fae6a2ed99f867d86298ed2d383290e6c7
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Const::Fast.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Const-Fast/157b00fae6a2ed99f867d86298ed2d383290e6c7

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Const/Fast.pm
