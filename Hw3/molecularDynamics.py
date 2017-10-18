import matplotlib.pyplot as plt
from scipy.special import erfinv
from matplotlib.animation import FuncAnimation
import numpy as np
import random
import math
import copy

##################### SETTINGS ########################
show_dist = False
uniform_v = False
random_position = False
uniform_position = True
boltz_v = True
print_u = True
print_t = True
tracking = False
temp_control = False
grad_temp = True
### init configuration

## time ##
t = 50
delta_t = .01
current_time = 0

## num of pieces ##
num_pieces = 16

## settings for evenly space ##
lattice = 4
if uniform_position is True:
    num_pieces = lattice ** 2

### number configuation
length = 10
limit = 3
ptemp = 0.1
temp_range = np.linspace(ptemp, ptemp / 10 + ptemp, 100)
ulimit = 1

### Constant
kb = 1


###################### SETTINGS END ###################

### plotting stuff ### = plt.figure()
fig, ax = plt.subplots()
#fig, ax2 = plt.subplots()
xdata, ydata, vx, vy, Fx, Fy = [], [], [], [], [], []
xbefore, ybefore = [], []
tracker = []
energy = []
kinE = []
ln, = ax.plot([], [], 'ro', animated=True)
#ln2, = ax2.plot([], [], 'r--', lw=2, animated=True)
#####################


def calU(radius):
    u = 0
    for i in radius:
        for j in i:
            u +=  -1.0 / j ** 6 + 1.0 / j ** 12
  #  print u
    return u

### calculate radius for all 9 
def movePieces():
    global xbefore, ybefore, xdata, ydata, vx, vy, current_time
    current_time = current_time + delta_t
    print "Time: ", current_time
    tempx = []
    tempy = []
    for i in range(len(xdata)):
        tempx.append(xdata[i])
        tempy.append(ydata[i])
        
        
        xdata[i] = 2 * xdata[i] - (xbefore[i]) + Fx[i] * (delta_t ** 2)
        ydata[i] = 2 * ydata[i] - (ybefore[i]) + Fy[i] * (delta_t ** 2)

        vx[i] = (xdata[i] - xbefore[i])
        vy[i] = (ydata[i] - ybefore[i])

      #  print vx[i]
        if xdata[i] - xbefore[i] > length - 1:
            vx[i] = vx[i] - 2 * length
            
        if xdata[i] - xbefore[i] < -length + 1:
            vx[i] = vx[i] + 2 * length

        if ydata[i] - ybefore[i] > length - 1:
            vy[i] = vy[i] - 2 * length

        if ydata[i] - ybefore[i] < -length + 1:
            vy[i] = vy[i] + 2 * length
        
        vx[i] = vx[i] / delta_t / 2
        vy[i] = vy[i] / delta_t / 2
        
        xbefore[i] = tempx[-1]
        ybefore[i] = tempy[-1]
        
        vbefore = math.sqrt(sum((np.array(vx) ** 2 + np.array(vy) ** 2)) / num_pieces)
   
    if vbefore ** 2 / 3 != ptemp and temp_control:
       # print vbefore ** 2 / 3
        vafter = math.sqrt(ptemp * 3)
        r = np.sqrt((np.array(xdata) - np.array(xbefore)) ** 2 + (np.array(ydata) - np.array(ybefore)) ** 2 )

        xbefore = np.array(xbefore) + (np.array(xdata) - np.array(xbefore)) * ((vbefore - vafter) * delta_t / r)
        ybefore = np.array(ybefore) + (np.array(ydata) - np.array(ybefore)) * ((vbefore - vafter) * delta_t / r)
        xbefore = xbefore % length
        ybefore = ybefore % length

    xdata = np.array(xdata) % length
    ydata = np.array(ydata) % length
    calculate()
    return xdata, ydata

def calculatePotential(x, r):
    return 4 * (6 * x / (r ** 8) - 12 *x / (r ** 14))

def calForce(radius, xx, yy):
    for i in range(len(radius)):
        x = 0
        y = 0
        for j in range(len(radius[i])):
            r = radius[i][j]
            Vtruncx = calculatePotential(xx[i][j], 3.0)
            Vtruncy = calculatePotential(yy[i][j], 3.0)

            x += calculatePotential(xx[i][j], r) - Vtruncx
            y += calculatePotential(yy[i][j], r) - Vtruncy
        Fx[i] = x
        Fy[i] = y
    return Fx, Fy

