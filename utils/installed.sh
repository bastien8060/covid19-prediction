#!/bin/bash
downloaded=`ls ../imports`
installed=`ls ../data`
var1=$downloaded
var2=$installed 

echo $installed
if [[ ! $downloaded == $installed ]]; then
	if [[ $downloaded > $installed ]]; then
		printf "Some countries has been installed but the download file has been removed.\n\n"
		printf "To redownload it, run \n"
		printf "utils/reset.sh\n"
		printf "/init countryname \n\n"
for num in `echo $var1,$var2 | tr -d " "| tr "," "\n " | sort | uniq | tr "\n" " "`
do
        if (`grep -v $num <<< "$var1" >/dev/null 2>&1` || `grep -v $num <<< "$var2" >/dev/null 2>&1`)
        then
                out="$out,$num"
        fi
done

echo $out | sed -e 's/,//'
	fi
	if [[ $installed > $downloaded ]]; then
		printf "Some countries has been downloaded but not installed.\n\n"
		printf "To install it, run \n"
		printf "utils/reset.sh\n"
		printf "/init countryname\n\n"
	    for num in `echo $var1,$var2 | tr -d " "| tr "," "\n " | sort | uniq | tr "\n" " "`
do
        if (`grep -v $num <<< "$var1" >/dev/null 2>&1` || `grep -v $num <<< "$var2" >/dev/null 2>&1`)
        then
                out="$out,$num"
        fi
done

echo $out | sed -e 's/,//'
	fi
fi