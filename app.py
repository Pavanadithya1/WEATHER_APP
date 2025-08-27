from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = "30d4741c779ba94c470ca1f63045390a"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city_name = request.form['city']
        complete_url = f"{base_url}appid={api_key}&q={city_name}"
        response = requests.get(complete_url)
        data = response.json()
        if data.get("cod") != "404":
            main_data = data["main"]
            weather = data["weather"][0]
            weather_data = {
                "temperature": f"{main_data['temp']} ",
                "pressure": f"{main_data['pressure']}",
                "humidity": f"{main_data['humidity']}",
                "description": weather["description"].upper(),

                "icon": weather["icon"],
                "city": city_name.upper()
            }
        else:
            weather_data = {"error": "CITY NOT FOUND"}  # Set error message when city is not found

    return render_template('index.html', weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)