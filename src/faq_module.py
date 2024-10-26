import json
from difflib import get_close_matches

# Load FAQ data from JSON
def load_faq_data(file_path="src/faq.json"):
    with open(file_path, 'r') as file:
        return json.load(file)

faq_data = load_faq_data()

def find_answer(question):
    # Check for exact matches first
    if question in faq_data:
        return faq_data[question]

    # Use get_close_matches to find similar questions if no exact match is found
    close_match = get_close_matches(question, faq_data.keys(), n=1, cutoff=0.6)
    if close_match:
        return faq_data[close_match[0]]
    else:
        return "I'm not sure about that, but I can try to help with something else!"

