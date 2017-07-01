# Automated banlist tool for Fail2Ban
An automated backend-tool to register and deploy ip-addesses for Fail2Ban 

## Requiremnts
* Install python-mysql connector: http://dev.mysql.com/doc/connector-python/en/connector-python-installation.html
* Installe mysqlutils packages from /mailx/develment/pyton_devel using pip

## Installation
* run install.sh
* Provide mysql-connection data in /etc/f2b_attack_log/config.ini 

## Set up Fail2Ban
* Edit actions in /etc/fail2ban/actions.d/iptables-multiport.conf