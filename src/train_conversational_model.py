from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

# Load a pre-trained DialoGPT model
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Prepare your conversational data (in this example, using dialogue pairs in a list)
conversations = [
    {"prompt": "Hello!", "response": "Hi there! How can I help you?"},
    {"prompt": "What's the weather like today?", "response": "It's sunny and bright today!"}
    # Add more dialogue pairs here
]

# Preprocess and tokenize your dialogue data
def preprocess_conversations(conversations):
    inputs = []
    labels = []

    for conv in conversations:
        encoded_prompt = tokenizer.encode(conv['prompt'] + tokenizer.eos_token, return_tensors='pt')
        encoded_response = tokenizer.encode(conv['response'] + tokenizer.eos_token, return_tensors='pt')
        inputs.append(encoded_prompt)
        labels.append(encoded_response)

    return inputs, labels

inputs, labels = preprocess_conversations(conversations)

# Define training arguments and trainer
training_args = TrainingArguments(
    output_dir="./chatbot_model",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=10,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=inputs,
)

# Train the conversational model
trainer.train()

