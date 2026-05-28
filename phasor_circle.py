#<----- Program and logic is under work, please avoid running, in case you do run it use Keyboard interrupt (ctrl+C) to stop it---->
#<----- upon running opens multiple wnidows, working to fix that ------>



import matplotlib.pyplot as plt
import matplotlib.animation as animat 
import numpy 
running = True
fig, areaCanvas = plt.subplots()
def onClose(event):
    global running
    if event.key == 'q' or event.key == 'Q': 
      running = False
      plt.close()
      exit()
def onX(event):
    exit()
fig.canvas.mpl_connect('key_press_event', onClose)
fig.canvas.mpl_connect('close_event', onX)
amp= 5 
x_component = []
y_component= []
for i in range(0,629):
    h = i/100
    x_component.append(amp*numpy.cos(h))
    y_component.append(amp*numpy.sin(h))
areaCanvas.plot(x_component,y_component)
indx=0
q = areaCanvas.quiver(0, 0, 0, 0, scale=1, scale_units='xy', angles='xy') 
while running:
    q.remove()
    q = areaCanvas.quiver(0, 0, x_component[indx],y_component[indx], scale=1, scale_units='xy', angles='xy')
    indx+=1
    plt.pause(0.01)
    plt.draw()
    if indx==len(x_component):
        indx-=indx

plt.show()
