from flask import Flask
from routes import routes

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Register blueprints
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
