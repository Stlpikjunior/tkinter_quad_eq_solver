
import tkinter_quad_eq_solver as tk
win = tk.Tk()

atext = tk.Label(win,text='koeficient a')
atext.pack()
a = tk.Entry(win)
a.pack()

btext = tk.Label(win,text='koeficient b')
btext.pack()
b = tk.Entry(win)
b.pack()

ctext = tk.Label(win,text='koeficient c')
ctext.pack()
c = tk.Entry(win)
c.pack()

def executor():
   print(a.get(),b.get(),c.get())
   ka = int(a.get())
   kb = int(b.get())
   kc = int(c.get())
   sol = (-kb +(kb**2-(4*ka*kc))**(1/2))/2*ka
   d = kb**2 - (4*ka*kc)
   if d< 0:
       vys = 'nema riesenie'
   elif d == 0:
       vys = 'x1 = '+str(-kb/(2*ka))
   else:
       vys = 'x1 = '+str((-kb +d**(1/2))/2*ka), 'x2 = '+str((-kb - d**(1/2))/(2*ka))
   print( vys)
   restext = tk.Label(win,text=vys)
   restext.pack()


button = tk.Button(win,text='Click me for results',command=executor)
button.pack()


win.mainloop()
