from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Путь к файлу базы данных
DATABASE_FILE = 'database.txt'

# Проверяем, существует ли файл database.txt, если нет, создаем пустой
if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, 'w', encoding='utf-8') as f:
        f.write('')  # Создаем пустой файл

@app.route('/')
def home():
    return "Сервер работает! Вы можете использовать маршруты /add-client и /view-database."

@app.route('/add-client', methods=['POST'])
def add_client():
    data = request.json
    name = data.get('name', '').strip()
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    with open('database.txt', 'a') as f:
        f.write(f"{name}|Тип A|Категория 1\n")
    return jsonify({'message': 'Client added successfully'}), 200

@app.route('/view-database', methods=['GET'])
def view_database():
    try:
        with open('database.txt', 'r') as f:
            data = f.read()
        return data, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    except FileNotFoundError:
        return jsonify({'error': 'Database file not found'}), 404


@app.route('/view-database', methods=['GET'])
def view_database():
    """
    Маршрут для просмотра содержимого database.txt
    """
    try:
        with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
            data = f.read()
        return f"<pre>{data}</pre>", 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    # Запускаем приложение Flask
    app.run(host='0.0.0.0', port=8080)
