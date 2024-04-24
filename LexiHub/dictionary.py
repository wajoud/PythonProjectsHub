import json
from difflib import get_close_matches

def load_data():
    """Load data from a JSON file only when needed."""
    try:
        with open("./data.json") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def translate(word, data):
    """Translate a word using a provided data dictionary."""
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return suggest_alternative(word, data)

def suggest_alternative(word, data):
    """Suggest closest match for unrecognized words."""
    matches = get_close_matches(word, data.keys())
    if matches:
        response = input(f"Did you mean {matches[0]} instead? [Y/n]: ")
        if response.lower() in ('y', 'yes', ''):
            return data[matches[0]]
        elif response.lower() in ('n', 'no'):
            return "No match found. Please check your input."
        else:
            return "Invalid input. Please just enter Y or N."
    else:
        return "The word doesn't exist. Please double-check it."

def main():
    data = load_data()
    if not data:
        print("Data file not found or is corrupt.")
        return

    word = input("Enter the word you want to search: ")
    output = translate(word, data)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

if __name__ == "__main__":
    main()
