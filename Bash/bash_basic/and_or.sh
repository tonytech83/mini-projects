#!/bin/bash

## helpers
# && --> AND
# || --> OR

## in terminal
echo "hi." || echo "This won't happen."
$(ls nonexistenfile) || echo "This happen if the first thing fails"
echo $(pwd) && echo "This ALSO happens!"