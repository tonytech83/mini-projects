#!/bin/bash

clear
echo ""
echo ""
echo "Let's figure out which OS / Distro you are running."
echo ""
echo ""
echo "    From some basic information on your system, you appear to be running: "
echo "        --  OS Name:              " $(lsb_release -i | cut -d: -f2 | awk '{$1=$1};1')
echo "        --  Description:  " $(lsb_release -d | cut -d: -f2 | awk '{$1=$1};1')
echo "        --  OS Versio:            " $(lsb_release -r | cut -d: -f2 | awk '{$1=$1};1')
echo "        --  Code Name:            " $(lsb_release -c | cut -d: -f2 | awk '{$1=$1};1')
echo ""
echo "------------------------------------------------------"
echo ""