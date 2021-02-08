import logging
import os

from flask import Flask, request, send_file
import xlwings as xw
from io import BytesIO

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    wb = xw.Book(request.files['file'])
    sht0 = wb.sheets[0]
    sht0.range('A1').value = 'Hello Paul'
    a1 = xw.Range('A1')
    a1.color = (255, 0, 0)
    wb.save('file.xlsx')
    # writer = BytesIO()
    # wb.save(writer)
    # writer.seek(0)
    # raiponce = func.HttpResponse(writer.getvalue(), mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") 
    # return send_file(, as_attachment=True,
    # attachment_filename='file.xslx', mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return "Hello World"

