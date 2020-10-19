from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Процедура инициализации
def init():
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.5, 0.5, 0.5, 1.0) # Серый цвет для первоначальной закраски
        gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
        global filled
        filled = 1

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
        global filled
        if key == b'\x1b':
                sys.exit(0)
        if key == b' ':
                filled = 1 - filled
        glutPostRedisplay()         # Вызываем процедуру перерисовки

# Процедура рисования
def draw(*args, **kwargs):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
        glRotated(1,1,1,1)
        global filled
        if filled == 1:
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        R1 = 0.5
        for i in range(21):

                glBegin(GL_QUAD_STRIP)

                glColor3f(1-i/23, 0.1 + i/27, 1/2 - i/28)
                for k in range(21):
                        z = R1*sin(2*pi*k/20)
                        r = 0.3
                        glVertex3d( (R1+r*cos(2*pi*k/20)) * cos(2*pi*i/20), \
                                 (R1+r*cos(2*pi*k/20)) * sin(2*pi*i/20), r*sin(2*pi*k/20))
                        glVertex3d( (R1+r*cos(2*pi*k/20)) * cos(2*pi*(i+1)/20), \
                                 (R1+r*cos(2*pi*k/20)) * sin(2*pi*(i+1)/20), r*sin(2*pi*k/20))

                glEnd()

        glutSwapBuffers()           # Меняем буферы
        glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL Second Program!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных клавиш
glutKeyboardFunc(keyboardkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()
