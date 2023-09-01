#!/bin/bash

## Arguments reference:
# $# --> number of args that our script was run with
# $0 --> the filename of our script
# $1..$n --> script arguments

# What's our filename?
ourfilename=$0
echo $ourfilename

# How many argumetns was the script called with?
num_arguments=$#
echo $num_arguments

# What are the arguments?
echo "The first three argumnets were ${1}, ${2} and ${3}"