from ast import Delete
from unicodedata import name


actor = {
    "first_name": "Alex",
    "last_name": "King",
    "country": "USA",
    "movies": [
        {
            "name": "Hercules",
            "date": "2001"
        },
            {
            "name": "Rembo",
            "date": "2010"
        },
            {
            "name": "Rocky",
            "date": "1996"
        },
    ],
    "money": {
        "salary": "20000",
        "currency": "euro"
    }
}

# Work with 'actor' dictionary

# Print actor first and last name
print(actor["first_name"],actor["last_name"])
# Print the number of movies the actor appeared in
print(len(actor["movies"]))
# Print is key 'hobby' exists in the dictionary
if "hobby" in actor:
    print("Yes")
else: print("No")
# Delete 'country' key from the dictionary. Print result
actor.pop("country")
print(actor)
# Add new key 'sex' and set as 'male'. Print result
actor["sex"]="male"
print(actor)
# Clear 'actor' dictionary. Print result
# actor.clear()
# print(actor)
# # Delete 'actor' dictionary. Print result.
# del actor
# print(actor)

print(actor["money"]["salary"])