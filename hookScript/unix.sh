#!/bin/bash

#`/bin/rm -f /tmp/logHook`
OUTPUT="$(/usr/bin/whoami)"
echo "${OUTPUT}" > /tmp/logHook
`cd ..`
OUTPUT="$(/usr/bin/git pull)"
echo "${OUTPUT}" >> /tmp/logHook
`cd`
OUTPUT="$(/usr/bin/supervisorctl restart all &)"
#echo "${OUTPUT}" >> /tmp/logHook
