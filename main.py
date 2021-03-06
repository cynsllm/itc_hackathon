"""
This is the template server side for ChatBot
"""

from bottle import route, run, template, static_file, request
import json
import random
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='davidzerah28#05',
                             db='cows',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)



def cows_data():
        with connection.cursor() as cursor:
            sql = "SELECT description FROM disease"
            cursor.execute(sql)
            result = cursor.fetchall()
            arr = []
            for elem in result:
                arr.append(elem["description"])
            answer = "I have 67% chance of having " + random.choice(arr)
            return answer



heart_list = ["heart", "beat", "beating", "heartbeat", "heartrate", "rate"]
body_list = ["body condition", "body", "condition"]
greeting_list = ["hey", "hi", "hello"]
drink_list = ["water", "drink", "liter"]
food_list = ["eat", "food"]
weight_list = ["weight", "pound", "weigh"]
feeling_list = ["how are", "feel", "feelings", "sick"]
pregnant_list = ["baby", "pregnant", "pregnancy"]
walking_list = ["steps", "step", "walk", "walking", "out", "outside"]
production_list = ["milk", "production"]
temp_list = ["temp", "temperature", "fever"]
sick_list = ["serious", "doctor", "vet", "medicines", "injection"]



def temp():
    answer = "My temperature is high, 39.2°C"
    return answer


def heart():
    answer = "67 beats per minute, my heart rate is okay"
    return answer

def body():
    answer = "My body condition score is: 3/10"
    return answer


def feeling():
    answer = "I'm not that good..."
    return answer


def greeting():
    answer = "Hey Morad!"
    return answer

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


def insemination():
    answer = "I had insemination 10 months ago."
    return answer

def pregnant():
    answer = "I have 10% chance of being pregnant."
    return answer


def walking():
    answer = "I spent all the day in the stable."
    return answer

def production():
    answer = "I produced 13.7L today."
    return answer


def meu():
    answer = "Meuuuuuuuuuuuuuuuuuuuuuu"
    return answer


def sick():
    answer = "Yes, call a doctor please..."
    return answer

def error_message():
    answer_list = "What do you mean ?"
    return answer_list



def bot_message(input):
    input = input.lower()
    if any(elem in input for elem in greeting_list):
        return greeting()
    elif input.startswith("how are"):
        return feeling()
    elif input.startswith("cow are"):
        return feeling()
    elif input.startswith("why"):
        return cows_data()
    elif any(elem in input for elem in temp_list):
        return temp()
    elif any(elem in input for elem in heart_list):
        return heart()
    elif any(elem in input for elem in body_list):
        return body()
    elif any(elem in input for elem in feeling_list):
        return feeling()
    elif "sick" in input:
        return cows_data()
    elif any(elem in input for elem in sick_list):
        return sick()
    elif any(elem in input for elem in walking_list):
        return walking()
    elif any(elem in input for elem in pregnant_list):
        return pregnant()
    elif any(elem in input for elem in drink_list):
        return drink()
    elif any(elem in input for elem in food_list):
        return food()
    elif any(elem in input for elem in weight_list):
        return weight()
    elif any(elem in input for elem in production_list):
        return production()
    elif "did you do" in input:
        return do()
    elif "insemination" in input:
        return insemination(input)
    elif input.startswith("meu"):
        return meu()
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



@route('/pics/<filename:re:.*\.(jpg|png|gif|ico|jpeg)>', method='GET')
def images(filename):
    return static_file(filename, root='pics')


@route('/fonts/<filename:re:.*\.ttf>', method='GET')
def images(filename):
    return static_file(filename, root='fonts')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()

