from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
#import pandas as pd

#include json library
import json
import ast

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    # base URL
    courses_link = "https://courses.ineuron.ai"
    course_resp = requests.get(courses_link)
    course_resp.encoding = 'utf-8'
    app.logger.debug(course_resp)

    # Parse object
    course_html = bs(course_resp.text, "html.parser")
    app.logger.debug(type(course_html))
    app.logger.debug(course_html.prettify())

    category_string = course_html.body.script.string
    app.logger.debug(category_string)

    # convert string to  object
    json_object = json.loads(category_string)
    app.logger.debug(type(json_object))

    # Pretty Print JSON
    json_formatted_str = json.dumps(json_object['props']['pageProps']['initialState']['init'], indent=4)
    app.logger.debug('Pretty Print JSON')
    app.logger.debug(json_formatted_str)

    return render_template('index.html', title="page", jsonfile=json_formatted_str)

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=5000, debug=True)
	app.run(debug=True)
