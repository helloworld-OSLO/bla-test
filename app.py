import logging
import os

import flask

from openpyxl import load_workbook
from io import BytesIO

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    # wb2 = load_workbook(flask.request.files['file'])
    # wb2['Feuil1']['A1'] = 'Paul est le boooo'
    # writer = BytesIO()
    # wb2.save(writer)
    # writer.seek(0)
    # # raiponce = func.HttpResponse(writer.getvalue(), mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    # return flask.send_file(writer, as_attachment=True,
    # attachment_filename='file.xslx', mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return "Hello World"

if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)