import os
import sys

HOME = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HOME, "conf"))
sys.path.append(os.path.join(HOME, "bin"))

from bin.utils import create_logger

create_logger()

from server import app
from config import config

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=config.PORT, debug=config.DEBUG)
