# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 21:04:59 2025

@author: toora
"""

# Installing custom modules and use them from their documentation
from prettytable import PrettyTable

table= PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align="l"
print(table)
