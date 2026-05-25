#<----- Program and logic is under work, please avoid running, in case you do run it use Keyboard interrupt (ctrl+C) to stop it---->
#<----- upon running opens multiple wnidows, working to fix that ------>



import matplotlib.pyplot as plt
import matplotlib.animation as animat
import numpy 
amp = 5 #amplitude
h = 0
x_component = []
y_component = []
for i in range(0,629):
    h = i/100
    x_component.append(amp*numpy.cos(h))
    y_component.append(amp*numpy.sin(h))
fig, areaCanvas = plt.subplots()
areaCanvas.plot(x_component,y_component)#plot points as (x,y) on given canvas (taking it as cartesian plane)
indx=0
def TheFor(indx):
    for k,j in zip(x_component, y_component):
        indx+=1
        areaCanvas.cla()
        areaCanvas.plot(x_component,y_component)
        if indx == (len(x_component)-2):
            k = x_component[0]
            j = y_component[0]
            indx=0
            TheFor(indx)
        areaCanvas.quiver(0, 0, k, j, scale=1, scale_units='xy', angles='xy') 
        plt.pause(0.01)
        plt.draw()
TheFor(indx)
plt.show()
