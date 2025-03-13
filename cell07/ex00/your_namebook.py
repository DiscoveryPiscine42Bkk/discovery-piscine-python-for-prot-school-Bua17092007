def array_of_name(names_dict):
    full_names = []
    for first_name, last_name in names_dict.items():
        full_names = f"{first_name.capitalize()}"
        full_names.append(full_names)
        return full_names
if __name__ == " __main__" :
    names = {
        "john": "doe",
        "jane": "smith",
        "alice": "johnson"
    }
    print(array_of_names(names))