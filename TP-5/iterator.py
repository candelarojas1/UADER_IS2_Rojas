from collections.abc import Iterable, Iterator

class StringIterator(Iterator):
    def __init__(self, collection: str, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self):
        if self._reverse:
            if self._position < 0:
                raise StopIteration()
            value = self._collection[self._position]
            self._position -= 1
        else:
            if self._position >= len(self._collection):
                raise StopIteration()
            value = self._collection[self._position]
            self._position += 1
        return value

    def __iter__(self):
        return self


class StringCollection(Iterable):
    def __init__(self, cadena: str = "") -> None:
        self._cadena = cadena

    def __iter__(self) -> StringIterator:
        return StringIterator(self._cadena)

    def get_reverse_iterator(self) -> StringIterator:
        return StringIterator(self._cadena, reverse=True)

    def add_char(self, char: str):
        self._cadena += char


if __name__ == "__main__":
    texto = StringCollection("Hola")

    print("Recorrido directo:")
    for c in texto:
        print(c, end=" ")

    print("\nRecorrido inverso:")
    for c in texto.get_reverse_iterator():
        print(c, end=" ")
