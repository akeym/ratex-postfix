#!/bin/bash

hostlist=(smtp1.oregonstate.edu smtp2.oregonstate.edu relay1 relay2 relay3 smtp1 smtp2 smtp3 smtp-brm1 smtp-brm2)
lines=

for h in "${hostlist[@]}"
do
    lines=$lines"${h},`ssh $h '/usr/local/sbin/mq.py'`"$'\n'
done

ssh cactus "echo \"${lines}\" > /var/www/cacti/smtp.csv"
