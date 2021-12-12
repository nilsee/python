#! /usr/bin/python 
import sys
import socket
from mysql.connector import MySQLConnection, Error
from mysqlutils.python_mysql_dbconfig import read_db_config

#
# http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
#
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    return True

config_file = '/etc/f2b_attack_log/config.ini'

#
# http://www.mysqltutorial.org/calling-mysql-stored-procedures-python/
#
def get_banlist():
    try:
        db_config = read_db_config(config_file)
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute('select * from f2b_v_banlist')
        row = cursor.fetchone()
        while row is not None:
            print(row[0])
            row = cursor.fetchone()
    except Error as e:
        sys.stderr.write(e)
    finally:
        cursor.close()
        conn.close()
         
def add_attacker(host, address):
    try:
        db_config = read_db_config(config_file)
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        args = [host, address]
        result_args = cursor.callproc('f2b_sp_log_attack', args)
        conn.commit()
    except Error as e:
        sys.stderr.write(e)
    finally:
        cursor.close()
        conn.close()

def add_to_whitelist(address):
    try:
        db_config = read_db_config(config_file)
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        args = [address]
        result_args = cursor.callproc('f2b_sp_add_to_whitelist', args)
        conn.commit()
    except Error as e:
        sys.stderr.write(e)
    finally:
        cursor.close()
        conn.close()

def add_to_blacklist(address):
    try:
        db_config = read_db_config(config_file) 
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        args = [address]
        result_args = cursor.callproc('f2b_sp_add_to_blacklist', args)
        conn.commit()
    except Error as e:
        sys.stderr.write(e)
    finally:
        cursor.close()
        conn.close()

def add_hostname(hostname):
    try:
        db_config = read_db_config(config_file) 
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        args = [hostnamm]
        result_args = cursor.callproc('f2b_sp_add_host', args)
        conn.commit()
    except Error as e:
        sys.stderr.write(e)
    finally:
        cursor.close()
        conn.close()

def usage():
    print ( "%s [attacker ip|whitelist ip|blacklist ip|banlist|addhost hostname]" % sys.argv[0] )

if __name__ == '__main__':

    if len(sys.argv) == 2 and sys.argv[1] == 'banlist':
        get_banlist()
        exit(0)
        
    if len(sys.argv) != 3:
        usage()
        exit(-1)

    if sys.argv[1] == 'addhost':
        add_hostname(sys.argv[2])
        exit(0)
        
    if not is_valid_ipv4_address(sys.argv[2]):
        usage()
        exit(-1)
        
    if sys.argv[1] == 'attacker':
        add_attacker('mail1.nils-is.me', sys.argv[2])
    elif sys.argv[1] == 'whitelist':
        add_to_whitelist(sys.argv[2])
    elif sys.argv[1] == 'blacklist':
        add_to_blacklist(sys.argv[2])
    else:            
        usage()
        exit(-1)

    exit(0)
