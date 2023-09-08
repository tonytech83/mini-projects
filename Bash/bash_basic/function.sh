#!/bin/bash

NUM_REQUIRED_ARGS=2
num_args=$#

# Do we have at least tow arguments?
if [ $num_args -lt $NUM_REQUIRED_ARGS ]; then
  echo "Not enough argumetns. Call this script with ${0} <name> <number>"
  exit 1
fi

# Set variables, using argumetns
name=$1
number=$2
echo "Your first two arguments were:$1 $2"

# for loop; iteration, string interpolation
echo "You ran this script with ${num_args} arguments. Here they are:"
for arg in "$@"; do
  echo "$arg"
done

# define a function (first way, without special word /function/)"
spaced() {
  # parameters are not namd, they are positional
  echo
  echo "###################"
  echo "$1"
  echo "###################"
  echo
}

# define a function
function javatest() {
  # test and conditionals
  if [[ $number -eq 99 ]]; then
    spaced "You win! You guessed the secret number! It's amaaazzziiinnnggg!!!"
  elif [[ $number -lt 10 ]]; then
    spaced "You'are a courageus one. I like that about you. Unfortunately, you must still DIE!"

    echo "Hie ${name}, to avert a horrible death, please enter the password:"
    read password

    if [[ "$password" != "Java" ]]; then
      spaced "Well, at least you'are not a Java Programming sympathizer. You can go now."
    else
      spaced "DIIIEEE! Actually, nevermind. Writing Java is enough of a hellosh punishment. You are free to leave. Take a biscuit on the way out."
    fi
  fi
}

# call function
javatest $number
exit 0
