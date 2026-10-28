# 🎮 Breakout: Edición Criolla - Juego Clásico en Pygame 🕹️

# 📋 Descripción

## **Venebreakout** es una versión evolucionada del clásico juego arcade Breakout, desarrollada en Python utilizando la biblioteca Pygame. 

## En esta versión no solo juegas a rebotar la bola y destruir bloques, sino que además cuentas con un **sistema de usuarios y login con contraseñas**, guardado automático de **récords en JSON**, **menú principal**, **menú de pausa**, y **música dinámica** para el menú y el juego.

## ¡Inicia sesión, supera a tus amigos y rompe tus propios récords! 🏆

---

# ✨ Características

## 👤 Sistema de Usuarios y Autenticación
* Registro de usuarios y login seguro con **ocultación de contraseñas** (`*`).
* Cambio de cuenta rápido directamente desde la interfaz.

## 💾 Guardado de Récords Locales
* Persistencia de datos en un archivo `records.json`.
* Cada jugador guarda su puntuación máxima de manera independiente.

## 🎵 Música y Sonido Dinámico
* Música del himno nacional para el menú principal.
* Transición fluida a música de acción al iniciar la partida.

## 🎮 Jugabilidad y Físicas
* Control preciso de la paleta con las teclas **A** y **D**.
* Ángulo de rebote dinámico según la zona donde la bola impacta la paleta.
* Corrección de bordes para evitar que la bola se trabe.

## 🧱 Bloques Variados
* Tres tipos de bloques organizados por niveles y representados con la bandera de Venezuela
.

## ⏸️ Menú de Pausa y Reinicio Rápido
* Pausa la partida en cualquier momento con **ESC**.
* Reinicia la partida al instante presionado **R** tras un Game Over.

---

# 🛠️ Requisitos

## Python 3.x 🐍
## Pygame 📦 (instalable con `pip install pygame`)

---

# 🚀 Instalación y Ejecución

## 1. Clona o descarga este repositorio 📥

## 2. Instala Pygame si aún no lo tienes:

```bash
pip install pygame
```

## 3. Descarga y coloca las imágenes y audios en la misma carpeta del script:

### 🖼️ Recursos de Imagen:
* [![menu_background.png](https://i.postimg.cc/q7Ds9Prz/background.jpg)](https://postimg.cc/7C7JzQfk) **Fondo del Menú** (`menu_background.png`)
* [![background.jpg](https://i.postimg.cc/q7Ds9Prz/background.jpg)](https://postimg.cc/7C7JzQfk) **Fondo del Juego** (`background.png`)
* [![player1.png](https://i.postimg.cc/26cCdx4p/player1.png)](https://postimg.cc/47cCsVLw) **Jugador / Paleta** (`player.png`)
* [![bola.png](https://i.postimg.cc/L6JNC8rS/bola.png)](https://postimg.cc/HVCwjdYv) **Bola** (`bola.png`)
* [![rectangulo.png](https://i.postimg.cc/R041BSbN/rectangulo.png)](https://postimg.cc/Mn3f0SwS) **Bloques Nivel 1** (`rectangulo.png`)
* [![rectangulo2.png](https://i.postimg.cc/150KX7Vg/rectangulo2.png)](https://postimg.cc/SJs9trrq) **Bloques Nivel 2** (`rectangulo2.png`)
* [![rectangulo3.png](https://i.postimg.cc/MKZn09rf/rectangulo3.png)](https://postimg.cc/bdMYp9Pq) **Bloques Nivel 3** (`rectangulo3.png`)

### 🎵 Recursos de Audio:
* `[Venezuela.National.Anthem.8-Bit.Version.Lyrics.mp3](https://github.com/user-attachments/files/34054360/Venezuela.National.Anthem.8-Bit.Version.Lyrics.mp3)
` - Música del menú principal
* `[SLOWER-TEMPO2019-12-11_-_Retro_Platforming_-_David_Fesliyan.mp3](https://github.com/user-attachments/files/34054385/SLOWER-TEMPO2019-12-11_-_Retro_Platforming_-_David_Fesliyan.mp3)
` - Música durante la partida

---

## 4. Ejecuta el juego:

```bash
python main.py
```

---

# 🎮 Controles

| Tecla / Acción | Pantalla | Función |
| :--- | :--- | :--- |
| **A** | Juego | Mover paleta a la izquierda |
| **D** | Juego | Mover paleta a la derecha |
| **ESC** | Juego | Pausar / Reanudar el juego |
| **R** | Game Over | Reiniciar la partida inmediatamente |
| **ESC** | Menús / Login | Volver al menú anterior |
| **TAB** | Login / Cambiar Cuenta | Cambiar entre campos (Usuario / Contraseña) |
| **Clic del Ratón** | Menús | Seleccionar botones e interactuar con la interfaz |

---

# 🧠 ¿Cómo funciona el código?

## 1. **Clases de Sprites (`GameSprite`, `Player`, `Block`)**:
* `GameSprite`: Clase base para manejar la carga de imágenes, posición y dibujado en pantalla.
* `Player`: Maneja los límites de pantalla y movimiento lateral de la paleta.
* `Block`: Subclase para instanciar la rejilla de bloques a destruir.

## 2. **Gestión de Datos (`JSON`)**:
* Las funciones `cargar_datos()` y `guardar_datos()` leen y escriben en `records.json` de forma transparente. Si el usuario rompe su récord personal al perder o ganar, se guarda automáticamente.

## 3. **Máquina de Estados de Juego (`game_state`)**:
* Controla en qué pantalla se encuentra el usuario: `"MENU"`, `"PANTALLA_LOGIN"`, `"PANTALLA_CAMBIAR_CUENTA"`, `"PLAYING"`, `"PAUSE"` o `"GAMEOVER"`.

## 4. **Música e Interfaz Dinámica**:
* La función `reproducir_musica()` aplica un *fadeout* y cambia de pista de audio al navegar entre el menú y la partida.

---

# ¡Gracias por jugar! 🎉✨
