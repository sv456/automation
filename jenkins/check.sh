#!/bin/bash
for i in `cat /tmp/sand.txt`
do
ssh -q mpdevops@"$i" << EOF
        bash /app/home/mpdevops/sand.sh
EOF
done
