# 🎮 Breakout - Juego Clásico en Pygame 🕹️

# 📋 Descripción

Breakout es un juego arcade clásico donde controlas una paleta para rebotar una bola y destruir todos los bloques 🧱. Está desarrollado en Python con la biblioteca Pygame.

¡Diviértete rompiendo bloques y superando tus récords! 🏆

# ✨ Características
🎯 Control preciso de la paleta con teclas A y D

⚽ Bola con rebotes realistas en paleta, bloques y paredes

🟨🟦🟥 Tres tipos de bloques con imágenes personalizadas

🏅 Sistema de puntuación que aumenta al romper bloques

🎉 Mensajes de victoria y derrota con opción para reiniciar

🧩 Código modular y fácil de entender

# 🛠️ Requisitos
Python 3.x 🐍

Pygame (instalable con pip install pygame) 📦

# 🚀 Instalación y Ejecución

Clona o descarga este repositorio 📥

Instala Pygame si no lo tienes:

bash
pip install pygame
Coloca las imágenes en la misma carpeta que el script:

background.png 🌌

player1.png 🎮

bola.png ⚽

victoryplayer1.png 🏆

rectangulo.png, rectangulo2.png, rectangulo3.png 🧱

Ejecuta el juego:

bash
python breakout.py
# 🎮 Controles

## Tecla	Acción
A	Mover paleta a la izquierda 👈
D	Mover paleta a la derecha 👉
R	Reiniciar juego 🔄
Cerrar ventana	Salir del juego ❌
📂 Estructura del proyecto
text
breakout/
├── breakout.py          # Código principal
├── background.png       # Fondo del juego
├── player1.png          # Paleta
├── bola.png             # Bola
├── victoryplayer1.png   # Imagen de victoria
├── rectangulo.png       # Bloque tipo 1
├── rectangulo2.png      # Bloque tipo 2
├── rectangulo3.png      # Bloque tipo 3
└── README.md            # Documentación
🧠 Cómo funciona el código
GameSprite: Clase base para sprites

Player: Controla la paleta y su movimiento

Block: Representa los bloques a destruir

La bola rebota en paleta, bloques y bordes

El juego termina si la bola cae o si destruyes todos los bloques

Reinicia con la tecla R para jugar otra vez 🔁

📬 Contacto
¿Preguntas o sugerencias? Escríbeme a [tu-email@ejemplo.com] ✉️

¡Gracias por jugar! 🎉✨
