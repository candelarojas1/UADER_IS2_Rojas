class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, emitted_id):
        for observer in self._observers:
            observer.update(emitted_id)


class IDObserver:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, emitted_id):
        if self.observer_id == emitted_id:
            print(f"Observer {self.observer_id} recibió su ID: {emitted_id}")


if __name__ == "__main__":
    # Crear el sujeto
    subject = Subject()

    # Crear 4 observers con IDs específicos
    obs1 = IDObserver("X123")
    obs2 = IDObserver("Y456")
    obs3 = IDObserver("Z789")
    obs4 = IDObserver("W000")

    # Suscribirse al subject
    subject.attach(obs1)
    subject.attach(obs2)
    subject.attach(obs3)
    subject.attach(obs4)

    # Emitir 8 IDs (al menos 4 que coincidan)
    ids_a_emitir = ["X123", "ABCD", "W000", "ZZZZ", "Y456", "LMNO", "Z789", "QWER"]

    for id_actual in ids_a_emitir:
        print(f"\nEmitiendo ID: {id_actual}")
        subject.notify(id_actual)
