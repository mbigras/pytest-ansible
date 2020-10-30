#!/usr/bin/env bash
# Start uWSGI server as the nobody user.

PORT=${PORT:-3000}

exec gosu nobody uwsgi --socket=0.0.0.0:$PORT --wsgi=app:app --protocol=http --master
