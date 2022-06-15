#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Const-Fast
Version  : 0.9929
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/version-0.9929.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/version-0.9929.tar.gz
Summary  : 'Structured version objects'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Const-Fast-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
version 0.9929
==================================
Object oriented versions for all Perl releases from 5.6.2 onward.  Replaces
the core version code for all Perl releases from 5.10.0 onwards.

%package perl
Summary: perl components for the perl-Const-Fast package.
Group: Default
Requires: perl-Const-Fast = %{version}-%{release}

%description perl
perl components for the perl-Const-Fast package.


%prep
%setup -q -n version-0.9929
cd %{_builddir}/version-0.9929

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

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
## Remove excluded files
rm -f %{buildroot}*/usr/share/man/man3/version.3
rm -f %{buildroot}*/usr/share/man/man3/version::Internals.3

%files
%defattr(-,root,root,-)

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
