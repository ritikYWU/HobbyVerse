from flask import Flask
from src.web import pages


app = Flask(__name__)

app.register_blueprint(pages.bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', prort='5000')