from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, update_task_status
from todo_app.data.database_client import add_task_to_db, delete_item_in_db
from todo_app.flask_config import Config
from todo_app.view_models.items_view_model import ItemsViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items_view_model = ItemsViewModel(get_items())
        return render_template('index.html', view_model = items_view_model)

    @app.route('/submit', methods = ["POST"])
    def create_new_task():
        task_name = request.form.get("name")
        task_description = request.form.get("description")
        add_task_to_db(task_name, task_description)
        return redirect(url_for('index'))

    @app.route('/update', methods = ["POST"])
    def update_item_status():
        card_id = request.form.get("item-id")
        if (request.form['action'] == "delete"):
            delete_item_in_db(card_id)
            return redirect(url_for('index'))
        else:
            card_status = request.form['action']
            update_task_status(card_id, card_status)
            return redirect(url_for('index'))

    return app