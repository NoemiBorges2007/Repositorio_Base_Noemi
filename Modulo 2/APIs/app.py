from flask import Flask, json, jsonify,request

#criar intancia Flask
app = Flask(__name__)


pedidos = [
   
   {"id":1, 'cliente': 'Noemi', 'prato': 'Strogonoff',"status":"aguardando"},
   {"id":2, 'cliente': 'Thiago', 'prato': 'Churrasco',"status":"aguardando"}
]

proximo_id = 3



#criar rotas

# rota simples

@app.route('/')
def index():
    return " <h1><center>FLASK TESTE DE API</center><H1>"

#rota simples, retornando mensagem

@app.route('/api', methods=['GET'])
def api():
    return jsonify(mensagemDia='bom dia', mensagemTarde=' Boa Tarde' )

#rota Retorna o nome do cliente

@app.route('/cliente/<nome>', methods=['GET'])
def cliente(nome):
  return jsonify(mensagem=f'Bom tarde {nome}')
 
#Rorta Simulando bom Dia em varios idiomas

@app.route('/idioma/<idioma>/<nome>', methods=['GET'])
def idioma(idioma,nome):
   mensagens  = {
      
      'pt': 'Bom dia',
      'en': 'Good Morning',
      'fr': 'Bonjour',
      'it': 'Buongiorno',
      'es': 'Buenos dias'
   }
   mensagens = mensagens.get(idioma)
   return jsonify(mensagem=f'{mensagens}, {nome}')


@app.route('/pedidos', methods=['GET'])
def lista():
   return jsonify(pedidos)

@app.route('/pedidos', methods=['POST'])
def new():
   global proximo_id
   novo_pedido_dados = request.json

   novo_pedido = {
      "id" : proximo_id,
      "cliente" : novo_pedido_dados['cliente'],
      "prato": novo_pedido_dados['prato'],
      "status": "aguardando"
   }

   pedidos.append(novo_pedido)
   proximo_id  += 1

   return jsonify(novo_pedido), 201

# Rota para ATUALIZAR um pedido existente (Update)
# Acessível via método PUT em /pedidos/<id>
@app.route('/pedidos/<int:pedido_id>', methods=['PUT'])
def alterar_pedido(pedido_id):
    # Obtém os dados de atualização da requisição
    dados_atualizacao = request.json
    
    # Procura o pedido que queremos atualizar
    pedido_encontrado = None
    for p in pedidos:
        if p['id'] == pedido_id:
            pedido_encontrado = p
            break
            
    if not pedido_encontrado:
        return jsonify({"erro": "Pedido não encontrado"}), 404

    # Atualiza os dados do pedido.
    # O método .get() é usado para evitar erros se a chave não existir nos dados enviados.
    # Por exemplo, o cliente pode querer atualizar apenas o status.
    pedido_encontrado['cliente'] = dados_atualizacao.get('cliente', pedido_encontrado['cliente'])
    pedido_encontrado['prato'] = dados_atualizacao.get('prato', pedido_encontrado['prato'])
    pedido_encontrado['status'] = dados_atualizacao.get('status', pedido_encontrado['status'])
    
    return jsonify(pedido_encontrado)

# Rota para LISTAR todos os pedidos (Read)
# Acessível via método GET em /pedidos
@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    # jsonify converte nossa lista de dicionários Python para o formato JSON
    return jsonify(pedidos)


# Rota para OBTER um pedido específico pelo ID (Read)
# Acessível via método GET em /pedidos/<id>
@app.route('/pedidos/<int:pedido_id>', methods=['GET'])
def obter_pedido(pedido_id):
    # Procura o pedido na lista usando uma list comprehension
    # É uma forma concisa de criar uma lista.
    pedido_encontrado = [p for p in pedidos if p['id'] == pedido_id]


    if pedido_encontrado:
        # Retorna o primeiro (e único) item encontrado
        return jsonify(pedido_encontrado[0])
    else:
        # Se a lista estiver vazia, o pedido não foi encontrado. Retorna erro 404.
        return jsonify({"erro": "Pedido não encontrado"}), 404
    
    # Rota para APAGAR um pedido (Delete)
# Acessível via método DELETE em /pedidos/<id>
@app.route('/pedidos/<int:pedido_id>', methods=['DELETE'])
def apagar_pedido(pedido_id):
    global pedidos
    # Usamos uma list comprehension para criar uma NOVA lista
    # contendo todos os pedidos, EXCETO aquele com o ID que queremos remover.
    pedidos_filtrados = [p for p in pedidos if p['id'] != pedido_id]


    # Se o tamanho da nova lista for o mesmo da original,
    # significa que nenhum pedido foi removido (não foi encontrado).
    if len(pedidos_filtrados) == len(pedidos):
        return jsonify({"erro": "Pedido não encontrado"}), 404


    # Substituímos a lista original pela nova lista filtrada
    pedidos = pedidos_filtrados


    # Retornamos uma mensagem de sucesso
    return jsonify({"mensagem": "Pedido apagado com sucesso!"})



# exaculta o seviso com derbug criado
if __name__== '__main__':
   app.run(debug=True)  
 