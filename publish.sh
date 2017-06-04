#!/usr/bin/env bash
source ./env/bin/activate
make html && make publish
cd output
git add --all
git commit -m 'content update'
git push origin HEAD:master