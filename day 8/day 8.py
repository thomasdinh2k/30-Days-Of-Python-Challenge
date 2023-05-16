dog_breeds = {
  "name": "Sammy",
  "color": "brown",
  "breed": "Golden Retriever",
  "legs": 4,
  "age": 2,

  "name": "Lola",
  "color": "black",
  "breed": "German Shepherd",
  "legs": 4,
  "age": 3,

  "name": "Max",
  "color": "white",
  "breed": "Poodle",
  "legs": 4,
  "age": 1,

  "name": "Charlie",
  "color": "blue",
  "breed": "Husky",
  "legs": 4,
  "age": 5,

  "name": "Bella",
  "color": "red",
  "breed": "Labrador Retriever",
  "legs": 4,
  "age": 6,

  "name": "Rocky",
  "color": "yellow",
  "breed": "Boxer",
  "legs": 4,
  "age": 7,

  "name": "Duke",
  "color": "grey",
  "breed": "Dachshund",
  "legs": 4,
  "age": 4,

  "name": "Princess",
  "color": "white and brown",
  "breed": "Beagle",
  "legs": 4,
  "age": 8,

  "name": "Bailey",
  "color": "black and white",
  "breed": "Yorkshire Terrier",
  "legs": 4,
  "age": 9,

  "name": "Cooper",
  "color": "brown and white",
  "breed": "Chihuahua",
  "legs": 4,
  "age": 10,

  "name": "Mia",
  "color": "black and tan",
  "breed": "Jack Russell Terrier",
  "legs": 4,
  "age": 11,

  "name": "Buddy",
  "color": "white and black",
  "breed": "Pug",
  "legs": 4,
  "age": 12,

  "name": "Rocky",
  "color": "brown and white",
  "breed": "French Bulldog",
  "legs": 4,
  "age": 13,
}

student = {
  "first_name": "Jane",
  "last_name": "Doe",
  "gender": "female",
  "age": 23,
  "marital_status": "single",
  "skills": ["writing", "reading", "history"],
  "country": "United States",
  "city": "Los Angeles",
  "address": "456 Elm Street"
}

print(len(student))
student["skills"] += ["biology", "chemistry"]   # Short-cut for append-method
print(student)

print(student.keys())
print(student.values())
print(student.items())

student.pop("first_name")
print(student)
del student
print(student)