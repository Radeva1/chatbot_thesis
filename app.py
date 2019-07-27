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


if __name__ == "__main__":
    app.run(debug=True)