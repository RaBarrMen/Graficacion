import pygame as pg
from OpenGL.GL import *
from OpenGL.raw.GLU import gluOrtho2D

class App:

    def _init_(self):
        # Inicializar la ventana de pygame
        pg.init()
        pg.display.set_mode((1200, 800), pg.OPENGL | pg.DOUBLEBUF)
        pg.display.set_caption("Tablero Isométrico OpenGL con Líneas")
        self.clock = pg.time.Clock()  # Controla el frame rate

        # Iniciar OpenGL
        glClearColor(1, 1, 1, 1)  # Color de fondo

        # Configuración de la proyección
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, 1200, 0, 800)  # Coordenadas ortogonales 2D
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.mainLoop()

    def draw_line(self, x1, y1, x2, y2):
        """Dibuja una línea entre dos puntos (x1, y1) y (x2, y2)."""
        glBegin(GL_LINES)
        glColor3f(0, 0, 0)  # Color negro para las líneas
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

    def draw_grid(self, rows, cols, tile_size):
        """Dibuja un grid isométrico usando líneas en lugar de tiles completos."""
        origin_x = 600  # Coordenada X central de la ventana
        origin_y = 400  # Coordenada Y central de la ventana

        for row in range(rows):
            for col in range(cols):
                x = origin_x + (col - row) * (tile_size / 2)
                y = origin_y + (col + row) * (tile_size / 4)

                # Dibuja las líneas para formar el tile
                if col < cols - 1:  # Línea hacia la derecha
                    x_next = origin_x + ((col + 1) - row) * (tile_size / 2)
                    y_next = origin_y + ((col + 1) + row) * (tile_size / 4)
                    self.draw_line(x, y, x_next, y_next)

                if row < rows - 1:  # Línea hacia abajo
                    x_next = origin_x + (col - (row + 1)) * (tile_size / 2)
                    y_next = origin_y + (col + (row + 1)) * (tile_size / 4)
                    self.draw_line(x, y, x_next, y_next)

    def mainLoop(self):
        running = True
        while running:
            # Checar eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # Refrescar pantalla
            glClear(GL_COLOR_BUFFER_BIT)

            # Dibujar el tablero isométrico con líneas
            self.draw_grid(10, 10, 50)

            # Actualizar la pantalla
            pg.display.flip()

            # Timing 60 cuadros por segundo
            self.clock.tick(60)
        self.quit()

    def quit(self):
        pg.quit()

if __name__ == "__main__":
    myApp = App()