from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Ludochka!!'


@app.route('/registration')
def registration():
    return render_template('register.html', name="asd")


@app.route('/ajax_registration', methods=['POST', 'GET'])
def ajax_registration():

    print(request.form['title'])
    return jsonify("return from python")


if __name__ == '__main__':
    app.run()
