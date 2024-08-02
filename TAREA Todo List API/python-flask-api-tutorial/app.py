from flask import Flask, jsonify, request

app = Flask(__name__)

to_do_database = [
    {"done": True, "label": "Sample To do 1"},
    {"done": False, "label": "Sample To do 2"},
    {"done": False, "label": "Sample To do 3"}
]

@app.route('/to_do')
def get_to_do(): 
    return jsonify(to_do_database), 200

@app.route('/to_do', methods=['POST'])
def create_to_do():
    to_do = request.json
    to_do_database.append(to_do)
    return jsonify({"message": "Task created successfully"}), 201

@app.route('/to_do/<int:to_do_position>', methods=['DELETE'])
def delete_to_do_by_id(to_do_position):
    if 0 <= to_do_position < len(to_do_database):
        to_do_database.pop(to_do_position)
        return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)