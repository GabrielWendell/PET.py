'''
This is the core of Lotka_Volterra package version 2.0 whose objective is to simulate the model 
complex predator-prey dynamics through systems of differential equations. 

These systems sometimes exhibit chaotic behavior provided that we have three or more species interacting. 
By simply increasing the dimensionality from two to three we introduce the possibility of chaos.

Rocha, G. W. C. (2021)
'''

# ---------------------------------------------------------------------------------------------------------------------
import matplotlib.animation as animation
from IPython.display import HTML
import matplotlib.pyplot as plt
from scipy import integrate
import numpy as np

plt.rcParams['font.family'] = 'monospace'
plt.rcParams['font.size'] = 15


# ---------------------------------------------------------------------------------------------------------------------
def opt_plot():
    """
    This function helps to improve the aesthetics of the graphics!
    """
    # plt.style.use('dark_background')
    plt.grid(True, linestyle=':', color='0.50')
    plt.minorticks_on()
    plt.tick_params(axis='both',which='minor', direction = "in",
                        top = True,right = True, length=5,width=1,labelsize=15)
    plt.tick_params(axis='both',which='major', direction = "in",
                        top = True,right = True, length=8,width=1,labelsize=15)




# ---------------------------------------------------------------------------------------------------------------------
'''
THE CLASSIC LOTKA-VOLTERRA MODEL (TWO-SPECIES):
Model complex predator-prey dynamics through systems of differential equations. These systems sometimes exhibit chaotic 
behavior provided that we have three or more species interacting. By simply increasing the dimensionality from two to 
three we introduce the possibility of chaos.
'''
def dX_dt_2Species(X, t, a,b,c,d):
    '''
    :param X:
    :param t:
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    '''
    return np.array([a * X[0] - b * X[0] * X[1],
                  -c * X[1] + d * X[0] * X[1]])

def LotkaVolterra(X0, params, t):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]

    if len(params) != 4:
        print("Params must be of length four!")

    sol = integrate.odeint(dX_dt_2Species, X0, t, args = (a, b, c, d))
    plt.plot(t, sol[:, 0], color = 'blue', label = 'Prey')
    plt.plot(t, sol[:, 1], color = 'red', label = 'Predator')
    plt.legend(loc = 'best')
    plt.xlabel('Time')
    plt.ylabel('Population')
    opt_plot()
    plt.show()
    plt.rcParams['animation.writer'] = 'avconv'

    def random_ic(scalefac=2.0):  
        '''
        Generate initial condition
        '''
        return scalefac * (0.5 * abs(np.random.randn(2)) + 1)

    nlines = 10
    linedata = []
    for ic in [random_ic() for i in range(nlines)]:
        linedata.append(integrate.odeint(dX_dt_2Species, ic, t, args = (a, b, c, d)))

    fig = plt.figure()
    ax = plt.axes(xlim = (0, 30), ylim = (0, 30))
    line, = ax.plot([], [], 'ko', markersize = 5, zorder = 10)
    traj, = ax.plot([], [], 'ro', markersize = 1, zorder = 2)
    npts = len(linedata[0][:, 0])

    def init():
        line.set_data([], [])
        traj.set_data([],[])
        return line, traj

    def animate(i):
        traj.set_data([l[0:i-1:3, 0] for l in linedata], [l[0:i-1:3, 1] for l in linedata])
        line.set_data([l[i, 0] for l in linedata], [l[i, 1] for l in linedata])
        return line, traj

    anim = animation.FuncAnimation(fig, animate, init_func = init,
                                   frames = npts, interval = 15, blit = True)

    plt.title('Lotka-Volterra Trajectories')
    plt.xlabel('Prey')
    plt.ylabel('Predator')
    plt.xlim(0,20)
    opt_plot()
    plt.show()

    return anim


def TwoSpeciesModel():
    params = [0.8, 0.1, 1.3, 0.2]
    t = np.linspace(0, 15, 1000)  
    X0 = np.array([10, 5])  
    LotkaVolterra(X0, params, t)
    
    
# ---------------------------------------------------------------------------------------------------------------------
'''
THREE-PLUS SPECIES LOTKA-VOLTERRA MODEL:
animals live in eco-systems where animals may be either predators or prey. There may even be more complication animal 
relationships like symbiosis or scavenger-behavior. The Hastings model is a three dimensional Lotka-volterra model where 
rates of feeding are porportional to ratios of populations. Upon choosing certain parameter values the trajectories can 
generate strange attractors and thus exhibit chaos. We see below the classic tea-cup shape of the strange attractor that 
appears for this model.
'''

def dX_dt_3Species(X, t, a,b,c,d,e,f):
    
    return np.array([X[0]*(1 - X[0] - X[1] - X[2]),
                     X[1]*(-a + b * X[0] - c*X[2]),
                     X[2]*(-d + e*X[0] + f*X[1])])

