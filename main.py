"""
This is the template server side for ChatBot
"""

from bottle import route, run, template, static_file, request
import json
import random
import requests





<<<<<<< HEAD
link_list = {
    "skirt": "https://www.asos.com/yellow-skirt", "dress": "https://www.asos.com/pink-dress", "jean":"https://www.asos.com/blue-jeans", "pant":"https://www.asos.com/black-pant", "jacket":"https://www.asos.com/leather-jacket", "accessory":"https://www.asos.com/soft-hat", "shirt":"https://www.asos.com/white-shirt", "coat":"https://www.asos.com/red-coat", "sweat":"https://www.asos.com/grey-sweat", "shoe":"https://www.asos.com/leather-shoes", "sneaker":"https://www.asos.com/nike-running",
    "clothe":"https://www.asos.com", "sock":"https://www.asos.com/multicolor-socks", "boxer":"https://www.asos.com/men-boxers", "suit":"https://www.asos.com/blue-suit", "blouse":"https://www.asos.com/oversized-blouse", "tie":"https://www.asos.com/red-tie", "top":"https://www.asos.com/night-tops", "trouser":"https://www.asos.com/black-trousers", "short":"https://www.asos.com/sexy-short", "glove":"https://www.asos.com/leather-gloves", "jumper":"https://www.asos.com/white-jumper",
    "swim":"https://www.asos.com/swimsuits", "bra":"https://www.asos.com/lingerie", "boot":"leather-boots"
}
like_list = ["yes", "wow", "beautiful", "amazing", "like", "nice", "cool", "great", "good", "much", "yeah", "yep", "love"]
dislike_list = ["no", "not", "aweful", "horrible", "bad", "nope", "dislike", "hate"]
curse_list = ["fuck", "bitch", "shit", "piss", "dick", "asshole", "bastard", "damn"]
=======
drink_list = ["water", "drink", "liter"]
food_list = ["eat", "food"]
weight_list = ["weight", "pound", "weigh"]
>>>>>>> 96b2367f0deb3c71f90620d1ab202bd5f75c9987
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
<<<<<<< HEAD
    global counter
    if counter == 0:
        counter += 1
        return greetings(input)
    elif any(elem in input for elem in link_list):
        return find_items(input)
    elif "you like" in input and input.endswith("?"):
        return do_you_like(input)
    elif any(elem in input for elem in like_list):
        return result(input)
    elif any(elem in input for elem in dislike_list):
        return result(input)
    elif any(elem in input for elem in curse_list):
        return swear_words(input)
    elif any(elem in input for elem in city_list):
        return weather_2(input)
    elif any(elem in input for elem in weather_list):
        return weather_1()
    elif any(elem in input for elem in hello_list):
        return start_conversation()
=======
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
>>>>>>> 96b2367f0deb3c71f90620d1ab202bd5f75c9987
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

