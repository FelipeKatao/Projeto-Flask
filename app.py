from datetime import timedelta
from flask import Flask,request,render_template,session
from servico.usuario_servico import UsuarioService

app_site  = Flask(__name__)
ServicoUsuario = UsuarioService()
app_site.secret_key = 'chave-secreta'
app_site.debug = True
app_site.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=60)

l ="4"
@app_site.route("/")
def login():
    if("usuario" not in session):
        return render_template("paginaCliente.html")
    return "Login já efetuado"

@app_site.post("/login")
def verificar_login():
    Login_status = ServicoUsuario.Login(request.form["login_id"],request.form["login_pass"])
    if(Login_status == "OK"):
        session["usuario"] = request.form["login_id"]
        return "Login feito com sucesso"
    return render_template("paginaCliente.html",status=Login_status)

# Projeto termina aqui 

if(__name__ == '__main__'):
    app_site.run(port=5501,debug=True)    
