from flask import Flask, jsonify, render_template
import threading
import requests
import time

app = Flask(__name__)

# A dictionary to hold the status of each endpoint
endpoints_status = {
    "https://0560bfbf6f6f420999a20420a6208cfa.i.tgcloud.io/": "Unknown",
    "https://fitlab-dulv4fp2kq-uw.a.run.app/": "Unknown"
}
def monitor_endpoint(url):
    while True:
        try:
            response = requests.get(url, timeout=60)
            if response.status_code == 200:
                endpoints_status[url] = "Up"
            else:
                endpoints_status[url] = "Down"
        except requests.exceptions.RequestException:
            endpoints_status[url] = "Error"
        time.sleep(60)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirected')
def redirected():
    return 'You have been redirected!'

@app.route('/monitor')
def display_status():
    return render_template('status.html', endpoints=endpoints_status)

if __name__ == '__main__':
    for url in endpoints_status.keys():
        thread = threading.Thread(target=monitor_endpoint, args=(url,))
        thread.daemon = True
        thread.start()
    app.run(host='0.0.0.0', port=8080)

