from flask import Flask, request, redirect, session
import twilio.twiml, random

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/", methods=['GET', 'POST'])
def replyMethod():

    # Will eventually check message for ISBN

    resp = twilio.twiml.Response()

    randomInt = random.randrange(0, 2)

    if (randomInt == 0):
        message = "Hi! Thanks for messaging Tricia! What can I do for you?"
    elif (randomInt == 1):
        message = "Hi! Thanks for texting! Have a great day!"
    elif (randomInt == 2):
        message = "Howdy! Tricia here!"

    resp.sms(message)

    return str(resp)

if __name__ == "__main__":
    app.run()
