#!/bin/sh

`rm -f /tmp/logHook`
OUTPUT="$(whoami)"
echo "${OUTPUT}" > /tmp/logHook
`cd ..`
OUTPUT="$(git pull)"
echo "${OUTPUT}" >> /tmp/logHook
OUTPUT="$(cd && supervisorctl restart all)"
echo "${OUTPUT}" >> /tmp/logHook
