#!/bin/bash

## Itegers
int1=1
int2=7

# equal, not equal (old style)
if [ $int1 -eq $int2 ]; then
  echo "${int1} is equal to ${int2}."
fi
if [ $int1 -ne $int2 ]; then
  echo "${int1} is NOT equal to ${int2}."
fi

# greater than, less than +equal (old style)
# -gt, -lt, -ge, -le
if [ $int1 -gt $int2 ]; then
  echo "${int1} is equal to ${int2}."
fi
if [ $str1 -le $int2 ]; then
  echo "${int1} is less than or equal to ${int2}."
fi

## NEW STYLE
# (())
# ==    Is Equal To
# !=    Is Not Equal To
# <     Is Less Than
# <=    Is Less Than Or Equal To
# >     Is Greater Than
# >=    Is Greater Than Or Equal To

# String comparison operators can be used with double parentheses
if (( $int1 == $int2 )); then
  echo "${int1} is equal to ${int2}."
fi