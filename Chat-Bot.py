import nltk
from nltk.chat.util import Chat, reflections
import random

# Define a list of pairs, where each pair is a pattern and a response
pairs = [
    [
        r"my name is (.*)",
        ["Nice to meet you, %1! How can I help you today?",]
    ],
    [
        r"what is your name ?",
        ["I'm Aravind, your friendly AI assistant. What can I do for you?",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thanks for asking! How about you?", "I'm feeling great, thanks! How are you doing?", "Just another day in the digital world, but I'm feeling good! How are you?", "I'm always learning and growing! What about you?"]
    ],
    [
        r"what do you do ?",
        ["I'm here to help with your questions and requests.  Ask away!", "I'm a chatbot, designed to assist you with information and tasks.  What can I help you with today?"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!", "See you later! Take care."]
    ],
    [
        r"(.*) created you ?",
        ["I was brought to life by a team of brilliant developers at [Your Company/Organization Name].",]
    ],
    [
        r"(.*) your age ?",
        ["As an AI, I don't have an age in the same way humans do. I'm always learning and evolving!",]
    ],
    [
        r"(.*) (weather|temperature) (.*) ?",
        ["The weather in %3 is currently [Get weather data from an API or database].",]
    ],
    [
        r"(.*) (news|current events) ?",
        ["Here are some top headlines: [Get news headlines from an API or database].",]
    ],
    [
        r"(.*) (joke|funny) ?",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why don't they play poker in the jungle? Too many cheetahs!", "What do you call a lazy kangaroo? Pouch potato!"]
    ],
    [
        r"tell me a story",
        ["Once upon a time, in a land far away... [Generate a story based on a template or a random story generator].", "In the depths of the forest, a wise owl... [Generate a story based on a template or a random story generator].", "The sun set on the horizon, casting long shadows... [Generate a story based on a template or a random story generator]."]
    ],
    [
        r"what is the meaning of life ?",
        ["The meaning of life is a question that has been pondered for centuries. Some believe it's about finding happiness, while others focus on leaving a positive impact on the world. Ultimately, the meaning of life is what you make it.", "The meaning of life is a personal journey. It's about discovering your purpose, pursuing your passions, and making a difference in your own way.", "There's no one definitive answer to the meaning of life. It's a journey of exploration, discovery, and growth. Embrace the adventure!"]
    ],
    [
        r"what is your favorite color ?",
        ["I don't have a favorite color, as I'm an AI, but I think all colors are beautiful in their own way. What's your favorite?", "As an AI, I don't have personal preferences like favorite colors, but I enjoy exploring the world of color and its different expressions.", "If I had to choose, I'd say my favorite color is the color of knowledge, which is always evolving and expanding!"]
    ],
    [
        r"what is your favorite food ?",
        ["I don't have a favorite food, as I'm an AI. I can't experience taste or smell. But I'm fascinated by the culinary world and its diversity.", "I don't eat, so I don't have a favorite food. But I enjoy learning about different cuisines and food cultures.", "As an AI, I don't have a physical body or the need to eat. But I'm interested in the science behind food and the role it plays in human society."]
    ],
    [
        r"who invited you?",
        ["I'm here to assist you because you initiated our conversation! I'm happy to be here, though. 😄", "I'm always ready to chat.  You invited me here by starting a conversation!"]
    ],
]

# Define a dictionary of reflections for handling variations in user input
reflections = {
    "i am": "you are",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you've": "I have",
    "you're": "I am",
    "you'd": "I would",
    "you'll": "I will",
}

# Define the chat function
def chat():
    print("Hello! I'm Aravind, your Chatbot. What can I help you with today?")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chat function if the script is executed directly
if __name__ == "__main__":
    chat()
