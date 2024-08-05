from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_rectangular_house():
    # Desenha a base da casa
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)  # Cor da base (light grey)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.0)
    glVertex2f(-0.5, 0.0)
    glEnd()

    # Desenha o telhado
    glBegin(GL_TRIANGLES)
    glColor3f(0.6, 0.3, 0.1)  # Cor do telhado (brown)
    glVertex2f(-0.6, 0.0)
    glVertex2f(0.0, 0.4)
    glVertex2f(0.6, 0.0)
    glEnd()

    # Desenha a porta
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.3, 0.1)  # Cor da porta (brown)
    glVertex2f(-0.1, -0.5)
    glVertex2f(0.1, -0.5)
    glVertex2f(0.1, -0.2)
    glVertex2f(-0.1, -0.2)
    glEnd()

    # Desenha a primeira janela
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.6, 0.9)  # Cor da janela (light blue)
    glVertex2f(0.2, -0.4)
    glVertex2f(0.4, -0.4)
    glVertex2f(0.4, -0.2)
    glVertex2f(0.2, -0.2)
    glEnd()

    # Adiciona divisórias à primeira janela
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)  # Cor das divisórias (black)
    glVertex2f(0.3, -0.4)
    glVertex2f(0.3, -0.2)
    glVertex2f(0.2, -0.3)
    glVertex2f(0.4, -0.3)
    glEnd()

    # Desenha a segunda janela
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.6, 0.9)  # Cor da janela (light blue)
    glVertex2f(-0.4, -0.4)
    glVertex2f(-0.2, -0.4)
    glVertex2f(-0.2, -0.2)
    glVertex2f(-0.4, -0.2)
    glEnd()

    # Adiciona divisórias à segunda janela
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)  # Cor das divisórias (black)
    glVertex2f(-0.3, -0.4)
    glVertex2f(-0.3, -0.2)
    glVertex2f(-0.4, -0.3)
    glVertex2f(-0.2, -0.3)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_rectangular_house()
    glutSwapBuffers()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Cor de fundo (branco)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow("Casa Retangular com Porta Grande e Janelões")
init()
glutDisplayFunc(display)
glutMainLoop()