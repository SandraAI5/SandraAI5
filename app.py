from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, soy tu asistente AI SandraAI5 💬"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = f"Tu dijiste: {user_message}. Estoy aprendiendo a responder mejor 😊"
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
