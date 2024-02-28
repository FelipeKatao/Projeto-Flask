from controller.usuario_controller import Usuario_controller

class UsuarioService():
    def __init__(self) -> None:
        self.UsuarioController = Usuario_controller()

    def Login(self,NomeUsuario,senha):
        return self.UsuarioController.LoginUsuario(NomeUsuario,senha)