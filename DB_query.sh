#!/bin/bash
res=`mysql -h 127.0.0.1 --user=username --password=password -e "sql1;sql2;"`
echo $res
