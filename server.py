from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message="My name is curt")

@app.route('/map')
def map():


if __name__ == '__main__':
    app.run(debug=True)


curl -X POST "https://apis.solarialabs.com/shine/v1/total-home-scores/bulk-search?apikey=FfFYj6Z02qDq58tNnOySJKZqavjARqI9" -d "{
    "data": [
        {
            "lat": "42.3545165",
            "lon": "-71.1263265"
        }
    ],
    "pageSize": "10"
}"