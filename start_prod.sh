#!/bin/sh
echo "Starting production Server"
gunicorn core.wsgi