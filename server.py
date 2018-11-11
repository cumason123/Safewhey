from flask import Flask, render_template
import distance_calc
app = Flask(__name__)

gmaps_key = "AIzaSyA-L1-CDamtVsUcngy65o54omBY_wn9TT0"

@app.route('/')
def hello_world():
    return render_template('index.html', message="My name is curt")

@app.route('/map')
def map():
    directions_result = distance_calc.create_directions_result()
    #result = distance_calc.create_directions()
    return render_template('goog_map_example.html', result=directions_result)

if __name__ == '__main__':
    app.run(debug=True)