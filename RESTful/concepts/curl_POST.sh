#TEST for POST 
echo '{"text": "Hello **world**!"}' | curl -X POST -d @- https://api.github.com/markdown
