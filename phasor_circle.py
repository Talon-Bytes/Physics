#<----- Program and logic is under work, please avoid running, in case you do run it use Keyboard interrupt (ctrl+C) to stop it---->
#<----- upon running opens multiple wnidows, working to fix that ------>



import matplotlib.pyplot as plt
import matplotlib.animation as animat 
import numpy 
amp= 5 
x_component = []
y_component= []
for i in range(0,629):
    h = i/100
    x_component.append(amp*numpy.cos(h))
    y_component.append(amp*numpy.sin(h))
fig, areaCanvas = plt.subplots()
areaCanvas.plot(x_component,y_component)
indx=0
q = areaCanvas.quiver(0, 0, 0, 0, scale=1, scale_units='xy', angles='xy') 
while True:
    q.remove()
    q = areaCanvas.quiver(0, 0, x_component[indx],y_component[indx], scale=1, scale_units='xy', angles='xy')
    indx+=1
    plt.pause(0.01)
    plt.draw()
    if indx==len(x_component):
        indx-=indx
plt.show()
