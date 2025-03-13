def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error: Name must be string.")
    else:
        print(f"Welcome, {name}!")
        greetings()
        greetings("john")
        greetings(123)