def exposure_therapy_conversation(user_level):
    # Dictionary of exposure levels with corresponding supportive scripts
    exposure_levels = {
        1: "Imagine you're meeting a new friend in a small group. What would you say to introduce yourself?",
        2: "Now, imagine you’re meeting someone new one-on-one. How would you start the conversation?",
        3: "Let’s say you’re at lunch, and you want to sit next to someone new. What could you say to join them?",
        4: "Imagine yourself introducing two friends to each other. What would you say?"
    }

    # Validate user input and gradually increase exposure level
    if user_level in exposure_levels:
        question = exposure_levels[user_level]
        print(f"Chatbot: {question}")
        # Example of encouraging feedback
        response = input("User: ")  # Simulated input from the user
        print(f"Chatbot: That’s great! You’re doing well.")
        
        # Ask if the user feels ready to move on to the next level
        if user_level < len(exposure_levels):
            next_level = input("Chatbot: Would you like to try the next level? (yes/no): ").lower()
            if next_level == "yes":
                exposure_therapy_conversation(user_level + 1)
            else:
                print("Chatbot: That’s okay. Let’s stop here for now. You did great!")
        else:
            print("Chatbot: You’ve completed all levels! Well done!")
    else:
        print("Chatbot: Let’s start with a small step. Imagine you're meeting a new friend in a small group.")

