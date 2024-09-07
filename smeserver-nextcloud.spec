%define release 32
%define version 1.2.0

Summary: Koozali SME Server Nextcloud configuration
Name: smeserver-nextcloud
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.xz

BuildArch: noarch
URL: https://www.nextcloud.com 

BuildRequires: e-smith-devtools

Requires: nextcloud-src >= 26.0.1
Requires: e-smith-apache
Requires: e-smith-mysql
Requires: smeserver-webapps-common
Requires: smeserver-php >= 3.0.0-15
Requires: samba-client
Requires: perl-JSON
Requires: perl-Exporter-Tiny
Requires: perl-Sub-Quote
Requires: php74-php-smbclient
Requires: php74-php-opcache
Requires: php74-php-pecl-apcu
Requires: php74-php-pecl-inotify
Requires: php74-php-pecl-zip
Requires: php74-php-pecl-imagick
Requires: php74-php-gmp
Requires: php81-php-smbclient
Requires: php81-php-opcache
Requires: php81-php-pecl-apcu
Requires: php81-php-pecl-inotify
Requires: php81-php-pecl-zip
Requires: php81-php-pecl-imagick
Requires: php81-php-gmp
Requires: php81-php-redis
Requires: smeserver-redis
Requires: jq
Requires: smeserver-mariadb105
Requires: e-smith-apache >= 2.6.0-19
Requires: smeserver-php >= 3.0.0-43

%description
Koozali SME Server Nextcloud files and configuration.


%prep
%setup
touch  root/etc/e-smith/templates/etc/opt/remi/php81/php.d/20-opcache.ini/template-begin

%build
perl createlinks

%install
rm -rf %{buildroot}
mkdir -p root/var/log/php/nextcloud
(cd root; find . -depth -print | cpio -dump %{buildroot})
/sbin/e-smith/genfilelist %{buildroot} \
 --dir /var/log/php/nextcloud  'attr(0755,www,www)' \
 --dir /var/lib/php/nextcloud  'attr(0755,www,www)' \
 --dir /var/lib/php/nextcloud/tmp 'attr(0755,www,www)' \
 --dir /var/lib/php/nextcloud/opcache 'attr(0755,www,www)' \
 --dir /var/lib/php/nextcloud/session 'attr(0755,www,www)' \
 --dir /home/e-smith/files/nextcloud 'attr(0755,www,www)' \
 --dir /home/e-smith/files/nextcloud/data 'attr(0755,www,www)' \
 --ignoredir "/etc/sudoers.d" \
 --file "/etc/sudoers.d/90_nextcloud" "attr(0440,root,root)" \
 --file /usr/bin/occ 'attr(0755,root,root)'\
 --file /usr/bin/nc_dbupdate 'attr(0755,root,root)'\
 > %{name}-%{version}-filelist

cat %{name}-%{version}-filelist
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING


%changelog
* Sat Sep 07 2024 cvs2git.sh aka Brian Read <brianr@koozali.org> 1.2.0-32.sme
- Roll up patches and move to git repo [SME: 12338]

* Sat Sep 07 2024 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.

* Thu May 16 2024 Jean-Philippe Pialasse <jpp@koozali.org> 1.2.0-31.sme
- fix php version on initial install [SME: 12685]

* Fri Apr 12 2024 Jean-Philippe Pialasse <jpp@koozali.org> 1.2.0-30.sme
- add maintenance windows start [SME: 12611]
  increase frequency of cron task every 5 min
- fix missing full path [SME: 12486]

* Mon Jan 29 2024 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-29.sme
- require nextcloud-src >= 26 [SME: 12318]
  multiple fixes and rewrites
- restore default log level [SME: 12412]

* Sat Sep 09 2023 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-28.sme
- workaround opcache segfault with php 81 using in memory only [SME: 12298]
- index file cache using Redis [SME: 12401]

* Sat Sep 09 2023 John Crisp <jcrisp@safeandsoundit.co.uk> 1.2.0-27.sme
- Fix syntax error in 20opcache.ini [SME: 12298]

* Sat Aug 19 2023 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-26.sme
- fix missing template-begin 

* Tue Aug 08 2023 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-25.sme
- make php81 compatible for NC 25 and higher [SME: 12298]
- requires php81-redis [SME: 12401]
- recognize need cpuinfo access [SME: 12339 ]
- remove simple signup link [SME: 12329]

* Wed Feb 08 2023 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-24.sme
- increase action script speed [SME: 12319]

* Sat Jan 21 2023 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-23.sme
- typo fix [SME: 11890] 

* Wed Jan 11 2023 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-22.sme
- use of runuser in place of sudo -u [SME: 11890]
  usage of /usr/bin/occ where possible
  removal of /usr/bin/OCC

* Mon Jan 09 2023 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-21.sme
- update disabled_fucntions list [SME: 12277]
- allow customization of opcache for Nextcloud see wiki [SME: 12299]
- actions scripts update

* Wed Nov 23 2022 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-20.sme
- set overwrite.cli.url [SME: 12208]
- allow shell_exec [SME: 12187]
- fix username conflict with group name [SME: 12241]

* Sat Jul 30 2022 Brian Read <brianr@bjsystems.co.uk> 1.2.0-19.sme
- Re-build and link to latest devtools [SME: 11997]

* Fri Jul 08 2022 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-18.sme
- update httpd fragment for httpd2.4 syntax [SME: 12053]

* Fri Jul 08 2022 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-17.sme
- Re-build and link to latest devtools gencache again [SME: 12096]
- Re-build and link to latest devtools ldap users/groups not availables on first run [SME: 12095]

