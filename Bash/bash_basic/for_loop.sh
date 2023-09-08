#!/bin/bash

num_args=$#

# For loops
echo "You ran this program with ${num_args} arguments. Here they are:"
for arg in "$@"; do
  echo "$arg"
done
