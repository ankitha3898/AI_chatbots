from flask import Flask, request,jsonify

# import requests


app = Flask(__name__)


# @app.route("/")
# def question1():
#     return "hello"


@app.route("/")
def hello():
    return "ques2"


@app.route('/api', methods=['GET', 'POST'])
def update():
    try:
        if request.method == 'POST':
            data = request.form['str']
            typevar = request.form['type']
        # x = data +'*'+typevar
        return ("success")
    except:
        print("failed")


if __name__ == '__main__':
    app.run()

    # run() method of Flask class runs the application
    # on the local development server.
#     app.run(debug=True)