let count=`find . -type f | wc -l`/2 ;
find . -type f -print0 | shuf -z -n $count | xargs -0 -- rm