from flask import Flask
from flask_restful import Resource, Api, reqparse

from logic import routine

class Tree(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()

            parser.add_argument('ticker', required=True)
            parser.add_argument('frame', required=True)
            
            args = parser.parse_args()

            ticker = args['ticker']
            frame = args['frame']
            key = ticker+"-"+frame
            message = routine(key)
            return {"data": message}
        except Exception as e:
            print(e)
            return {"error": "something went wrong"}