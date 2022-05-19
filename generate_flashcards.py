import json
from wiki_request import wiki_request

# Read data from file:
data = json.load( open( "dict.json" ) )

for i in data:

    with open('output.html', 'a') as f:
        s = str(i) + " " + str(wiki_request(i)) + "\n"
        f.write(s)




