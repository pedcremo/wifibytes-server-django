#!/bin/bash
# FULL PATH IS REQUIRED BECAUSE WE NO HAVE VARIABLE CONTEXT PATH WHEN WE CALL THE SCRIPT
OUTPUT="$(/usr/bin/whoami)"
echo "${OUTPUT}" > /tmp/logHook
`cd ..`
OUTPUT="$(/usr/bin/git pull)"
echo "${OUTPUT}" >> /tmp/logHook
`cd`
OUTPUT="$(/usr/bin/supervisorctl restart all &)"
#echo "${OUTPUT}" >> /tmp/logHook
