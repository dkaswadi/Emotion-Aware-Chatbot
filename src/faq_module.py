import json
from difflib import get_close_matches

# Load FAQ data from JSON file
def load_faq_data(file_path="src/faq.json"):
    with open(file_path, 'r') as file:
        return json.load(file)

faq_data = load_faq_data()

if __name__ == "__main__":
    print(faq_data)  # This should print the loaded JSON data

def find_answer(question):
    question = question.lower()  # Normalize user input to lowercase

    # Normalize keys to lowercase and check for exact matches first
    normalized_faq = {key.lower(): value for key, value in faq_data.items()}
    
    if question in normalized_faq:
        return normalized_faq[question]

    # Use get_close_matches to find similar questions if no exact match is found
    close_match = get_close_matches(question, normalized_faq.keys(), n=1, cutoff=0.4)
    if close_match:
        return normalized_faq[close_match[0]]
    else:
        return "I'm not sure about that, but I can try to help with something else!"
