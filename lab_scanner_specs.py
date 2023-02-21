import pypulseq as pp

# Inside 3T scanner (UHP):
system = pp.Opts(max_grad=100, grad_unit='mT/m',
                 max_slew=200, slew_unit='T/m/s',
                 grad_raster_time=4e-6)

# Outside 3T scanner (MR750):
system = pp.Opts(max_grad=50, grad_unit='mT/m',
                 max_slew=200, slew_unit='T/m/s',
                 grad_raster_time=4e-6)

# Gradient raster time = 4 us