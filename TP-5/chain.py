class AbstractHandler:
    def __init__(self, nxt=None):
        self._nxt = nxt

    def handle(self, request):
        handled = self.processRequest(request)
        if not handled and self._nxt:
            self._nxt.handle(request)
        elif not handled:
            print(f"Número {request} no fue consumido.")

    def processRequest(self, request):
        raise NotImplementedError("¡Primero debes implementar esto!")


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


class HandlerPrimos(AbstractHandler):
    def processRequest(self, request):
        if es_primo(request):
            print(f"{self.__class__.__name__} consumió el número primo {request}")
            return True
        return False


class HandlerPares(AbstractHandler):
    def processRequest(self, request):
        if request % 2 == 0:
            print(f"{self.__class__.__name__} consumió el número par {request}")
            return True
        return False


class DefaultHandler(AbstractHandler):
    def processRequest(self, request):
        # Lo manejamos desde AbstractHandler si no hay next, así que no es obligatorio tener esta clase.
        return False


class Cliente:
    def __init__(self):
        self.handler = HandlerPrimos(HandlerPares(None))

    def ejecutar(self):
        for numero in range(1, 101):
            self.handler.handle(numero)


if __name__ == "__main__":
    cliente = Cliente()
    cliente.ejecutar()
