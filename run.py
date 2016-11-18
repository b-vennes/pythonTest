from flask import Flask, request, redirect, session
import twilio.twiml, random

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

greetings = ["Hello! ", "Hi! ", "Hey! "]

questions = ["How are you? ", "What's up? ", "How's it going? "]

@app.route("/", methods=['GET', 'POST'])
def replyMethod():

    resp = twilio.twiml.Response()

    greeting = random.choice(greetings)

    question = message + random.choice(questions)

    message = greeting + question

    resp.sms(message)

    return str(resp)

if __name__ == "__main__":
    app.run()
    
