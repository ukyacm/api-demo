import flask
from flask.ext import restful
import example

app = flask.Flask(__name__)
api = restful.Api(app)

class MashupResource(restful.Resource):

    def get(self, user):
        return example.mashup(user)

api.add_resource(MashupResource, '/mashup/<string:user>', endpoint='mashup')

if __name__ == '__main__':
    app.run()
