# Aula 04 - API's

## O Que é uma "API"?

     API Significa:
        Application Programaing Interface
        Interface de Progamação de Aplicações

Podemos explicar fazendo uma anoalogia com um garçon que pega o pedido ()
Esse garçom também trás de volta a comida pronta (resposta do pedido da api).

### exemplos: 
    - e-commercer consome uma api dos correios para calcular frente.
    - Aplicativo consome api para buscar provisão do tempo
    - uber consome api para calcular preço, buscar motorista disponíveis.

   Permite que aplicativos diferentes "Conversem"

## Como Funciona?

     Existe város métodos : Rest, Soap, Rpc, web Scocket

     Vamos utilizar  "REST" (Representational State Transfer)

   Rest Utiliza como meio de comunição o HTTP (mesmo meio de sites)    
   HTTP(Hyper Text Transfer Protocol)

     Rest Vias Http utiliza 5 tipos de requisições:
      
      -  Get (pegar/visualizar - muito usado! "Consumido a api")
      -  Post (enviar dados via api)
      -  Put (atualizar algum dado que está no servidor)
      -  Patch (atualizar parte de um conteúdo)
      -  Delet (apagar do servidor)

    * pertinente associar métodos rest com GRUD do banco de dados  