# Started 2/21/2023
# Additional visualization functions

from matplotlib import pyplot as plt

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

def plot2Dkspace(k_traj_adc, k_traj, t_excitation, t_refocusing, t_adc):
    plt.figure(1)
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