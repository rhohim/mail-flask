from flask import Flask, render_template, request
import smtplib
from flask_mysqldb import MySQL, MySQLdb
import base64
from email.mime.text import MIMEText

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cvoxdev'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template('index.html')

@app.route("/form", methods=["GET", "POST"])
def form():
    name = request.form.get("Name")
    number = request.form.get("Number")
    email = request.form.get("Email")
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM info WHERE UserId=%s",("cretivox.web@gmail.com",))
    user = curl.fetchone()
    curl.close() 
    msg = MIMEText('\033[1m' + "test send email from smtp @cvoxdev " + name + " " + number + " " + email + '\033[1m' )
    msg['Subject'] = 'Test mail'    
    msg['From'] = 'cretivox.web@gmail.com'
    msg['To'] = 'cretivox.dev@gmail.com'
    #msg = "test send email from smtp @cvoxdev " + name + " " + number + " " + email 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("cretivox.web@gmail.com", base64.b64decode(user["UserPassword"]).decode("utf-8"))
    server.sendmail("cretivox.web@gmail.com", "cretivox.dev@gmail.com", msg.as_string())
    return render_template('index.html')


if __name__ == '__main__':

    app.run(debug = True)