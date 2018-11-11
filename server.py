from flask import Flask, render_template
from flask import request
from libsafewhey import SafeWhey
import distance_calc
import googlemaps
app = Flask(__name__)

gmaps_key = "AIzaSyA-L1-CDamtVsUcngy65o54omBY_wn9TT0"
gmaps = googlemaps.Client(key = gmaps_key)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/map', methods=['GET', 'POST'])
def map():
	if request.method == 'POST':
		vals = SafeWhey(request.form['start'], request.form['dest'])

		directions_result = distance_calc.create_directions_result()
		try:
			start_coord = gmaps.geocode(request.form['start'])[0]['geometry']['location']
			# print('success: {0}'.format(gmaps.geocode(request.form['start'])[0]))
		except:
			print('err: {0}'.format(gmaps.geocode(request.form['start'])))
			return render_template('index.html', err='enter valid address')
	else:
		directions_result = distance_calc.create_directions_result()
	print(vals['safety_vals'])
	# return render_template('goog_map_example.html', results=vals['safety_vals'], 
	# 	start=request.form['start'], end=request.form['dest'], mode="WALKING", 
	# 	origin=start_coord, num_routes=vals['num_routes'])

	return render_template('goog_map_example.html', results=[45, 45, 45], 
		start=request.form['start'], end=request.form['dest'], mode="WALKING", 
		origin=start_coord, num_routes=vals['num_routes'], holder=0)

if __name__ == '__main__':
	app.run(debug=True)