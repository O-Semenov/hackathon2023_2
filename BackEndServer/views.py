from flask import jsonify, Blueprint, request
import handlers
stock_blueprint = Blueprint('stock', __name__)

# Пример данных для stock_data
stock_data = {
    'item1': 100,
    'item2': 200,
    # Другие данные из вашего файла config
}

# Пример данных для forklifts
forklifts = [
    {
        'id': 1,
        'sensor_id': 'K1',
        'task_id': 123,
        'status': 'wait'
    },
    {
        'id': 2,
        'sensor_id': 'K2',
        'task_id': 456,
        'status': 'run_to_order'
    },
    # Другие погрузчики и их данные
]


@stock_blueprint.route('/stock', methods=['GET'])
def get_stock():
    result = {
        'stock_data': stock_data,
        'forklifts': forklifts
    }
    return jsonify(result)


@stock_blueprint.route('/script', methods=['POST'])
def get_script():
    data = request.get_json()
    if data:
        handlers.main(data)
        result = {'message': 'Data processed successfully', 'data': data}
        return jsonify(result), 200
    else:
        return jsonify({'message': 'Invalid data'}), 400
