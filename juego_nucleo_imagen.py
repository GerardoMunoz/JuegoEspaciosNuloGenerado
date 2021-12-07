# El juego comienza con una matriz de 2x2, 
# se dibujan los dos vectores columna v1 y v2
# si el rango de la matriz es 2 o 0 gana el primero avise 
# si no entonces los jugadores se van turnando para jugar las dos partes del juego
# En ambas Los jugadores debe dar puntos en la dirección de v1 pero sumando un vector +-u 
#   es decir cada jugados da puntos sobe una recta paralela a gen{v1,v2}
# La primera parte la gana El primer Jugador que encuentre un punto del espacio nulo de la matriz y grita nucleo
# Cuando oprime suma aparece el vector al que es transformado el punto
# la nota baja por cada turno, y el primero qe encuentra de descuentan un turno
# La segunda parte la gana el primer jugador que encuentre un punto que interseca la rectas paralela a nucle que pasa por v1
# Encaso de empate se desempata similar a la segunda parte pero que pasa por v3

# Extender el juego a más dimensiones


# Falta colocar multiplicacion en  el canvas

import tkinter as tk
import numpy as np


def gira90(v):
    return [-v[1],v[0]]

class una_figura():
    def __init__(self):
        self.figura=None
    def __call__(self):
        return self.figura
    

class un_punto(una_figura):
    def __init__(self, v, de_color='black', de_radio=2, **kwargs):
        self.v=v
        self.radio=de_radio
        self.figura=canvas.create_oval(int(escala*(v[0]+width/2))-de_radio,int(escala*((-v[1]+height/2)))-de_radio,int(escala*(v[0]+width/2))+de_radio,int(escala*((-v[1]+height/2)))+de_radio,fill=de_color, **kwargs)
        #print('un_punto.__init__',int(escala*(v[0]+width/2))-de_radio,int(escala*(-(v[1]+height/2)))-de_radio,int(escala*(v[0]+width/2))+de_radio,int(escala*(-(v[1]+height/2)))+de_radio)
        pass

    def __str__(self):
        return '['+str(self.v[0])+', '+str(self.v[1])+']'

    def __getitem__(self,i):
        return self.v[i]

    def np(self):
        return np.array([self[0],self[1]])

    def suma(self,u):
        #print('suma antes',self.v,u)
        self.v=[self.v[0]+u[0],self.v[1]+u[1]]
        #print('suma después',self.v,u)
        canvas.coords(self.figura,int(escala*(self.v[0]+width/2))-self.radio,int(escala*(-(self.v[1])+height/2))-self.radio,int(escala*(self.v[0]+width/2))+self.radio,int(escala*(-(self.v[1])+height/2))+self.radio)
        canvas.update() 

   



class un_segmento(una_figura):
    def __init__(self,v, que_empieza_en=[0,0], de_color='black', **kwargs ):
        #print('un_segmento',v,que_empieza_en,+width/2,height/2)
        self.figura=canvas.create_line( int(escala*(que_empieza_en[0]+width/2)),int(escala*(-(que_empieza_en[1])+height/2)),int(escala*(v[0]+width/2)),int(escala*(-(v[1])+height/2)),fill=de_color, **kwargs)
        #print('un_segmento2',que_empieza_en[0]+width/2,-(que_empieza_en[1])+height/2,v[0]+width/2,-(v[1])+height/2)

class una_recta(una_figura):
    def __init__(self, que_pasa_por, y_también_por=None, en_dirección=None, de_color='black', **kwargs):
        #print('una_recta.__init__', que_pasa_por, y_también_por, en_dirección)
        puntos=[]
        P=que_pasa_por
        if y_también_por  is not None:
            Q=y_también_por
        elif en_dirección is not None:
            Q=[P[0]+en_dirección[0],P[1]+en_dirección[1]]
        bordes=[height/2,width/2,height/2,width/2]
        for i in range(4):
            if P[1] != Q[1] :
                x=P[0] + (P[0] - Q[0])*(bordes[i] - P[1])/(P[1] - Q[1])
            else:
                x=float('inf')
            #print('i,x',i,x,bordes[i])
            if abs(x)<bordes[i]:
                puntos.append([x,bordes[i]])
            P=gira90(P)
            Q=gira90(Q)
            puntos=[gira90(punto) for punto in puntos] 
        #return puntos
        # x_h0=self.calc_x(P,Q,-height/2)
        # x_h1=self.calc_x(P,Q,+height/2)
        # y_w0=self.calc_y(P,Q,-width/2)
        # y_w1=self.calc_y(P,Q,+width/2)
        # if abs(x_h0)<width/2:
        #      puntos.append([x_h0,-height/2])
        # if abs(x_h1)<width/2:
        #      puntos.append([x_h0, height/2])
        # if abs(y_w0)<height/2:
        #      puntos.append([-width/2,y_w0])
        # if abs(y_w1)<height/2:
        #      puntos.append([ width/2,y_w1])
        #print('puntos',puntos)#,x_h0,x_h1,y_w0,y_w1)
        if len(puntos)==2:
            self.figura=un_segmento(puntos[1], que_empieza_en=puntos[0], de_color=de_color, **kwargs)
        
    def calc_x(self,P,Q,y):
        x0,y0=P[0],P[1]
        x1,y1=Q[0],Q[1]
        return x0 + (x0 - x1)*(y - y0)/(y0 - y1)

    def calc_y(self,P,Q,x):
        x0,y0=P[0],P[1]
        x1,y1=Q[0],Q[1]
        return y0 + (x - x0)*(y0 - y1)/(x0 - x1)


