import sys
import os

# Adding the `src` directory to the system path for module imports
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.append(src_path)

from faq_module import find_answer

while True:
    user_question = input("Ask a question: ")
    if user_question.lower() in ["exit", "quit"]:
        break
    response = find_answer(user_question)
    print(f"Chatbot answer: {response}")
