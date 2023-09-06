from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.database_client import DatabaseClient
from todo_app.flask_config import Config
from todo_app.view_models.items_view_model import ItemsViewModel
from todo_app.data.constants import LOGGER_NAME
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    logging.basicConfig(level = app.config['LOG_LEVEL'])
    client = DatabaseClient()

    @app.route('/')
    def index():
        items_view_model = ItemsViewModel(client.get_items())
        return render_template('index.html', view_model = items_view_model)

    @app.route('/submit', methods = ["POST"])
    def create_new_task():
        task_name = request.form.get("name")
        task_description = request.form.get("description")
        logging.getLogger(LOGGER_NAME).info(f'Adding new task to DB with name: {task_name}, description: {task_description}')
        client.add_task_to_db(task_name, task_description)
        return redirect(url_for('index'))

    @app.route('/update', methods = ["POST"])
    def update_item_status():
        item_id = request.form.get("item-id")
        if (request.form['action'] == "delete"):
            logging.getLogger(LOGGER_NAME).info(f'Deleting task in DB with id: {item_id}')
            client.delete_item_in_db(item_id)
            return redirect(url_for('index'))
        else:
            task_status = request.form['action']           
            logging.getLogger(LOGGER_NAME).info(f'Updating task in DB with id: {item_id}')
            client.update_task_status(item_id, task_status)
            return redirect(url_for('index'))

    return app