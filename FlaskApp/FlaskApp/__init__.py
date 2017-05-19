import sqlite3
import os
from flask import g
from flask import Flask, request

app = Flask(__name__)
DATABASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../database/firebirddb.db'))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello():
    return "Hellow world"

@app.route("/reject", methods=['POST'])
def reject():
    photo_filename = request.form["photo_filename"]
    username = request.form["username"]
    db = get_db()
    db.execute("INSERT OR IGNORE INTO Users (Username) VALUES (?)", [username])
    db.execute("INSERT INTO Classifications (PhotoId, UserId, FirelineData, WasRejected) VALUES ((SELECT PhotoId FROM Photos WHERE Filename == ?), (SELECT UserId FROM Users WHERE Username == ?), NULL, 1)", [photo_filename, username])
    db.commit()

    return "Success"

if __name__ == "__main__":
    app.run()
