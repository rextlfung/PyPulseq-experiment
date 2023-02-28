addpath ~/code/pulseq/matlab/  % +mr package
addpath ~/code/toppe/          % +toppe package
addpath ~/code/PulseGEq/       % +pulsegeq package

fname = "rex_3_epi_se_rs.seq";

seq = mr.Sequence();
seq.read(fname);
sys = toppe.systemspecs('maxSlew',200,'slewUnit','T/m/s','maxGrad',100,'gradUnit','mT/m');
pulsegeq.seq2ge(seq, sys, 'toppeVersion', '5', 'verbose', true);