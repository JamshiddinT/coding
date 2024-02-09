#!/bin/bash
# elif statements

echo "what's your age? " 
read num1
echo "will you promise not to drink at the party? " 
read num2
if [[ $num1 -ge 18 && $num2 == 'yes' ]]
then
    echo You may go to the party.
elif [[ $num1 -lt 18 && $num2 == 'yes' ]]
then
    echo You may go to the party but be back before midnight.
else
    echo You may not go to the party.
fi