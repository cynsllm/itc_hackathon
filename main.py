"""
This is the template server side for ChatBot
"""

from bottle import route, run, template, static_file, request
import json
import random
import requests





drink_list = ["water", "drink", "liter"]
food_list = ["eat", "food"]
weight_list = ["weight", "pound", "weigh"]
weather_list = ["weather", "forecast", "temp", "degree", "celcius", "sun", "cloud", "rain", "sky", "hot", "cold"]
city_list = ["paris", "london", "tel aviv", "new york", "jerusalem", ""]
end_conversation_list = ["bye", "see you", "to leave", "to go"]

can_list = ["can you", "possible", "can I"]

def drink():
    answer_list = ["I drunk 12L today!"]
    return answer_list

def food():
    answer_list = ["I ate 2 kilos of soja and 1 kilo of corn."]
    return answer_list

def weight():
    answer_list = ["I weigh 957 kilos."]
    return answer_list

def do():
    answer_list = ["I walked 10km.", "I played outside with my friends!"]
    return random.choice(answer_list)


def start_conversation():
    answer_list = ["Hello dear!", "Hi my friend!", "What's up!", "Hey! I'm happy to see you again!", "How are you today ?", "Hey bro!"]
    return random.choice(answer_list)

def end_conversation():
    answer_list = ["Do you really want to end the conversation?", "I hope you'll come and talk soon!", "No problem, see you next time!", "Okay, we'll continue our conversation later!"]
    return random.choice(answer_list)

def how_are_you():
    answer_list = ["I'm good thank you!", "I am a bit stressed"]
    return random.choice(answer_list)


def can_you():
    answer_list = ["Oh no...", "So boring...", "Don't make me waist my time"]
    return random.choice(answer_list)

def error_message():
    answer_list = ["Sorry, I can't help you.", "Sorry, I think I cannot help you.", "Sorry, ask another robot who may help you!"]
    return random.choice(answer_list)

def not_english():
    answer_list = ["What is that language?", "Sorry, I speak english only!", "Go talk to another robot which speaks your weird language!"]
    return random.choice(answer_list)


def bot_message(input):
    input = input.lower()
    if input.startswith("how are"):
        return how_are_you()
    elif any(elem in input for elem in drink_list):
        return drink()
    elif any(elem in input for elem in food_list):
        return food()
    elif any(elem in input for elem in weight_list):
        return weight()
    elif "did you do" in input:
        return do()
    elif any(elem in input for elem in end_conversation_list):
        return end_conversation()
    elif any(elem in input for elem in can_list):
        return can_you()
    else:
        return error_message()




@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    user_message = bot_message(user_message)
    return json.dumps({"msg": user_message})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()

