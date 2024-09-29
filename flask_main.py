import  sqlite3
import database
from flask import Flask, request, jsonify




app = Flask(__name__)


database.init()


@app.route('/')
def index():
    return "Hello, World!"

# Get all
@app.route('/members')
def get_members():
    res = database.read_all()

    return jsonify(res), 200

# Get one
@app.route('/members/<int:id>')
def get_member(member_id):
    con = sqlite3.connect("flask_ex.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM members WHERE rowid = ?",(member_id))
    member = cur.fetchall()
    
    con.close()
    
    return jsonify(member)

@app.route('/api/members/create', methods=['POST'])
def create_member():
    
    new_member = request.get_json()


    conn = sqlite3.connect('flask_ex.db')
    c = conn.cursor()
    c.execute("INSERT INTO members VALUES(?,?,?,?,?,?,?,?,?,?,?)", tuple(new_member.values()))
    conn.commit()

    return jsonify(new_member), 201



if __name__ == '__main__':
    app.run(debug=True)