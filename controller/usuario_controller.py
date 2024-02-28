from repo.usuario_repository import Usuario_repository

class Usuario_controller():
    def __init__(self) -> None:
        self.UsuarioRepo = Usuario_repository()

    def LoginUsuario(self,usuario,senha):
        if(len(usuario) >=10 or len(senha) >=8):
            return self.UsuarioRepo.InfoUsuario(usuario,senha)
        return "Usuario ou senha incorretos."