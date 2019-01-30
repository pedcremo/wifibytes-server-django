#!/bin/sh
`rm -f /tmp/logHook`
`cd ..`
OUTPUT="$(git pull)"
echo "${OUTPUT}" > /tmp/logHook 
`cd`
OUTPUT="$(supervisorctl restart all)"
echo "${OUTPUT}" >> /tmp/logHook