* Thu Jul 07 2022 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-16.sme
- migrate property CloudDomain to VirtualHost [SME: 11918]
- use mariadb105 on new installs [SME: 11343]
- update rewriterules [SME: 11972]
- update to NC24 [SME: 12094]
  use a nextcloud-src rpm and avoid conflicts between web and rpm updates
- add to backup [SME: 12016]

* Fri May 20 2022 Terry Fage <terry@fage.au> 1.2.0-15.sme
- Re-build and link to latest devtools cron syntax error [SME: 11854]

* Wed May 18 2022 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-14.sme
- Re-build and link to latest devtools gencache_init failed [SME: 11855]
  fix missing nextcloud-conf action in update event

* Wed May 18 2022 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-12.sme
- use php_pecl-apcu for cli [SME: 11920]
- db update of keys and indexes [SME: 11854]
- few nextcloud-occ-conf fixes [SME: 11973]
  make occ used in scripts rather than OCC

* Sun Jun 06 2021 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-11.sme
- Re-build and link to latest devtools logrotate error [SME: 11172]
- Re-build and link to latest devtools noise in error log

* Sun Jun 06 2021 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-9.sme
- Re-build and link to latest devtools dav redirections for domain use and subdir  [SME: 11086]
- refresh externalfs on loading, best for ibays
- tidying 

* Sun Jun 06 2021 Jean-Philippe Pialasse <tests@pialasse.com> 1.2.0-8.sme
- add update event [SME: 11086] 
- add occ as hard link of OCC

* Fri Dec 18 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 1.2.0-7.sme
- Fix typo in php pool template [SME: 11268]

* Tue Dec 01 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 1.2.0-6.sme
- Add a check for the Min/Max/Start servers [SME: 11171]
- https://bugs.contribs.org/show_bug.cgi?id=11171#c4

* Mon Nov 16 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 1.2.0-5.sme
- Template missing Min/Start/Max Servers and Children [SME: 11171]

* Thu Nov 12 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 1.2.0-4.sme
- Add missing SMB configuration details including domain/workgroup

* Mon Nov 09 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 1.2.0-3.sme
- Fix sudoer file permissions in file list
- Fix some install bugs
- typo in httpd.conf
- switch db from mysql to maria db
- update php version
- add Requires

* Sun Nov 08 2020 Jean-Philipe Pialasse <tests@pialasse.com> 1.2.0-2.sme
- use username as id in place of ldap uuid [SME: 10876]

* Sun Nov 08 2020 Jean-Philipe Pialasse <tests@pialasse.com> 1.2.0-1.sme
- initial SME10 import [SME: 11086]

* Sun Nov 08 2020 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-19.sme
- use php73-fpm [SME: 11003]
- Require php-gmp for Nextcloud 19 and newer [SME: 11004]
- add phpbasedir support so you can add individual access to dir or files [SME: 11083]
  simply use nextcloud PHPBaseDir property
- increase FastCgiExternalServer php pool timeout to 300 [SME: 11084]
- ease use of a dedicated domaine with https [SME: 10885]

* Mon Jan 27 2020 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-16.sme
- Re-build and link to latest devtools missing Requirement and template-begins  [SME: 10852]

* Mon Dec 16 2019 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-15.sme
- use php72-fpm instead of php71-fpm [SME: 10852]

* Sun Feb 17 2019 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-14.sme
- Re-build and link to latest devtools 512MB error on events [SME: 10728]
- add requirement for inotify support [SME: 10733]

* Wed Jan 16 2019 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-13.sme
- Re-build and link to latest devtools /.well-known check [SME: 10709]
- created a OCC command you can call as root as if you were the right user. [SME: 10711]
- night cron to fix db [SME: 10710 ]

* Mon Jan 07 2019 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-11.sme
- increase memory limit to new default from 128M to 512M [SME: 10695]
  add property to nextcloud db key MemoryLimit to set to local value if needed.

* Thu Dec 20 2018 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-10.sme
- Re-build and link to latest devtools /var/log/php/nextcloud/ is missing [SME: 10601]

* Wed Dec 19 2018 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-9.sme
- Re-build and link to latest devtools timeout on update [SME: 10596]

* Wed Jul 04 2018 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-8.sme
- Re-build and link to latest devtools wrong filter name for fail2ban jail.conf  [SME: 10608]

* Wed Apr 11 2018 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-7.sme
- Re-build and link to latest devtools long update [SME: 10564]
- Re-build and link to latest devtools IncludeIbay not working.

* Wed Apr 11 2018 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-6.sme
- Re-build and link to latest devtools shares not correctly handled [SME: 10564]
- improve shares support
- reload file cache after creation of ibays folder, so it displays to users.
- improve output to message log

* Mon Apr 09 2018 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-5.sme
- Re-build and link to latest devtools signal-event nextcloud-update hang [SME: 10560]

* Sun Apr 08 2018 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-4.sme
- Re-build and link to latest devtools wrong logrotate option [SME: 10560]
- change password storage mode for smb share to allow access from portable devices [SME: 10558]
- create the "ibays" main folder to mount all ibays in every user nextcloud space [SME: 10557]
- add Shared folders in nextcloud under the ibays folder [SME: 10559]

* Sat Apr 07 2018 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-3.sme
- tidying templates, set cron update
- Re-build and link to latest devtools bad folder name for ibays [SME: 10556]

* Fri Mar 30 2018 Jean-Philipe Pialasse <tests@pialasse.com> 1.1.0-1.sme
- initial release

