import os
import sys
import json
import logging
import traceback

from flask import Flask, request
from views.send_mail import Sender

logger = logging.getLogger(__name__)

def init_app(app):
    @app.route("/", methods=[""GET", "POST"])
    def main():
        return json.dumps({"status": "0000", "msg": "OK!"})


