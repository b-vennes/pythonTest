from flask import Flask, request, redirect, session
import twilio.twiml, random

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

greetings = dict("Hello! " = 0, "Hi! " = 1, "Hey! " = 2)

questions = dict("How are you?" = 0, "What's up?" = 1, "How's it going?" = 2)

@app.route("/", methods=['GET', 'POST'])
def replyMethod():

    # Will eventually check message for ISBN

    resp = twilio.twiml.Response()

    randomInt = random.randrange(0, 5)

    message = random.choice(greetings.keys())

    message = message + random.choice(questions.keys())

    resp.sms(message)

    return str(resp)

if __name__ == "__main__":
    app.run()
