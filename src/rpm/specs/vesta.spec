Name:           vesta
Version:        0.9.8
Release:        3
Summary:        Vesta Control Panel
Group:          System Environment/Base
License:        GPL
URL:            http://vestacp.com/
Vendor:         vestacp.com
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       redhat-release >= 5
Provides:       vestacp vesta-api vesta

%define         _vestadir  /usr/local/%{name}

%description
This package contains the packages for Vesta Control Panel api.

%prep
%setup -q -n %{name}-%{version}

%build
gcc -lcrypt src/v-check-user-password.c -o bin/v-check-user-password

%install
install -d  %{buildroot}%{_vestadir}
%{__cp} -ad ./* %{buildroot}%{_vestadir}

%clean
rm -rf %{buildroot}

%post
if [ $1 -ge 2 ]; then
    if [ -e /usr/local/vesta/upd/convert-templates.sh ]; then
        /usr/local/vesta/upd/convert-templates.sh
    fi
fi

%files
%{_vestadir}
%config(noreplace) %{_vestadir}/web/images/logo.png
%config(noreplace) %{_vestadir}/web/images/favicon.ico

%changelog
* Mon Jul 29 2013 Serghey Rodin <builder@vestacp.com> - 0.9.8-3
- Fixed issue with uppercase domains
- Implemented JS hints when adding database or ftp domain
- Package trigger support
- Improved html structure
- Debian/Ubuntu addoptation
- Czech language support


* Mon Jun 10 2013 Serghey Rodin <builder@vestacp.com> - 0.9.8-2
- Fixed missing ssl certificate on restore
- Fixed wrong disk usage key
- Added nginx trigger for templates
- Added template update function


* Mon May 27 2013 Serghey Rodin <builder@vestacp.com> - 0.9.8-1
- DNS Cluster
- JS: select checkbox by clicking on a row
- Record order change functions
- Fix for ns3 and ns4 support
- Web-log viewer
- Fixed i18n login bug
- New template logic
- RSSH shell on additional web users
- Romanian language file
- Edit user from topmenu links
- Highlighted active links

* Mon Apr 08 2013 Serghey Rodin <builder@vestacp.com> - 0.9.7-21
- Fix for null data in bandwidth calculation
- Fix from Magentron for updating or deleting SSL certificates
- Fix from Magentron for database host validation

* Fri Apr 05 2013 Serghey Rodin <builder@vestacp.com> - 0.9.7-21
- i18n fix for IDN domain names
- fixed bandwidth calculation

* Tue Apr 03 2013 Serghey Rodin <builder@vestacp.com> - 0.9.7-20
- email notifcation on backup error
- backup now saves file permissions
- web backup scheduler
- improved web/dns rebuild functions
- fix for idn mail domains
- added script for ftp backup config
- added restore function
- added vsftpd pasv_address trigger
- SNI support on shared IP
- Increasing contrast on top panel
- Nginx repo integration
- Improved template structure

* Thu Mar 05 2013 Serghey Rodin <builder@vestacp.com> - 0.9.7-19
- Inconsistent archive removal when backup failed
- Fixed mail config removal
- Removed  email notification if database hasn't been created
- Fixed BW calculation bug
- Spanish translation
- APC will be installed by default
- Even more clean looking html

* Wed Feb 27 2013 Serghey Rodin <builder@vestacp.com> - 0.9.7-18
- Web API wrapper
- WHMCS support module
- Reread system ip addresses function
- Fix for missing package names begin with numbers
- Fixed bug on ip removal
- Fix for shell change in package
- HTML code fix for submenu
- Fix for broken dns unsuspend function
- Improved traffic calc function
- Fixed incomplete mail account listing bug

* Mon Feb 18 2013 Serghey Rodin <builder@vestacp.com> - 0.9.7-17
- fixed blank screen on bad login
- ftp account uid same as uid of main user
- support for NATed network
- phpMyadmin/pgMyAdmin links to remote database servers
- new installer (info about packages)
- dns records remains alive on suspend

* Mon Jan 28 2013 Serghey Rodin <builder@vestacp.com> - 0.9.7-16
- new color scheme
- i18n support
- idn fix for awstats
- service manager
- web updater

* Mon Jan 14 2013 Serghey Rodin <builder@vestacp.com> - 0.9.7-15
- replaced underlines in rebuild script
- less history to improve listing speed
- proper perms for fcgid in rebuild script
- improved domain validation
- added dash as a valid character for templates

* Tue Jan 08 2013 Serghey Rodin <builder@vestacp.com> - 0.9.7-14
- display full emailbox on edit page
- submenu scroling visabilty
- uppercase arguments in cli help message
- webmail reset function
- more contrast on topmenu
- special info line for dns records and  mail account listing
- number of records on "list records" button
- send database credentials to email
- nonreplaceble logo.png
- added verification for none uniq ftp account

* Mon Dec 24 2012 Serghey Rodin <builder@vestacp.com> - 0.9.7-13
- imroved ssl certificate validation
- added links in return status string
- disabled database charset validation
- renamed css styles to prevent blocking from adblock
- fixed cgi-bin permissions for mod_fcgid
- excluded threads from rrd procs calculation
- added overall monthly statistics
- improved dns expiriation date formating
- navigation menu improvements

* Mon Dec 17 2012 Serghey Rodin <builder@vestacp.com> - 0.9.7-12
- renamed SSL Certificate Authority field
- fixed history log page for users

* Sun Dec 16 2012 Serghey Rodin <builder@vestacp.com> - 0.9.7-11
- disabled ssl check function for startssl certificates

* Sun Dec 16 2012 Serghey Rodin <builder@vestacp.com> - 0.9.7-10
- fixed bug in ip change function
- replaced cancel with back on control buttons

* Sat Dec 01 2012 Serghey Rodin <builder@vestacp.com> - 0.9.7-3
- hotfix for mysql unsuspend function

* Thu Nov 29 2012 Serghey Rodin <builder@vestacp.com> - 0.9.7-2
- hotfix for user valudation function

* Sun Jul 01 2012 Serghey Rodin <builder@vestacp.com> - 0.9.7-1
- New web interface
- Mail api
- Changed vesta user with admin

* Wed Jan 25 2012 Serghey Rodin <builder@vestacp.com> - 0.9.6-3
- Alpha preview of 'login as' function

* Tue Jan 24 2012 Serghey Rodin <builder@vestacp.com> - 0.9.6-2
- Bugfix: nginx include + dublicate ip adresses in listing

* Tue Jan 17 2012 Serghey Rodin <builder@vestacp.com> - 0.9.6-1
- Web interface
- Rebuild functions
- RRD support
- SSL Certificate Authority support
- New return codes
- ServerAlias 8k issue
- Autodocumentation

* Tue Sep 13 2011 Serghey Rodin <builder@vestacp.com> - 0.9.5-2
- small fixes to domain function

* Tue Sep 13 2011 Serghey Rodin <builder@vestacp.com> - 0.9.5-1
- added mpm itk, fcgi, mod_ruid2 support
- changed permissions in bin directory
- new scripts v_del_sys_user v_list_sys_user_childs v_rebuild_dns_domains
- removed backup.pipe
- renamed reseller.conf to child.conf
- complex dns format validator
- added new key for disk usage U_DIR_DISK
- improved rebuild webdomain script
- fixed cron bug
- added backup system
- new user keys FNAME LNAME
- merged key NS1 and NS2 to NS
- moved db configs to conf folder
- yes|no boolean logic in config
- renamed crontab.conf to cron.conf
- renamed web_domains.conf to web.conf
- changed web domains directory to "web"
- fixed v_change_db_password localhost bug
- removed main config from rpm
- improved vesta install scenario

* Tue Jul 05 2011 Serghey Rodin <builder@vestacp.com> - 0.9.4-1
- nginx per domain integration
- removed SSL key and renamed TEMPLATES to WEB_TPL
- added web config rebuild script
- added includes into templates
- code formating by convention
- added error_document support
- v_check_sys_user_password refactoring
- added v_change_sys_ip_status script
- fixed ip interface bugs
- added libidn support
- added skel directory in templates
- updated site templates
- added v_list_sys_user_packages 
- updated v_add_sys_user script (ns1 ns2 args)
- updated documentation

* Tue Jan 04 2011 Serghey Rodin <builder@vestacp.com> - 0.9.3-3
- new rpm spec without updates to code

* Sun Jan 02 2011 Serghey Rodin <builder@vestacp.com> - 0.9.3-2
- many fixes to installer
- added condition to upgrade macro in spec file
- fixed v_add_web_alias_script
- updated disk.pipe

* Tue Dec 28 2010 Serghey Rodin <builder@vestacp.com> - 0.9.3-1
- excluded vesta user from package
- new template storage scheme
- updated funcion increase_user_value()
- added new keys U_CHILDS MAX_CHILDS U_DIR_DISK
- renamed template php_cgi to phpcgi
- added apache_ prefix to tpls
- new logic on keys STATS_AUTH='no' STATS='no'
- updated function get_usr_disk()
- added new script v_upd_sys_user_disk

* Mon Nov 22 2010 Serghey Rodin <builder@vestacp.com> - 0.9.2-4
- fixed update script / rpm %files section

* Mon Nov 22 2010 Serghey Rodin <builder@vestacp.com> - 0.9.2-3
- fixed update script v_upd_sys_vesta

* Mon Nov 22 2010 Serghey Rodin <builder@vestacp.com> - 0.9.2-2
- removed user vesta user from rpm
- fixed %postun script

* Mon Nov 22 2010 Serghey Rodin <builder@vestacp.com> - 0.9.2-1
- added sqlite support into x86_64 repo
- fixed permissions on /var/log/httpd/domains
- many fixes in installer
- fixed empty mask in v_upd_sys_ip script
- added default robots.txt in v_add_web_domain
- new web_domains.conf key NGINX_EXT

* Sat Nov 13 2010 Serghey Rodin <builder@vestacp.com> - 0.9.1-7
- added script v_upd_sys_user_bill
- updated installer 
- replaced v_list_web_domains_proxy with v_list_web_domains_nginx
- fixed rpaf.conf generation
- added nginx templates

* Tue Oct 29 2010 Serghey Rodin <builder@vestacp.com> - 0.9.1-6
- added missing function to db/ip/shared includes

* Tue Oct 26 2010 Serghey Rodin <builder@vestacp.com> - 0.9.1-5
- added U prefix to DISK and BANDWIDTH keys
- new script v_change_sys_ip_name
- added keys NETMASK,INTERFACE,DATE to ip system
- added key IP_OWNED to user system
- improved decrease_db_value() function
- fixed update_user_value() function
- updated installer

* Thu Oct 07 2010 Serghey Rodin <builder@vestacp.com> - 0.9.1-4
- fixed path in php-cgi templates
- increased php_memory_limit up to 32M for wordpress
- updated vsftpd and sudoers configs

* Wed Oct 05 2010 Serghey Rodin <builder@vestacp.com> - 0.9.1-3
- updated db functions

* Wed Oct 04 2010 Serghey Rodin <builder@vestacp.com> - 0.9.1-2
- fixed dns installer + added cron job logging

* Wed Sep 15 2010 Serghey Rodin <builder@vestacp.com> - 0.9.1-1
- created vesta api package
