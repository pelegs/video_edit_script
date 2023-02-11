#!/bin/bash
A="ask.mp4" 
B="ans.mp4" 
LST="0:00:30 0:02:15 0:03:25" 
s="0" 
c=0 
for t in $LST;
do 
  INP+=("-ss" "$s" "-to" "$t" "-i") 
  if (( ($c % 2) == 0 )); then 
    INP+=("$A") 
  else 
    INP+=("$B") 
  fi 
  CON+="[${c}:v][${c}:a]" 
  s=$t 
  ((c++)) 
done 
echo "${INP[@]}"
