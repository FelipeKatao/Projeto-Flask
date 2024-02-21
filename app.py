from flask import Flask,request,render_template
from servico.calculo import Calculo
from servico.compras import Compras

app_site  = Flask(__name__)

_Compras = Compras()

@app_site.route("/usuario/<contexto>") 
def helloWorld(contexto): 
    if(contexto == "compras"): 
        return render_template("index.html",context=str(contexto),Carrinho = _Compras.CarrinhoUsuario())
    if(contexto == "vendas"):
        return render_template("index.html",context=str(contexto),Carrinho = _Compras.CarrinhoUsuario(),QuanidadeVendas =0)
    if(contexto == "cadastro"):
        return render_template("index.html",context=str(contexto),cadastro = True)
    return render_template("index.html",context=str(contexto))
  
@app_site.post("/cad/produto")
def CadProduto():
    Status_erro = []
    if(len(request.form["nome_produto"]) <=10 ):
        Status_erro.append(" O Nome tem menos de 10 caracteres \n")

    if(int(request.form["preco_produto"]) < 0):
            Status_erro.append(" O preço é menor que 0 ")

    if( Status_erro != ""):
        return render_template("index.html",status=Status_erro,cadastro = True)
    else:
        return render_template("index.html",status="Produto cadastrado com sucesso",cadastro = True)

if(__name__ == '__main__'):
    app_site.debug = True 
    app_site.run()  