from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


index = [{'name': 'python', 'text': 'Welcome to python training!!'},
          {'name': 'coc', 'text': 'Welcome to clash of clans!!'}]

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})

@app.route('/index', methods=['GET'])
def returnAll():
    return jsonify({'index' : index})


@app.route('/index/<string:name>', methods=['GET'])
def returnOne(name):
    theOne = index[0]
    for i,q in enumerate(index):
      if q['name'] == name:
        theOne = index[i]
    return jsonify({'index' : theOne})

if __name__ == "__main__":
    app.run(debug=True)
