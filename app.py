import logging
import os

from flask import Flask

from openpyxl import load_workbook
from io import BytesIO

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    wb2 = load_workbook(flask.request.files['file'])
    wb2['Feuil1']['A1'] = 'Paul est le boooo'
    writer = BytesIO()
    wb2.save(writer)
    writer.seek(0)
    # raiponce = func.HttpResponse(writer.getvalue(), mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return flask.send_file(writer, as_attachment=True,
    attachment_filename='file.xslx', mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
