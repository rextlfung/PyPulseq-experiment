# Started 2/28/2023
# Visualization functions that currently don't work or takes too long to run

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation
from IPython.display import HTML, display

matplotlib.rcParams['animation.embed_limit'] = 2**128

def animate2Dkspace(k_traj_adc, k_traj, t_excitation, t_refocusing, t_adc):
    '''
    !! TAKES FOREVER TO RUN !!
    Animates the 2D k-space trajectory and the sampled points
    
    This function takes in the output of PyPulseq's calculate_kspace() and animates the 2D k-space trajectory for visualization purposes. Returns nothing
    
    Parameters
    ----------
    k_traj_adc : numpy.array
        K-space trajectory sampled at `t_adc` timepoints.
    k_traj : numpy.array
        K-space trajectory of the entire pulse sequence.
    t_excitation : numpy.array
        Excitation timepoints.
    t_refocusing : numpy.array
        Refocusing timepoints.
    t_adc : numpy.array
        Sampling timepoints.

    Returns
    -------
    None
    '''

    # Preprocessing
    k_traj = np.array(k_traj) # convert to np array
    
    fig, ax = plt.subplots() # make new figure axes pair

    # Set axes to be slightly bigger than the traversed area 
    k_min = np.nanmin(k_traj[0:2,:])
    k_max = np.nanmax(k_traj[0:2,:])
    ax.axis([1.1*k_min, 1.1*k_max, 1.1*k_min, 1.1*k_max])

    line, = ax.plot([],[]) # Create line object

    # Helper functions to be passed to FuncAnimation
    def init():
        line.set_data([],[])
        return (line,)

    def animate(i):
        line.set_data(k_traj[0,0:i],k_traj[1,0:i])
        return (line,)

    # Animate
    frames = len(k_traj[0,:])
    ani = matplotlib.animation.FuncAnimation(fig, animate, init_func=init,frames=frames,save_count=0,interval=20,blit=True)
    display(HTML(ani.to_jshtml()))