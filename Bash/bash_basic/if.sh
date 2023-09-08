#!/bin/bash

NAME=$1
GREETING="Hi there"
HAT_TIP="*tip of the hat*"
HEAD_SHAKE="*slow head shake*"

if [ "$NAME" = "Anton" ]; then
    echo $GREETING
elif [ "$NAME" = "Steve" ]; then
    echo $HAT_TIP
else
    echo $HEAD_SHAKE
fi
