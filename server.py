@app.route('/add-client', methods=['POST'])
def add_client():
    data = request.json
    name = data.get('name')
    client_type = data.get('type', 'Тип B')  # Новое статическое значение по умолчанию
    client_category = data.get('category', 'Категория 2')  # Новое статическое значение по умолчанию

    if not name:
        return jsonify({'success': False, 'error': 'Name is required'}), 400

    try:
        with open(DATABASE_FILE, 'a', encoding='utf-8') as f:
            # Запись с фиксированным type и category
            f.write(f"{name}|{client_type}|{client_category}\n")
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
