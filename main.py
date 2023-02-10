from flask import Flask, request
import os
import json
import datetime

app = Flask(__name__)

@app.route('/save_json', methods=['POST'])
def save_json():
    file = request.get_json()
    file_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".json"
    with open(os.path.join('json_files', file_name), 'w') as f:
        json.dump(file, f)
    return 'JSON file saved.'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)