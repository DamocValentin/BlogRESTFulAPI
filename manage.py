import os
from flask_migrate import Migrate, MigrateCommand
from src.app import create_app, db
import flask_script

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

migrate = Migrate(app, db)

manager = flask_script.Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
