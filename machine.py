import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Example dataset
data = {
    'Question': ['How are you?', 'Hello', "What's your name?", 'Tell me a joke', 'Goodbye','hallo','hey'],
    'Label': ['greeting', 'greeting', 'personal_info', 'entertainment', 'goodbye','greeting','greeting']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Preprocess: Vectorize the questions
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Question'])

# Split the data into training and testing sets
y = df['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Test the model and print accuracy
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%')

# Chatbot response function
def ml_chatbot_response(user_input):
    user_input_vec = vectorizer.transform([user_input])  # Vectorize the input
    prediction = model.predict(user_input_vec)[0]  # Predict the label

    # Responses based on predicted intent
    if prediction == 'greeting':
        return "Hello! How can I help you today?"
    elif prediction == 'personal_info':
        return "I am a simple chatbot created to assist you."
    elif prediction == 'entertainment':
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif prediction == 'goodbye':
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."

# Chat loop to interact with the chatbot
def start_ml_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = ml_chatbot_response(user_input)
        print("Chatbot:", response)

# Start the machine learning chatbot
start_ml_chatbot()
