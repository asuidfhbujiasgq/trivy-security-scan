from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, este es un test de seguridad con Trivy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
