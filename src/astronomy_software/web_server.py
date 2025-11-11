from flask import Flask, render_template
import os
from .nasa_api import get_apod
import argparse

app = Flask(__name__, template_folder=os.path.abspath('src/astronomy_software/driving_school'))

@app.route('/')
def index():
    apod_data = get_apod()
    return render_template('index.html', apod_data=apod_data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-reload', action='store_true')
    args = parser.parse_args()
    app.run(debug=True, use_reloader=not args.no_reload, host='0.0.0.0')
