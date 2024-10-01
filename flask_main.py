import os
import database
import github_service as gs
from flask import Flask, request, jsonify, make_response, render_template


app = Flask(__name__)


database.init()


@app.route('/')
def index():
    return render_template('index.html')

# Get all
@app.route('/members')
def get_members():
    res = database.read_all()

    return jsonify(res), 200

# Get one
@app.route('/members/<int:id>')
def get_member(id):
    res = database.read(id)

    if not res:
        return jsonify(message="Member not found"), 404

    return jsonify(res), 200


# List Public repositories
@app.route('/members/<id>/repos')
def get_repos(id):
    res = database.read(id)

    if not res:
        return jsonify(message="Member not found"), 404

    username = res[0]['github_username']


    # returns a list
    return jsonify(gs.get_repo_list(username)), 200



# Create new member
@app.route('/members', methods=['POST'])
def create_member():
    
    new_member = request.get_json()
    id = database.create(new_member)
    response = make_response(jsonify(success=True, message="Resource created"), 201)
    response.headers['Location'] = f'/members/{id}'

    return response
    #return new_member

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    member = request.get_json()
    database.update(id, member)

    return jsonify(), 204

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    database.delete(id)

    return jsonify(), 204

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host='0.0.0.0',port=port)