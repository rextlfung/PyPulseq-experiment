# Feb 21, 2023
- Started a devlog to keep track of what I did.
- Sequences owned: One line, vanilla GRE, vanilla EPI
- Functions owned: viz.py

# Feb 22, 2023
- increased resolution of plot2Dkspace()
- wrote seq2toppe.m to convert .seq files to GE using PulseGEq
- was gonna scan but ran into compatibility issues between PyPulseq and Pulseq
- resolved issue by upgrading pypulseq module by pip installing latest version (1.4.0) downloaded from Github

# Feb 23, 2023
- began working on animating k-space trajectory for visualization
- code runs way too slow and uses too much memory
- need to figure out a more memory efficent way of animating plots

# Feb 28, 2023
- made animation work by setting matplotlib.rcParams['animation.embed_limit'] = 2**128 (effectively unlimited)
- takes ~90 seconds to run for Nx = Ny = 8 for vanilla EPI sequence
- takes a lifetime ot run for Nx = Ny = 16 for vanilla GRE sequence
- decided to give up on animating k-space trajectory as it provides too little value in data visualization for its computational cost
- created viz_failed.py to house dysfunctional visualization functions
- cloned new updates to PyPulseq github but there were several bugs as well as removed functions :(
- realized that seq2ge interpolates .seq files to toppe files, which can exceed system limits defined when creating the sequence in pulseq