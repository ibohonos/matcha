from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, Im Flask on VestaCP!'
if __name__ == '__main__':
    app.run()

