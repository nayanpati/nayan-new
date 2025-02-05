from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, AWS Copilot! Your container is running successfully. 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
