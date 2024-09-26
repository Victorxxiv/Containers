from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# use environment variables to get the database URL
app.config['SQLALCHEMY_DATABASE_URS'] = 'postgresql://user:password@db:5432/mydb'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'Hello from Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)