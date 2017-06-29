#!/bin/bash
#Remove html tags
#Remove chars starting from & and ending with ;
#Remove linebreaks
#Remove | , "" '' - 


sed -e 's/[\t\r",\?\.'\''\\A-Za-z0-9<>\&\_\!\@\#\=\/\+\-\)\(\:\;]//g' $1  \
					 | sed 's/\xe0\xa5\xa5//g' \
					 | sed 's/\xe0\xa5\xa6//g' \
					 | sed 's/\xe0\xa5\xa7//g' \
					 | sed 's/\xe0\xa5\xa8//g' \
					 | sed 's/\xe0\xa5\xa9//g' \
					 | sed 's/\xe0\xa5\xaa//g' \
					 | sed 's/\xe0\xa5\xab//g' \
					 | sed 's/\xe0\xa5\xac//g' \
					 | sed 's/\xe0\xa5\xad//g' \
					 | sed 's/\xe0\xa5\xae//g' \
					 | sed 's/\xe0\xa5\xaf//g' \
					 | sed -e 's/-//g' | sed -e 's/  */ /g' | sed 's/   *//g'> $2
 echo "output saved to $2"