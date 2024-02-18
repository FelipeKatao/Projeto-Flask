

class Compras:
    def __init__(self) -> None:
        self.Carrinho = []

    def CarrinhoUsuario(self):
        self.Carrinho.clear()
        self.Carrinho.append({"Item":"Caderno","valor":4,"Parcelado":None})
        self.Carrinho.append({"Item":"Caneta","valor":2,"Parcelado":3})
        return self.Carrinho