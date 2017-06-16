#!/bin/bash
res=`mysql -h 127.0.0.1 --user=readuser --password=L@uGh1@3 -e "sql1;sql2;"`
echo $res
