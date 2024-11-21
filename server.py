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
    """
    Маршрут для добавления клиента в файл database.txt
    """
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'success': False, 'error': 'Имя клиента обязательно'}), 400

    try:
        # Добавляем запись в файл
        with open(DATABASE_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{name}|Тип A|Категория 1\n")
        return jsonify({'success': True, 'message': 'Клиент успешно добавлен!'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

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
