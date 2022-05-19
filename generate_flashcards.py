import json
from wiki_request import wiki_request

# Read data from file:
data = json.load( open( "dict.json" ) )
#for i in data:
    
    #print(i, wiki_request(i))

print(wiki_request('bureau'))