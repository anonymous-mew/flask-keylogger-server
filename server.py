from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def receive_log():
    log_data = request.form.get('log')
    if log_data:
        with open("received_logs.txt", "a", encoding="utf-8") as f:
            f.write(log_data + "\n")
    return "OK", 200

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

