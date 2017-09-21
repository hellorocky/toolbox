import os
import sys
import json
import logging
import traceback

from flask import Flask
from flask import request

HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(HOME, "conf"))
sys.path.append(os.path.join(HOME, "bin"))

from config import config
from utils import create_logger
from views.send_mail import Sender
from api import init_app

create_logger()

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(config["default"])
init_app(app)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=app.config["PORT"], debug=False)
