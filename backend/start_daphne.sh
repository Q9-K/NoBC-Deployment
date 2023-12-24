#!/bin/bash
supervisord -c /code/supervisord.conf
supervisord start daphne