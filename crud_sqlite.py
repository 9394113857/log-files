from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL)''')

conn.commit()
conn.close()


@app.route('/')
def index():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return render_template('index.html', users=users)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    email = request.form['email']
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
