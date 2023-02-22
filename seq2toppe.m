addpath ~/code/pulseq/matlab/  % +mr package
addpath ~/code/toppe/          % +toppe package
addpath ~/code/PulseGEq/       % +pulsegeq package

fname = 'rex_2_epi.seq';

seq = mr.Sequence();
seq.read(fname);
sys = toppe.systemspecs('maxSlew',200,'slewUnit','T/m/s','maxGrad',50','gradUnit','mT/m');
pulsegeq.seq2ge(fname, sys, 'toppeVersion', 'v4', 'verbose', true);