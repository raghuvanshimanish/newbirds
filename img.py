from flask import Flask,session,escape,url_for,render_template,redirect,flash,request,g, send_from_directory
import sqlite3


app = Flask(__name__,static_folder="static")

#----------Index Page start------------
@app.route('/')
def index():
	conn = sqlite3.connect('dbirds.db')
	c = conn.cursor()
	c.execute("SELECT *FROM user")
	result = c.fetchall()
	print result
	conn.commit()
	conn.close()	
	return render_template('index.html', dis=result)
	
#----------Create user account Signup---------


@app.route('/signup', methods = ['POST'])
def signup():
	conn = sqlite3.connect('dbirds.db')
	c = conn.cursor()
	name = request.form['name']
	email = request.form['email']
	contact = request.form['contact']
	city = request.form['city']
	cpny = request.form['cpny']
	record = (name, email, contact, city, cpny)
	c.execute("INSERT INTO user VALUES (NULL, ?, ?, ?, ?,?)", record)
	conn.commit()
	conn.close()
	return redirect('/')
	

#----------Delete user ---------
	
@app.route('/delete', methods = ['POST'])
def delete():
	conn = sqlite3.connect('dbirds.db')
	c = conn.cursor()
	dele = request.form['del']
	c.execute("Delete FROM user where id=?", [dele])
	result = c.fetchall()
	print result
	conn.commit()
	conn.close()	
	return redirect('/')
	
	
if __name__ == "__main__":
    app.run(host='0.0.0.0')
