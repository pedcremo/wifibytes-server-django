#!/bin/sh
`rm -f /tmp/logHook`
OUTPUT="$(cd ..)"
echo "${OUTPUT}" > /tmp/logHook
OUTPUT="$(git pull)"
echo "${OUTPUT}" > /tmp/logHook >> /tmp/logHook
OUTPUT="$(cd)"
echo "${OUTPUT}" > /tmp/logHook >> /tmp/logHook
OUTPUT="$(supervisorctl restart all)"
echo "${OUTPUT}" > /tmp/logHook >> /tmp/logHook
