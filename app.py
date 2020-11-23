from flask import Flask
from flask_restful import Resource, Api, reqparse 
import os

app = Flask(__name__)
api = Api(app)

DATA = {
    'places': [
        'rome', 'london', 'new york city', 'los angeles', 'brisbane',
        'new delhi', 'beijing', 'paris', 'berlin', 'barcelona',
    ]
}


class Places(Resource):
    def get(self):
        #return our data and 200, OK HTTP code
        return {'data': DATA}, 200
    
    def post(self):
        args = self._parse_request()

        # check if we already have the location in the places list
        if args['location'] in DATA['places']:
            return {'messsage' : f"'{args['location']}' already exitsts"}, 401
        DATA['places'].append(args['location'])
        return {'data': DATA}, 200

    def delete(self):
        args = self._parse_request()

        if args['location'] in DATA['places']:
            DATA['places'].remove(args['location'])
            return {'data' : DATA}, 200

        return {'message' : f"'{args['location']}' does not exist"}, 404

    def _parse_request(self):
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True)
        return parser.parse_args()


api.add_resource(Places, '/places')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))