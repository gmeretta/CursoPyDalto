# import modulo_saludar as modgreet # namespace

from funciones_buenas.modulo_saludar import saludar as saludar_normal, saludar2 # importo sólo una función
import funciones_buenas.modulo_saludar as m_saludar

print(saludar_normal("Lucas"))
print(saludar2("Gustavo"))

print(dir(m_saludar))
print(m_saludar.__name__)

print(__name__)

import sys

print(sys)
print(sys.builtin_module_names) # creados en C

# Ver enrutamiento(5:45:00)
print(sys.path)