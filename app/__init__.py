from flask import Flask
from config import Config

config = Config()

app = Flask(__name__)  # The variable __name__ is set to the name of the module being used
app.config.from_object(config)

from app.routes import *
