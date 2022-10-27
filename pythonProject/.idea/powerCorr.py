

## Calculates power correlations within frequency bands across channels
# INPUTS:
# psdTrls = power-spectra for each behavior of interest; format: structure
#   created by powerComp.m where each behavior is in its own cell with
#   .relPow as a field containing the relative power in each band for every
#   trial
#__________________________________________________________________________
# OUTPUTS:
# r = cell array of correlation values; format: cell array with 3D arrays
#   containing all correlation values (channel,channel,band)
# rVect = vectorized version of r; because of intrinsic symmetry of
#   correlation matrices, takes just lower half of matrix and puts into row
#   vector. For example, if 4 channels then the vector of r values will be
#   for the following correlations: 1-2, 1-3, 1-4, 2-3, 2-4, and 3-4.
#____________
def powerCorr(psdTrls):
    # Find empty events
    return [r, rVect]