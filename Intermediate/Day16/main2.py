

# Installed PrettyTable package

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", [
                 "Pikachu", "Squirtle", "Charmander"], align="l", valign="m")
table.add_column("Type", ["Electric", "Water", "Fire"], align="l", valign="m")


print(table)