def ThreeSpecies(X0, params, t):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    e = params[4]
    f = params[5]

    if len(params) != 6:
        print("Params must be of length four!")

    sol = integrate.odeint(dX_dt_3Species, X0, t, args = (a, b, c, d, e, f), rtol = 10**-8)

    plt.plot(t, sol[:, 0], 'b', label = 'Prey')
    plt.plot(t, sol[:, 1], 'g', label = 'Predator')
    plt.plot(t, sol[:, 2], 'r', label = 'Super-Predator')
    plt.legend(loc = 'best')
    plt.xlabel('Time')
    plt.ylabel('Population')
    opt_plot()
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot(sol[:, 0], sol[:, 1], sol[:, 2], 'b')
    ax.grid()
    ax.set_xlabel('Prey')
    ax.set_ylabel('Predator')
    ax.set_zlabel('Super-Predator')
    ax.set_title('Three Species Model')
    opt_plot()
    plt.show()
    plt.rcParams['animation.writer'] = 'avconv'


def ThreeSpeciesModel():
    ## aa = -5 bb = 25 cc = 0.0400 dd =2 ee = 0.65 ff=1.3
    params = [5, 32, 0.04, 2, 0.5, 1.3]
    t = np.linspace(0, 500, 100000)  
    X0 = np.array([0.1, 0.1, 0.1])
    
    ThreeSpecies(X0, params, t)
    
    
# ---------------------------------------------------------------------------------------------------------------------
'''
HASTING MODEL:
The Hastings model is an extension of the Lotka-Volterra model found above to three species. In addition the coeffecients 
are now predation rates controlled by the relative size of the populations - afterall, a predator can only hunt if there 
is prey to be found.
'''
def dX_dt_Hasting(X, t, a, b, c , d, e ,f):
    

    return np.array([ X[0]*(1 - X[0]) - a*(X[0]*X[1])/(1 + b*X[0]),
                    (-e*X[1] + (a*X[0]*X[1])/(1 + b*X[0]) - c*(X[2]*X[1])/(1 + d*X[1])),
                    - f*X[2] + c*(X[1]*X[2])/(1 + d*X[1])])


# Animation function.  This will be called sequentially with the frame number


def Hastings(X0, params, t, animate = False, graph = True):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]
    e = params[4]
    f = params[5]

    if len(params) != 6:
        print("Params must be of length six!")

    sol = integrate.odeint(dX_dt_Hasting, X0, t, args = (a, b, c, d, e, f), rtol = 10**-8)
    plt.figure()
    plt.plot(t[50:-6000], sol[50:-6000, 0], 'b', label = 'Prey')
    plt.plot(t[50:-6000], sol[50:-6000, 1], 'g', label = 'Predator')
    plt.plot(t[50:-6000], sol[50:-6000, 2], 'r', label = 'Super-Predator')
    plt.legend(loc = 'best')
    plt.xlabel('Time')
    plt.ylabel('Population')
    opt_plot()
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot(sol[50:-6000, 0], sol[50:-6000, 1], sol[50:-6000, 2], 'b')
    ax.legend(loc = 'best')
    ax.set_xlabel('Prey')
    ax.set_ylabel('Predator')
    ax.set_zlabel('Super-Predator')
    ax.set_title('Hastings Lotka-Volterra Model')
    opt_plot()
    plt.show()



    x = sol[:,0]
    y = sol[:,1]
    z = sol[:,2]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection = "3d")
    ax.set_xlabel('Prey')
    ax.set_ylabel('Predator')
    ax.set_zlabel('Super-Predator')
    ax.set_title('Hastings Lotka-Volterra Model')
    ax.set_xlim(-0.1, 1)
    ax.set_ylim(-0.1, 1)
    ax.set_zlim(0, 13)

    lines = []
    for i in range(len(t)):
        head = i - 1
        head_slice = (t > t[i] - 1.0) & (t < t[i])
        line1, = ax.plot(x[:i], y[:i], z[:i],
                          color = 'black', alpha = 0.5)
        line1a, = ax.plot(x[head_slice], y[head_slice], z[head_slice],
                           color = 'red', linewidth = 2)
        line1e, = ax.plot([x[head]], [y[head]], [z[head]],
                           color = 'red', marker = 'o', markeredgecolor = 'r')
        lines.append([line1, line1a, line1e,])

    plt.tight_layout()
    ani = animation.ArtistAnimation(fig, lines, interval= 5, blit = True)
    opt_plot()
    plt.show()
    # Sample params: params = [5, 2, 0.1, 2, 0.4, 0.01]
    
def HastingsModel():
    params = [5, 3, 0.1, 2, 0.4, 0.01]
    t = np.linspace(0, 2500, 10000)  
    X0 = np.array([1, 0.19, 10])

    Hastings(X0, params, t)
    
# ---------------------------------------------------------------------------------------------------------------------