from flask import Flask, render_template
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="test"
)

app = Flask(__name__)


@app.route('/')
def index():
    conCursor = con.cursor()

    conCursor.execute("SELECT * FROM student")

    result = conCursor.fetchall()

    for x in result:
        print(x)

    # return "<h3> Hello Python... </h3>" 
    return render_template('index.html', students = result)

@app.route('/about')
def about():
    return '<h3> About page </h3>'

if __name__ == "__main__":
    app.run(debug=True)


""" ========run:- "flask run" to run this flas app========= """
