#comment: if lib not present do pip/pip3 install flask :)
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

db_config = {
   'host' : 'localhost',
   'user' : 'root',
   'password' : '',
   'database' : 'test'
}

db_conn = pymysql.connect(**db_config)
cursor = db_conn.cursor()

# Route to get all items
@app.route('/items', methods=['GET'])
def get_items():
   try :
      cursor.execute("SELECT ID, Nombre FROM items")
      items = [{'ID':ID, 'Nombre':Nombre} for ID, Nombre in cursor.fetchall()]
      return jsonify(items)
   except Exception as e:
        return jsonify({'error': str(e)})

# Route to insert value in DB
@app.route('/items', methods=['POST'])
def insert_items():
    try:
        data = request.get_json()
        nombre = data.get('name')
        precio_raw = data.get('precio')
        precio = float(precio_raw)
        cursor.execute("INSERT INTO items (Nombre, Precio) VALUES (%s, %s)", (nombre, precio))
        db_conn.commit()
        return jsonify({'message': 'El Item ha sido agregado exitosamente!'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Route to update value in DB
@app.route('/items/<int:id>', methods=['PUT'])
def update_items(id):
    try:
        data = request.get_json()
        nombre = data.get('name')
        precio_raw = data.get('precio')
        precio = float(precio_raw)
        cursor.execute("UPDATE items SET Nombre=%s, Precio=%s WHERE ID=%s", (nombre, precio, id))
        db_conn.commit()
        return jsonify({'message': 'El Item ha sido actualizado exitosamente!'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Route to Delete value in DB
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_items(id):
    try:
        cursor.execute("DELETE FROM items WHERE ID=%s", (id))
        db_conn.commit()
        return jsonify({'message': 'El Item ha sido eliminado exitosamente!'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
   app.run(debug=True)
