#!/bin/sh

cd ..
git pull
cd
supervisorctl restart all
