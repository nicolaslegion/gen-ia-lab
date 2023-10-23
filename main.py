from flask import Flask
from controllers.main_controller import main_controller
from models.data_access import initialize_database, create_tables

app = Flask(__name__)

app.secret_key = 'testing-key'
app.register_blueprint(main_controller)
app.config['DEBUG'] = True

with app.app_context():
    initialize_database()
    create_tables()

if __name__ == '__main__':
    app.run()