from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='mydb'
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=('GET', 'POST'))
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title, description, due_date) VALUES (%s, %s, %s)',
                        (title, description, due_date))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('add_task.html')

@app.route('/edit/<int:task_id>', methods=('GET', 'POST'))
def edit_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
    task = cursor.fetchone()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']

        cursor.execute('UPDATE tasks SET title = %s, description = %s, due_date = %s WHERE id = %s',
                       (title, description, due_date, task_id))
        conn.commit()
        return redirect(url_for('index'))

    cursor.close()
    conn.close()
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>', methods=('POST',))
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()

    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)