def suma_1():
    global cont_1
    jugador_1.suma(deslizador_1.get()*dir)
    cont_1 += 1
    canvas.itemconfig(ccont_1,text=str(cont_1))
    

def suma_2():
    global cont_2
    jugador_2.suma(deslizador_2.get()*dir)
    cont_2 += 1
    canvas.itemconfig(ccont_2,text=str(cont_2))




def dispara_1():
    y=A @ jugador_1.np()
    print('dispara_1',y)
    un_punto(y,de_color=color_1,outline=color_1)
    if np.linalg.norm(y)<0.1:
        una_recta(nu,[0,0],de_color=color_1,width=6)

def dispara_2():
    y=A @ jugador_2.np()
    un_punto(y,de_color=color_2,outline=color_2)
    print('dispara_2',y)
    if np.linalg.norm(y)<0.1:
        una_recta(nu,[0,0],de_color=color_2,width=6)


def dibuja_ejes():
    canvas.create_line(0, height_canvas/2, width_canvas, height_canvas/2, dash=(4, 2))
    canvas.create_line(width_canvas/2,  height_canvas,    width_canvas/2, 0,dash=(4, 2))
    canvas.create_oval(width_canvas/2-2,height_canvas/2-2,width_canvas/2+2,height_canvas/2+2)
    for i in range(0,width_canvas//2,escala):
        canvas.create_line(width_canvas//2-i,  height_canvas/2-4, width_canvas//2-i,  height_canvas/2+4)
        canvas.create_line(width_canvas//2+i,  height_canvas/2-4, width_canvas//2+i,  height_canvas/2+4)
    for i in range(0,height_canvas//2,escala):
        canvas.create_line(width_canvas/2-4, height_canvas//2-i,  width_canvas/2+4,height_canvas//2-i)
        canvas.create_line(width_canvas/2-4, height_canvas//2+i,  width_canvas/2+4,height_canvas//2+i)




dir=np.array([0.5,
              1])
k=-2
A=np.concatenate((dir,k*dir)).reshape(2,2).T
#A=np.array([[1,2],
#            [0.5,1]])
nu=np.array([-k,1])
v=np.array([-0.1,
             0.2])
#usar cramer para encontrar el punto de corte del nucleo con la recta de cada jugador
#  

width=4.1
height=6.1
escala=100
width_canvas  = int(width  * escala)
height_canvas = int(height * escala)

color_1='olive'
color_2='green'

cont_1=0
cont_2=0

pos_1=2#np.zeros(2)
pos_2=-2#np.zeros(2)


master = tk.Tk()
deslizador_1 = tk.Scale(master, from_=-3, to=3, length=600,tickinterval=2, orient=tk.HORIZONTAL, fg=color_1,resolution=0.01)
deslizador_1.pack()
boton_1=tk.Button(master, text='Suma', command=suma_1, fg=color_1).pack()
boton_dispara_1=tk.Button(master, text='Dispara', command=dispara_1, fg=color_1).pack()
deslizador_2 = tk.Scale(master, from_=-3, to=3, length=600,tickinterval=2, orient=tk.HORIZONTAL,fg=color_2,resolution=0.01)
deslizador_2.pack()
boton_2=tk.Button(master, text='Suma', command=suma_2,fg=color_2).pack()
boton_dispara_2=tk.Button(master, text='Dispara', command=dispara_2, fg=color_2).pack()

canvas = tk.Canvas(master, width=width_canvas, height=height_canvas)
canvas.pack()

dibuja_ejes()

ccont_1 = canvas.create_text(width_canvas/4,   20, text='0',fill =color_1)
ccont_2 = canvas.create_text(width_canvas*3/4, 20, text='0',fill =color_2)
#P=un_punto([100,200])
#v=un_segmento([400,50])
#l=una_recta([20,50],[40,50])
P=un_punto(A[:,0])
Q=un_punto(A[:,1])
l1=una_recta(P,Q)
l2=una_recta(v,en_dirección=P, de_color=color_1)
l3=una_recta(-v,en_dirección=P, de_color=color_2)
#print(P.np(),'a')
jugador_1=un_punto(pos_1*dir+v, de_color=color_1, de_radio=3, outline=color_1)
jugador_2=un_punto(pos_2*dir-v, de_color=color_2, de_radio=3, outline=color_2)

#un_segmento([1,1], que_empieza_en=[2,-1], de_color='black' )

#canvas.create_line(325, 0, 85, 600)

# print ('1',canvas.winfo_reqwidth())
# print ('2',canvas.winfo_reqheight())
# print ('3',canvas.winfo_geometry())


tk.mainloop()