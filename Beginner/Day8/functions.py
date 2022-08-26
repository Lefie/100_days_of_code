#function with inputs

def greet(name):
    print(f"hello {name}")


greet("Lemon")

#keyword argument 
def greeting2(location = "New York", name = "Lemon"):
    print(f"Hi {name}. You are from {location}")

greeting2("China")
