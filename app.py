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
    return render_template("index.html",context=str(contexto))
  
@app_site.post("/teste")
def a():   
    valor = 0 
    return str(valor) 
   
@app_site.get("/dados/<dados>") 
def ObterDados(dados): 
    nome =request.args.get("nome")
    if nome != None:
        return {"Nome":nome}
    return "Nome não cadastrado!"

@app_site.get("/funcao/somar/<numero>")
def Somar(numero):
    _calc = Calculo()
    return {"ValorDaRemesa":str(_calc.Soma(int(request.args.get("v1")),int(request.args.get("v2"))))}

if(__name__ == '__main__'):
    app_site.debug = True 
    app_site.run()  