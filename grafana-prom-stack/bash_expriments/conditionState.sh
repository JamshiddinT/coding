#!/bin/bash

if [ $1 -gt 100 ]
then
    echo Hey that\'s a large number.
    if (( $1 % 2 == 0 ))
    then
        echo And is also an even number.
    fi
    
    pwd
fi 

date