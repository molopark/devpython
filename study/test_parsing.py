import json
from io import StringIO

io = StringIO('{"title":"Book1", "ISBN":"12345", "author":[{"name":"author1", "age":30}, {"name":"author2", "age":25}]}')
json_data = json.load(io)

print(json_data['title'])
print(json_data['ISBN'])

for author in json_data['author']:
    print(author['name'])
    print(author['age'])
