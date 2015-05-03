#!/bin/sh

if ! hash pip 2>/dev/null; then
  echo "Error: You need to install 'pip' (apt-get install python-pip)"
  exit 1
fi

if ! hash bower 2>/dev/null; then
  echo "Error: You need to install 'bower' (npm install -g bower)"
  exit 1
fi

pip install -r requirements.txt

pushd web
bower install
popd

if ! hash wkhtmltopdf 2>/dev/null; then
  echo "Warning: You need to install 'wkhtmltopdf' (apt-get install wkhtmltopdf)"
fi

if ! hash lpr 2>/dev/null; then
  echo "Warning: Can't find command 'lpr' - check your CUPS installation"
fi

echo "Run ./runserver.py to start"
