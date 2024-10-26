from faq_module import find_answer

while True:
    user_question = input("Ask a question: ")
    if user_question.lower() in ["exit", "quit"]:
        break
    response = find_answer(user_question)
    print(f"Chatbot answer: {response}")

