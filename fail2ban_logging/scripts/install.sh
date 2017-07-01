#! 

if [ ! -d /usr/local/lib/python2.7/dist-packages/mysqlutils ];
then
    echo "Install /usr/local/lib/python2.7/dist-packages/mysqlutils using pip install first!"
    exit
fi

if [ ! -d /etc/f2b_attack_log ];
then
    mkdir -p /etc/f2b_attack_log
fi

if [ ! -f /etc/f2b_attack_log/config.ini ];
then
    cp config.sample.ini /etc/f2b_attack_log/config.ini
fi

cp f2b_attack_log.py  /usr/bin/f2b_attack_log.py
