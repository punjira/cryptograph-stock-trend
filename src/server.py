from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast

import os
import sys

sys.path.append(os.path.join(sys.path[0],"endpoints"))
sys.path.append(os.path.join(sys.path[0],"helpers"))

from endpoints.tree import Tree

app = Flask(__name__)
api = Api(app)

api.add_resource(Tree, "/create")

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)