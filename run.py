from flask import Flask, request, redirect, session
import twilio.twiml

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+15032770678": "Branden",
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    resp = twilio.twiml.Response()
    resp.message("Hi Cole")
    return str(resp)

if __name__ == "__main__":
    app.run()
