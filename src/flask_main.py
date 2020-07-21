from flask_restplus import Resource, Api, fields, reqparse
from flask import Flask

from sparse_array import SparseArray
import os
app = Flask(__name__)
api = Api(app)

one_result = api.model('Occurrence', {
    'word': fields.String,
    'occurrence': fields.String,
})

results_fields = api.model('Result', {
    'result': fields.List(fields.Nested(one_result)),
})

parser = reqparse.RequestParser()
parser.add_argument('query', type=str, help='words separated by comma, ex: x,y,z')

sparse_array = SparseArray(os.environ['INPUT'])


@api.route('/api')
class HelloWorld(Resource):
    @api.marshal_with(results_fields)
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        result = sparse_array.compute(args['query'].split(","))
        output = []
        for word, occurrence in result.items():
            output.append({'word': word, 'occurrence': occurrence})
        return {'result': output}


if __name__ == '__main__':
    app.run(host='0.0.0.0')


