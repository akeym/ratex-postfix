#!/usr/bin/env python
import os, os.path
deferred=0
active=0
active=len(os.listdir('/var/spool/postfix/active'))
for msgid in os.listdir('/var/spool/postfix/deferred'):
   deferred += len(os.listdir(os.path.join('/var/spool/postfix/deferred',msgid)))
print "{0},{1}".format(active,deferred)

