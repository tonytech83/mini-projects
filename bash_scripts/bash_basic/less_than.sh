n#!/bin/bash
# testing and control flow with if, [ and [[, and/or

NUM_REQUIRED_ARGS=2

#Do we have at least two arguments? Using -lt (lessthen) to compare.
if [[ $# -lt NUM_REQUIRED_ARGS ]]; then
  echo "Not enough arguments. Call this script with ./{$0} <name><number>"
fi
