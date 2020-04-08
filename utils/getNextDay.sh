country=$1
round=$2
cat imports/$country/data.csv > tmp/$country.csv
lastline=`awk '/./{line=$0} END{print line}' tmp/"$country".csv`
echo $lastline > tmp/addtemp.lastline
date=`awk -F',' '{print $1}' tmp/addtemp.lastline`
rm tmp/addtemp.lastline
dateday="${date: -1}"
day=$(($dateday + $round))
daterest="${date::-1}"
printf $daterest$day
