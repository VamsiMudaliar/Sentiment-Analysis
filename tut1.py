from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import pymysql as sql

app= Flask(__name__)

try: 
	db_connection= sql.connect(host="localhost",user="root",password="",database="amazonreview") 
	print("Done")
except: 
	print("Can't connect to database")

cur=db_connection.cursor()

@app.route("/")

def hello():
	return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
	if(request.method=='POST'):
		name= request.form.get('name')
		email=request.form.get('email')
		password=request.form.get('password')
		cur.execute("SELECT * from userdetails where Name=name and Password=password")
		
	return render_template("login.html")


@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/abc",methods =["GET","POST"])

def contact():
	if(request.method=='POST'):
		name = request.form.get('name')
		email = request.form.get('email')
		phone = request.form.get('phone')
		password = request.form.get('password')
		cur.execute("INSERT INTO userdetails(Name,Email,Phone,Password) VALUES(%s,%s,%s,%s)",[name,email,phone,password])
		db_connection.commit()
		db_connection.close()
	return render_template('login.html')



app.run(debug=True)