def calRadius(index, x1, y1, x2, y2, radius, xx, yy):
    offx = x2 + length
    offy = y2 + length
    for i in range(3):
        for j in range(3):
            r = math.sqrt((offx - x1) ** 2 + (offy - y1) ** 2)
            if  r < limit:
                radius[index].append(r)
              #  print radius   
                xx[index].append(offx - x1)
                yy[index].append(offy - y1)
            offy = (offy - length)
        offx = (offx - length)
        offy = y2 + length
  #  print xx[index], yy[index], r, index
   # print radius, xx, yy
    return radius, xx, yy
    #print F
   # print radius

##initializing 
def initRadius():
    xx = []
    yy = []
    radius = []
    for i in xdata:
        radius.append([])
        xx.append([])
        yy.append([])
    return radius, xx, yy

##Calculating radius
def calculate():
    radius, xx, yy = initRadius()
    kin = 0
    for i in range(len(xdata)):
        x1 = xdata[i]
        y1 = ydata[i]
        kin += (vx[i] ** 2 + vy[i] ** 2) / 4
        for j in range(len(xdata)):
            if i != j:
                radius, xx, yy = calRadius(i, x1, y1, xdata[j], ydata[j], radius, xx, yy)
    Fx, Fy = calForce(radius, xx, yy)
    u = calU(radius)
    if print_u == True:
        print "Energy: ", kin + u
        energy.append(u)
        kinE.append(kin)
    if print_t == True:
        print "Temperature: ", kin / num_pieces / 3 * 4
    return u, kin

def check(x, y, xdata, ydata):
    for i in range(len(xdata)):
        if math.sqrt((x - xdata[i]) ** 2 + (y - ydata[i]) ** 2) > 0.5:
           # print x, y
            return x, y

def boltz(t):
    return erfinv(random.random() * 2 - 1) * math.sqrt(2 * kb *t)

def putPieces():
    global xdata, ydata, Fx, Fy, vx, vy, xbefore, ybefore, ulimit, energy, kinE
    global current_time
    print "initializing"
    u = ulimit + 1
    dis = []
    for i in range(num_pieces):
        Fx.append(0)
        Fy.append(0)

    if boltz_v == True:
        for i in range(num_pieces):
            x = boltz(ptemp)
            y = boltz(ptemp)
            vx.append(x)
            vy.append(y)

    if show_dist == True:
        plt.hist(np.array(vx) ** 2 + np.array(vy) ** 2 / 3 / num_pieces, bins='auto')
        plt.show()

    if uniform_v is True:
        for i in range(length):
            for j in range(length):
                vx.append(i * 0.95)
                vy.append(j * 0.95)
    
    if random_position is True:
        while u > ulimit or u < -1 * ulimit:
            xdata = []
            ydata = []
            ybefore = []
            xbefore = []
            energy = []
            kinE = []
            for i in range(num_pieces):
                x = random.random()
                y = random.random()
                xbefore.append(x * length)
                ybefore.append(y * length)
                xdata.append(xbefore[i] + vx[i] * delta_t)
                ydata.append(ybefore[i] + vy[i] * delta_t)
            u, kin = calculate()
    counter = 0
    if uniform_position is True:
        for i in np.linspace(1, 9, lattice):
            for j in np.linspace(1, 9, lattice):
                xbefore.append(i)
                ybefore.append(j)
                xdata.append(xbefore[-1] + vx[counter] * delta_t)
                ydata.append(ybefore[-1] + vy[counter] * delta_t)
                counter = counter + 1
      #  print vx, vy
    #print xdata, ydata
    u, kin = calculate()
   # print u, kin, "<-------------------", u + kin
## updating a frame
def update(frame):
    xdata, ydata = movePieces()
    ln.set_data(xdata, ydata)
    
    return ln,

## constructing the anime
def anime():
    ani = FuncAnimation(fig, update, frames=np.linspace(0, t, t / delta_t), 
            init_func=setup, blit=True, repeat=False, interval=10)

    plt.show()
    if print_u:
        plt.plot(np.array(energy))
        plt.plot(kinE)
        plt.plot(np.array(energy[:-1]) + np.array(kinE[1:]))
   # print energy
        plt.show()
## setting up the board
def setup():
    ax.set_xlim(0, length)
    ax.set_ylim(0, length)
    return ln,

def main():
    putPieces()
    anime()

if __name__ == "__main__":
  main()