#!/usr/bin/sh

if ! command -v uv 2>&1 >/dev/null
then
    echo "uv must be installed to run this program"
    exit 1
fi


uv run src/main.py