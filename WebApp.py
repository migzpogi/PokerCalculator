from flask import Flask, request
app = Flask(__name__)

@app.route("/poker")
def hello():
    board = request.args.get('board')
    hand = request.args.get('hand')
    return board+hand

if __name__ == '__main__':
    app.run()