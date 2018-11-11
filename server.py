from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', InputData='My name is cj')

if __name__ == '__main__':
    params = (
        ('address', '{value}'),
        ('street-number', '{value}'),
        ('street-name', '{value}'),
        ('city', '{value}'),
        ('state', '{value}'),
        ('zip-code', '{value}'),
        ('lat', '{value}'),
        ('lon', '{value}'),
        ('apikey', '{value}'),
    )

    response = requests.get('https://apis.solarialabs.com/shine/v1/total-home-scores/reports', params=params)
    print(response)
    app.run(debug=True)
