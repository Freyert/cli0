cat babies.txt | \
python reverso.py | \
curl -XPOST -H 'Content-Type: text/plain; charset=utf-8' --data-binary "@-" 'http://127.0.0.1:5000/reverso'
