import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state + manejo de memorias
#*--------------------------------------------------------------------

class State:
	def scan(self):
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))


class AmState(State):
	def __init__(self, radio):
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate


class FmState(State):
	def __init__(self, radio):
		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate


class Radio:
	def __init__(self):
		self.fmstate = FmState(self)
		self.amstate = AmState(self)
		self.state = self.fmstate

		# Memorias predefinidas (pueden ser de AM o FM)
		self.memories = [
			("M1", "FM", "101.1"),
			("M2", "AM", "1320"),
			("M3", "FM", "99.5"),
			("M4", "AM", "1410")
		]
		self.mem_pos = 0

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		# Primero sintoniza estaciones normales del estado actual
		self.state.scan()

		# Luego sintoniza memoria
		memoria = self.memories[self.mem_pos]
		print("Sintonizando... Memoria {} {} {}".format(memoria[0], memoria[1], memoria[2]))

		# Mover al siguiente slot de memoria
		self.mem_pos += 1
		if self.mem_pos == len(self.memories):
			self.mem_pos = 0


if __name__ == "__main__":
	os.system("clear")  # usá 'cls' en Windows si da error

	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
	actions *= 2

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()
