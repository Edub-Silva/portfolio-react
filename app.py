# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import time
import random

app = Flask(__name__)

# Simulação de base de dados para o "Cérebro" do SaaS
DATABASE_MOCK = {
    "vendas": "O volume de vendas cresceu 15% após a última atualização de marketing.",
    "lucro": "A margem líquida atual é de 22%, otimizada pela redução de custos em servidores Cloud.",
    "usuarios": "Identificamos um novo padrão de uso: a maioria dos usuários acessa entre 14h e 18h.",
}

@app.route('/')
def index():
    # Certifique-se de que o arquivo 'index.html' esteja dentro de uma pasta chamada 'templates'
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Dados não fornecidos"}), 400

    query = data.get('query', '').lower()
    
    # Simula latência de processamento de IA (UX: feedback visual de carregamento)
    time.sleep(1.5)
    
    # Lógica de resposta dinâmica
    if "venda" in query or "lucro" in query:
        response = f"{DATABASE_MOCK['vendas']} {DATABASE_MOCK['lucro']}"
    elif "usuário" in query or "pessoa" in query or "usuario" in query:
        response = DATABASE_MOCK["usuarios"]
    else:
        responses = [
            "Os algoritmos sugerem foco na retenção de clientes no próximo ciclo.",
            "Análise concluída: A performance atual está 5% acima da média do setor.",
            "Detectamos oportunidade de expansão baseada no seu tráfego atual."
        ]
        response = random.choice(responses)

    return jsonify({
        "status": "success",
        "message": response
    })

if __name__ == '__main__':
    # Rodando o servidor
    app.run(debug=True, port=5000)