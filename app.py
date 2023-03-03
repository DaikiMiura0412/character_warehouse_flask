from flask import Flask, render_template, request
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']

def create_table():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user_info (name TEXT, age INT, hometown TEXT);")
    conn.commit()
    cur.close()
    conn.close()

def insert_data(name, age, hometown):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("INSERT INTO user_info (name, age, hometown) VALUES (%s, %s, %s)", (name, age, hometown))
    conn.commit()
    cur.close()
    conn.close()

def select_data():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("SELECT name, age, hometown FROM user_info")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = request.form['age']
    hometown = request.form['hometown']
    insert_data(name, age, hometown)
    return render_template('index.html')

@app.route('/list')
def show_list():
    rows = select_data()
    return render_template('list.html', rows=rows)

if __name__ == '__main__':
    create_table()
    app.run(debug=True, host='0.0.0.0')
