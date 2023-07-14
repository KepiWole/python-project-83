from flask import Flask, render_template
import os

app = Flask(__name__)
load_dotenv(find_dotenv())
DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')
app.config.update(SECRET_KEY=SECRET_KEY)


@app.route('/')
def main_get():
	return render_template('main.html')

