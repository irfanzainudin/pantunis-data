#!/usr/bin/bash

# Courtesy of Razin Izzuddin
 
# Put ur cookie here
COOKIE="d1689c1eafe4de4cb447bc9277be6e78=c66efd39c11d0a546cf2e8e21cc61f6b"
 
function download_page {
    PAGE=$1
    FILENAME=$2
    curl "https://malaycivilization.com.my/items/show/$PAGE" \
      -H 'authority: malaycivilization.com.my' \
      -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
      -H 'accept-language: en-US,en;q=0.9' \
      -H 'cache-control: no-cache' \
      -H "cookie: $COOKIE" \
      -H 'pragma: no-cache' \
      -H 'referer: https://malaycivilization.com.my/search' \
      -H 'sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"' \
      -H 'sec-ch-ua-mobile: ?0' \
      -H 'sec-ch-ua-platform: "Windows"' \
      -H 'sec-fetch-dest: document' \
      -H 'sec-fetch-mode: navigate' \
      -H 'sec-fetch-site: same-origin' \
      -H 'sec-fetch-user: ?1' \
      -H 'upgrade-insecure-requests: 1' \
      -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36' \
      --compressed > "$FILENAME"
}
 
# Change number here
for i in {136484..136507}
do
    download_page "$i" "136484-136507/$i.txt"
done