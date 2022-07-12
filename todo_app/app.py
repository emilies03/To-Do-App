from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

def update_csv(task_name):
    with open("./todo_app/todo_list.csv", 'a') as file:
        file.write(f"\n{task_name}")

@app.route('/')
def index():
    with open("./todo_app/todo_list.csv") as file:
        todo_items = [  {'task': line } for line in file ]
    return render_template('index.html', items=todo_items)

@app.route('/submit', methods = ["POST"])
def submit_review():
    task_name = request.form.get("task-name")
    update_csv(task_name)
    return redirect(url_for('index'))