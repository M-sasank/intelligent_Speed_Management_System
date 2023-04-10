from flask import Flask
import os
import json
import time


def writeJSON():
    dict = {}
    base = os.path.join(os.getcwd(), 'results')
    files = os.listdir(base)
    for i in range(len(files)):
        folder = os.path.join(base, files[i])
        files1 = os.listdir(folder)
        req_file = os.path.join(folder, files1[1])
        with open(req_file, 'r') as f:
            data = f.read()
            dict["size"] = len(files)
            s = {"vis": data}
            x = time.time()
            y = time.ctime(x)
            s["time"] = y
            dict["test" + str(i)] = s
    return dict


app = Flask(__name__)


@app.route('/api', methods=['GET'])
def request():
    return json.dumps(writeJSON())


if __name__ == '__main__':
    app.run(debug=True)
