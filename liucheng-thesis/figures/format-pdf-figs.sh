#!/bin/bash

Files=`find ./*.pdf -mmin -30`
for f in $Files
do
    ./mycrop $f $f
done

