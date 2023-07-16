
userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

read -p "Plase, paste url: " url
curl -A "$userAgent" "$url" | grep -o '<iframe[^>]*src=[^>]*>' | sed -e 's/<iframe[^"]*src="\([^"]*\)"[^>]*>/\1/g'

