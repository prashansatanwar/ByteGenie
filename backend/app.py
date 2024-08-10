from flask import Flask
from flask_cors import CORS
from api import api

app = Flask(__name__)
CORS(app)

# Register api blueprint
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)