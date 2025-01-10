from flask import Flask, render_template
app = Flask(__name__)
# Dados fictícios dos produtos
produtos = [
    {
        "id": 1, 
        "nome": "The Last of Us™ Parte I", 
        "descricao": "Um jogo de aventura emocionante.", 
        "preco": "R$ 59,99",
        "imagem": "https://upload.wikimedia.org/wikipedia/pt/b/be/The_Last_of_Us_capa.png",
        "detalhes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
        "id": 2, 
        "nome": "Marvel's Spider-Man - Jogo de PS4", 
        "descricao": "Um jogo de estratégia envolvente.", 
        "preco": "R$ 89,99",
        "imagem": "https://image.api.playstation.com/vulcan/ap/rnd/202011/0402/C784xeOFo2wViCf4m5bxgoeH.png",
        "detalhes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
        "id": 3, 
        "nome": "Left 4 Dead 2", 
        "descricao": "Ação e adrenalina pura.", 
        "preco": "R$ 69,99",
        "imagem": "https://cdn.awsli.com.br/600x700/1158/1158875/produto/99725402/bbf6d2a624.jpg",
        "detalhes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
        "id": 4, 
        "nome": "Enigma do Medo", 
        "descricao": "Mistério e investigação.", 
        "preco": "R$ 79,99",
        "imagem": "https://upload.wikimedia.org/wikipedia/pt/7/7e/Arte_promocional_de_Enigma_do_Medo.jpg",
        "detalhes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    }
]
@app.route('/')
def home():
    return render_template('index.html', produtos=produtos)
@app.route('/produto/<int:id>')
def produto(id):
    # Find the product with the matching id
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        return render_template('produto.html', produto=produto)
    return "Produto não encontrado", 404
if __name__ == '__main__':
    app.run(debug=True)