#!/bin/bash

## Strings
str1="a"
str2="b"

# Equality (= and !=) (ASCII comparison)
if [ "$str1" = "$str2" ]; then
  echo "${str1} is equal to ${str2}!"
fi

if [ "$str1" != "$str2" ]; then
  echo "${str1} is not equal to ${str2}!"
fi