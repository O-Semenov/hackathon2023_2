from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from views import stock_blueprint
import handlers
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warehouses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.register_blueprint(stock_blueprint)

if __name__ == '__main__':
    app.run()
