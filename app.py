from flask import Flask, render_template

app = Flask(__name__)

# Dados fictícios dos produtos
produtos = [
    {"id": 1, "nome": "Jogo 1", "descricao": "Um jogo de aventura emocionante.", "preco": "R$ 59,99"},
    {"id": 2, "nome": "Jogo 2", "descricao": "Um jogo de estratégia envolvente.", "preco": "R$ 89,99"},
    {"id": 3, "nome": "Jogo 3", "descricao": "Ação e adrenalina pura.", "preco": "R$ 69,99"},
    {"id": 4, "nome": "Jogo 4", "descricao": "Mistério e investigação.", "preco": "R$ 79,99"}
]

@app.route('/')
def home():
    return render_template('index.html', produtos=produtos)

# Rota dinâmica para os produtos
@app.route('/produto/<int:id>')
def produto(id):
    if 1 <= id <= 4:  # Certifica-se de que o ID está entre 1 e 4
        return render_template(f'produto{id}.html', produto=produtos[id - 1])
    else:
        return "<h1>Produto não encontrado</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)
