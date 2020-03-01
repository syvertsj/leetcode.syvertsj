# Read from the file words.txt and output the word frequency list to stdout.

awk '{ 
    for(i = 1; i <= NF; i++) h[$i]++ 
} END {
    for(k in h) print k, h[k]
}' < words.txt | sort -k 2 -nr
