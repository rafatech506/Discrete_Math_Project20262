for file in ./tests/*; do
    echo "$file"
    python main.py < $file
    if [ $? -ne 0 ]; then
        echo "Something wrong"
        exit 33
    fi
done
echo "Ended succesfully"