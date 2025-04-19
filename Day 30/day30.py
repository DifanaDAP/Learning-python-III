# day 30 : final projct - mini AI chatbot using nlp

# required libraries:
# pip install scikit-learn nltk joblib

import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# download requried nltk data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# sample training data
training_data = [
    ("Hello", "hi there! how can i help you?"),
    ("hi", "Hello! what can i do for you?"),
    ("How are you?", "i'm just a bot, but i'm doing fine"),
    ("what is your name?", "I'm a simple AI Chatbot"),
    ("bye", "Goodbye! Have a great day!"),
    ("thank you", "you are welcome"),
    ("thanks", "No problem! happy to help"),
    ("can you help me", "of course! ask me anything"),
    ("what can you do", "i can chat with you and help answer basic question")
]

# separate input and output
X_train = [item[0] for item in training_data]
y_train = [item[1] for item in training_data]

# create and train the model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# save model
joblib.dump(model, "chatbot_model.joblib")

# load model
chatbot = joblib.load("chatbot_model.joblib")

# chatbot interaction loop
def chat():
    print("AI Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You :")
        if user_input.lower() == 'exit':
            print("chatbot: Goodbye")
            break
        response = chatbot.predict([user_input])[0]
        print(f"Chatbot: {response}")

if __name__ == '__main__':
    chat()