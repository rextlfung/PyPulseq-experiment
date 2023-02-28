# Started 2/21/2023
# Additional visualization functions

import numpy as np
from matplotlib import pyplot as plt

# Make figures high quality by default
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300


def plot2Dkspace(k_traj_adc, k_traj, t_excitation, t_refocusing, t_adc):
    '''
    Plot out the 2D k-space trajectory and the sampled points
    
    This function takes in the output of PyPulseq's calculate_kspace() and plots out the 2D k-space trajectory for visualization purposes. Returns nothing
    
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

    plt.figure()
    plt.plot(k_traj[0,:],k_traj[1,:],'k',linewidth=1,label='trajectory',zorder=1)
    plt.scatter(k_traj_adc[0,:],k_traj_adc[1,:],marker=".", label='acquired samples',zorder=2)
    plt.scatter(k_traj_adc[0,0],k_traj_adc[1,0],marker="X", label='first sample',zorder=2)
    plt.scatter(k_traj_adc[0,-1],k_traj_adc[1,-1],marker="X", label='last sample',zorder=2)
    plt.axis('equal')
    plt.xlabel('$k_{x} (m^{-1})$')
    plt.ylabel('$k_{y} (m^{-1}$)')
    plt.legend(bbox_to_anchor=(1,1))
    plt.show()

    return