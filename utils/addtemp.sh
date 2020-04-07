#!/bin/bash
echo " "
{
country=$1
toadd=$2
cat imports/$country/data.csv > tmp/$country.csv
lastline=`awk '/./{line=$0} END{print line}' tmp/"$country".csv`
echo $lastline > tmp/addtemp.lastline
date=`awk -F',' '{print $1}' tmp/addtemp.lastline`
rm tmp/addtemp.lastline
dateday="${date: -1}"
day=$(($dateday + 1))
daterest="${date::-1}"
echo $daterest$day,$toadd >> tmp/"$country".csv

./utils/reinit.py $country > /dev/null

} &> /dev/null
