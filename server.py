from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message="My name is curt")

@app.route('/map')
def map():


if __name__ == '__main__':
    app.run(debug=True)