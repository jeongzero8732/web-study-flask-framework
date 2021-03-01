# manage.py 
import os 
from flask_script import Manager 
from flask_migrate import Migrate, MigrateCommand
from app import create_app,db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev') 
app.app_context().push()

manager = Manager(app)

# migrate = Migrate(app, db)

# manager.add_command('db', MigrateCommand)

@manager.command 
def run(): 
    app.run(host='0.0.0.0') 

if __name__ == "__main__": 
    manager.run()

