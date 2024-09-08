from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Carregar diálogos do arquivo JSON com codificação UTF-8
def carregar_dialogos(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dialogos = json.load(arquivo)
    return dialogos

dialogos = carregar_dialogos('dialogos.json')

# Responder à entrada do usuário
def responder(entrada):
    entrada = entrada.lower()
    for categoria, respostas in dialogos.items():
        if entrada in respostas:
            return respostas[entrada]
    return "Desculpe, não entendi. Você pode tentar perguntar de outra forma?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensagem_usuario = request.json.get("mensagem")
    resposta = responder(mensagem_usuario)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
