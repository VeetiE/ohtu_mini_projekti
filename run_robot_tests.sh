#!/bin/bash

# käynnistetään Flask-palvelin taustalle
poetry run python3 src/index.py &

# suoritetaan testit
poetry run robot src/

status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5000)

exit $status
