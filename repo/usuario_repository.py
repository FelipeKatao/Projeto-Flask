

class Usuario_repository():
    def __init__(self) -> None:
        self.DadosUsuario = {"Usuario":"Felipe_fornecedor","Senha":"12345678"}

    def InfoUsuario(self,usuario,senha):
        if(usuario == self.DadosUsuario["Usuario"] and senha == self.DadosUsuario["Senha"]):
            return "OK"
        return "Usuario ou senha incorretos."
