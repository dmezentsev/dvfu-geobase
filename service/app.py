import os
from flask import Flask

from service.api import configure
from service.geobase import Geobase

flask = Flask(__name__, instance_path=os.getcwd())
geobase = Geobase()
configure(flask, geobase)

if __name__ == "__main__":
    flask.run(host="0.0.0.0", port=5001)
