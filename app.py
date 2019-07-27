from flask import Flask, render_template, request, redirect
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
# import logging
#
# logger = logging.getLogger()
# logger.setLevel(logging.ERROR)


app = Flask(__name__)

bot = ChatBot("Robo")

trainer = ListTrainer(bot)
trainer.train(['What is your name?', 'My name is Robo'])
trainer.train(['Who are you?', 'I am a bot'])
trainer.train(['Who created you?', 'Tony Stark', 'Eli', 'You?'])

trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.sales")


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", year=datetime.now().year)


@app.route("/get", methods=['GET', 'POST'])
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html', title='Contact', year=datetime.now().year, user='Eli')


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html', title='About', year=datetime.now().year, user='Eli')



if __name__ == "__main__":
    app.run(debug=True)