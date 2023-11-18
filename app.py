from flask import Flask, request, jsonify
from dbfuncs import create_db_connection, create_table, insert_name, get_names, delete_name, update_name

app = Flask(__name__)

conn = create_db_connection()

# Create a table called names in the database
create_table(conn)

# Create a route to insert a name into the database


@app.route('/newname', methods=['POST'])
def newname():
    name = request.json['name']
    if insert_name(conn, name):
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'failure'})

# Create a route to get all the names from the database


@app.route('/getnames', methods=['GET'])
def getnames():
    names = get_names(conn)
    if names is not None:
        return jsonify({'result': [{'id': row[0], 'name': row[1]} for row in names]})
    else:
        return jsonify({'result': 'failure'})


# Create a route to update a name in the database
@app.route('/updatename', methods=['PUT'])
def updatename():
    idno = request.json['id']
    name = request.json['name']
    if update_name(conn, idno, name):
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'failure'})

# Create a route to delete a name from the database


@app.route('/deletename', methods=['DELETE'])
def deletename():
    idno = request.json['id']
    if delete_name(conn, idno):
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'failure'})


app.run(host='0.0.0.0', port=5000)
