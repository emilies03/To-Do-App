from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item, update_task_status
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
    def submit_review():
        task_name = request.form.get("name")
        task_description = request.form.get("description")
        add_item(task_name, task_description)
        return redirect(url_for('index'))

    @app.route('/update', methods = ["POST"])
    def update_item_status():
        card_id = request.form.get("item-id")
        card_status = request.form.get("item-status")
        update_task_status(card_id, card_status)
        return redirect(url_for('index'))

    return app