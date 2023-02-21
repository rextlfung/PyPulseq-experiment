# Started 2/21/2023
# Additional visualization functions

from matplotlib import pyplot as plt

def plot2Dkspace(Nx, Ny, k_traj_adc):
    plt.figure(1)
    plt.plot(k_traj_adc[0,0:Nx*Ny],k_traj_adc[1,0:Nx*Ny],'k',label='trajectory')
    plt.scatter(k_traj_adc[0,:],k_traj_adc[1,:],marker="x", label='acquired samples')
    plt.scatter(k_traj_adc[0,0],k_traj_adc[1,0],marker="X", label='start')
    plt.scatter(k_traj_adc[0,-1],k_traj_adc[1,-1],marker="X", label='end')
    plt.xlabel('$k_{x} (m^{-1})$')
    plt.ylabel('$k_{y} (m^{-1}$)')
    plt.legend(bbox_to_anchor=(1,1))
    plt.show()

    return