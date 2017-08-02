%{?scl:%scl_package plexus-interactivity}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}plexus-interactivity
Version:        1.0
Release:        0.23.alpha6.1%{?dist}
Epoch:          0
Summary:        Plexus Interactivity Handler Component
License:        MIT
URL:            https://github.com/codehaus-plexus/plexus-interactivity
BuildArch:      noarch
# svn export \
#   http://svn.codehaus.org/plexus/plexus-components/tags/plexus-interactivity-1.0-alpha-6/
# tar caf plexus-interactivity-1.0-alpha-6-src.tar.xz \
#   plexus-interactivity-1.0-alpha-6
Source0:        plexus-interactivity-1.0-alpha-6-src.tar.xz
Patch1:         plexus-interactivity-dependencies.patch
Patch2:         plexus-interactivity-jline2.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(jline:jline) >= 2
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-api)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%package api
Summary:        API for %{pkg_name}

%description api
API module for %{pkg_name}.

%package jline
Summary:        jline module for %{pkg_name}

%description jline
jline module for %{pkg_name}.

%prep
%setup -q -n plexus-interactivity-1.0-alpha-6
%patch1 -p1
%patch2 -p1

%mvn_file ":{plexus}-{*}" @1/@2

%build
%mvn_package ":plexus-interactivity"

%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles

%files api -f .mfiles-plexus-interactivity-api

%files jline -f .mfiles-plexus-interactivity-jline

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 0:1.0-0.23.alpha6.1
- Automated package import and SCL-ization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-0.23.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.0-0.22.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.21.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.20.alpha6
- Update upstream URL

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.19.alpha6
- Rebuild to fix Maven auto-requires

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.18.alpha6
- Rebuild to fix requires and provides

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.17.alpha6
- Fix build-requires on plexus-components-pom

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.16.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.15.alpha6
- Use Requires: java-headless rebuild (#1067528)

* Fri Feb 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.14.alpha6
- Remove requires on subpackages from main package

* Fri Feb 21 2014 Michael Simacek <msimacek@redhat.com> - 0:1.0-0.13.alpha6
- Split into subpackages

* Tue Oct 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.12.alpha6
- Build with XMvn
- Remove %%pre javadoc scriplet
- Port to jline2, resolves: rhbz#1022978

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.11.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.10.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.0-0.9.alpha6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 11 2012 Michal Srb <msrb@redhat.com> - 0:1.0-0.8.alpha6
- Removed dependency on plexus-container-default (Resolves: #878573)
- Fixed rpmlint warning

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.7.alpha6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.6.alpha6
- Add patch to fix build issues

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.5.a6.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a6.8
- Build with maven 3.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.4.a6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  1 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.3.a6.7
- Fix pom filenames (Resolves rhbz#655821)
- Cleanups according to new guidelines

* Wed Oct 6 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.6
- Use javadoc:aggregate.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.5
- Really fix depmaps.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.4
- Add parent/subname defines to fix poms/depmaps.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.3.a6.3
- Update to alpha 6.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.3.a5.2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.2.a5.2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-0.1.a5.2.3
- drop repotag
- fix license tag

* Tue Mar 13 2007 Matt Wringe <mwringe@redhat.com> 1.0-0.1.a5.2jpp.2
- Add missing build requires for ant-nodeps

* Fri Feb 16 2007 Andrew Overholt <overholt@redhat.com> 1.0-0.1.a5.2jpp.1
- Remove javadoc symlinking

* Thu Feb 23 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.0-0.a5.2jpp
- First JPP 1.7 build
- With remavenization to 1.1 by Deepak Bhole <dbhole@redhat.com>

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a5.1jpp
- First JPackage build
