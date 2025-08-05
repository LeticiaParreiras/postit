#Color.py
import random
colors = {"amarelo": "yellow2",
 "rosa": "maroon2",
 "roxo" : "purple2",
 "azul" : "skyblue2",
 "verde" : "green3",
 "laranja" : "orange2",
 "branco"  :"snow"}

def choose_random_color():
    """Escolhe uma cor aleatoria."""
    return random.choice(list(colors.values()))