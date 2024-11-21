from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE_FILE = 'database.txt'

@app.route('/add-client', methods=['POST'])
def add_client():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'success': False, 'error': 'Name is required'}), 400

    try:
        with open(DATABASE_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{name}|Тип A|Категория 1\n")
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
