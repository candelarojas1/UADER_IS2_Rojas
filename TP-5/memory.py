import os

#*--------------------------------------------------------------------
#* Design pattern memento con múltiples niveles de undo
#*--------------------------------------------------------------------

class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content


class FileWriterUtility:
	def __init__(self, file):
		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:
	def __init__(self):
		self.history = []

	def save(self, writer):
		# Guarda el memento actual al principio
		self.history.insert(0, writer.save())
		# Mantener solo los 4 más recientes
		if len(self.history) > 4:
			self.history.pop()

	def undo(self, writer, pos=0):
		if 0 <= pos < len(self.history):
			writer.undo(self.history[pos])
		else:
			print(f"No hay estado guardado en la posición {pos}")


#*------------------ PRUEBA -------------------

if __name__ == '__main__':
	os.system("clear")  # usa 'cls' si estás en Windows

	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	print("\n1) Se graba contenido y se guarda")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content)
	caretaker.save(writer)

	print("\n2) Se graba contenido y se guarda")
	writer.write("Material adicional I\n")
	print(writer.content)
	caretaker.save(writer)

	print("\n3) Se graba contenido y se guarda")
	writer.write("Material adicional II\n")
	print(writer.content)
	caretaker.save(writer)

	print("\n4) Se graba contenido y se guarda")
	writer.write("Material adicional III\n")
	print(writer.content)
	caretaker.save(writer)

	print("\n5) Se graba contenido y se guarda")
	writer.write("Material adicional IV\n")
	print(writer.content)
	caretaker.save(writer)

	print("\n--- UNDO al estado anterior inmediato (0) ---")
	caretaker.undo(writer, 0)
	print(writer.content)

	print("\n--- UNDO al estado anterior en posición 2 ---")
	caretaker.undo(writer, 2)
	print(writer.content)

	print("\n--- UNDO a una posición inexistente (5) ---")
	caretaker.undo(writer, 5)
