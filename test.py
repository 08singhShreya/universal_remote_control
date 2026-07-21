fruits = ["Apple", "Banana", "Mango", "Papaya", "Litchi","Watermelon", "Muskmelon"]
summer_fruits = ["Mango", "Litchi","Watermelon", "Muskmelon"]

for fruit in fruits:
    if fruit in summer_fruits:
        print(f"Summer_fruits are: {fruit}")
    else:
        print(f"{fruit} is not summer fruit.") 


record = {
    "name": "Shreya",
    "age": 26,
    "hobby": "xyz",
    "sex": "Female",
    "is_married": False
}

print(dir(record))

user = {"username": "raj123", "email": "raj@test.com", "active": True}
print(user)
print(type(user))
print(user["email"])

response = {"status": "success", "data": {"id": 5, "score": 88}}
print(response)
print(type(response))
print(response["data"]["score"])

def get_weather():
    return {"city": "Bhopal", "temp_c": 34, "condition": "Sunny"}

weather = get_weather()

print(weather)
print(type(weather))
print(weather["temp_c"])

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

my_book = Book("Dune", "Frank Herbert", 400)
print(my_book)
print(type(my_book))
print(my_book.author)
print(dir(my_book))

data = [{"name": "Amit", "score": 70}, {"name": "Priya", "score": 95}]
print(type(data))
print(data)
for person in data:
    print(f"Name: {person['name']}, | Score: {person['score']}")
    


api_response = {
    "user": {
        "id": 12,
        "profile": {
            "city": "Delhi",
            "age": 30
        }
    }
}

print(type(api_response))
print(api_response)
print(api_response["user"]["profile"]["city"])