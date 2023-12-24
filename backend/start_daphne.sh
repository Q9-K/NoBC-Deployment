#!/bin/bash
supervisord -c /code/supervisord.conf
supervisorctl start daphne
tail -f /dev/null