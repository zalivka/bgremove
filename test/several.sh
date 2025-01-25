cd test_imgs

rm -f *_processed.png

for file in *; do
    if [[ -f "$file" ]]; then
        output_name="${file%.*}_processed.png"
        echo "curl -X POST -F \"image=@$file\" https://q6o1f66j8465uz-5000.proxy.runpod.net/bg -o \"$output_name\""
        curl -X POST -F "image=@$file" https://q6o1f66j8465uz-5000.proxy.runpod.net/bg -o "$output_name"
    fi
done