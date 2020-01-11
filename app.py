from flask import Flask, render_template
from gevent.pywsgi import WSGIServer
import mysql.connector
import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.test

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ranjit@123",
    database="test"
)

app = Flask(__name__)


@app.route('/')
def index():
    conCursor = con.cursor()

    conCursor.execute("SELECT * FROM user")

    result = conCursor.fetchall()

    for x in result:
        print(x)

    # return "<h3> Hello Python... </h3>" 
    return render_template('index.html', users = result)

@app.route('/about')
def about():
    print(db.name)
    for item in db.user.find():
        print(item)
    return '<h3> About page </h3>'

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()


""" ========run:- "flask run" to run this flas app========= """
