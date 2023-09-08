#!/bin/bash

# Not Null (-n) or Zero length (-z)
notnull="this is something (not nothing)"
null=""

if [ -n "$notnull" ]; then
  echo "This is not at all null..."
fi

if [ -z "$null" ]; then
  echo "null/zeroooo (length)"
fi
