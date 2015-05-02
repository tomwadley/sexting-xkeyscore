#!/bin/sh

pip install -r requirements.txt

pushd web
bower install
popd
