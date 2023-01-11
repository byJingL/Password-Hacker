# ------------------ JSON Module -------------- #
import json
movie_dict = {
  "movies": [
    {
      "title": "Inception",
      "director": "Christopher Nolan",
      "year": 2010
    },
    {
      "title": "The Lord of the Rings: The Fellowship of the Ring",
      "director": "Peter Jackson",
      "year": 2001
    },
  ]
}

# Encoding to JSON
with open('Password-Hacker/pre-topics/data.json', 'w') as data_file:
    json.dump(movie_dict, data_file, indent=4)
    
# Decoding JSON
with open('Password-Hacker/pre-topics/data.json', 'r') as data_file:
    movie_data = json.load(data_file)
    print(type(movie_data))
    print(movie_data == movie_dict)

# Not with file
json_str = json.dumps(movie_dict, indent=4)
print(type(json_str))

another_data = json.loads(json_str)
print(type(another_data))

