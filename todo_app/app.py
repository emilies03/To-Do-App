from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item, update_task_status
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return render_template('index.html', items=get_items())

@app.route('/submit', methods = ["POST"])
def submit_review():
    task_name = request.form.get("task-name")
    add_item(task_name)
    return redirect(url_for('index'))

@app.route('/update', methods = ["POST"])
def update_item_status():
    item_id = request.form.get("item-id")
    update_task_status(item_id)
    return redirect(url_for('index'))