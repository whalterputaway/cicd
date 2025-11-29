from flask import Flask
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
dbname1 = os.getenv('dbname1')
user1 = os.getenv('user1')
password1 = os.getenv('password1')
host1 = os.getenv('host1')

app = Flask(__name__)
@app.route('/')
def index():
	conn = psycopg2.connect(dbname=dbname1, user=user1,password=password1,host=host1)
	cursor = conn.cursor()

	cursor.execute('CREATE TABLE products (id int IDENTITY PRIMARY KEY, name char(30))')
	cursor.execute("INSERT INTO products (name) VALUES ('milk')")
	cursor.execute("INSERT INTO products (name) VALUES ('bread')")
	cursor.execute("INSERT INTO products (name) VALUES ('meat')")
	cursor.execute("INSERT INTO products (name) VALUES ('water')")
	cursor.execute("SELECT * FROM products LIMIT 10')
	records = cursor.fetchall()
	
	cursor.close()
	conn.close()
	
	return '<h1>Hello from MIREA!<h1>' + f'{"<p>".join(map(str,records))}'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=4000)
