from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def receive_log():
    log_data = request.form.get('log')
    if log_data:
        with open("received_logs.txt", "a", encoding="utf-8") as f:
            f.write(log_data + "\n")
    return "OK", 200

if __name__ == '__main__':
    app.run()
