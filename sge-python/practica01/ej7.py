# Escribe un programa que pida una cantidad en euros, a continuación mostrará la cantidad en pesetas

cantidad = float(input("Dame una cantidad (en €):"))
print(f"La peseta ha desaparecido :(, pero:\n{cantidad} € eran {round(cantidad * 166.386)} pesetas.")
