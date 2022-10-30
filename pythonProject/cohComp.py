## Calculates coherence using either a single hamming window and mscohere
# or the multitaper method proposed by Percival and Walden.
#__________________________________________________________________________
# INPUTS
# trls = structure containing data to be analyzed; requires a field
#   'trials' which contains raw data channel X time X trial
# adfreq = sampling rate; format = integer
# eoi = events of interest; format = cell array, first column has name of
#   event and second column has timing around event
# bands = cell array of frequency bands; format = cell array, first column
#   has name of bands and second column has inclusive start and stop of
#   bands
# zeroedChannel = index of any channels to be skipped due to noise; format
#   = integer
# foi = frequencies of interest; format = [low frequency, step, high
#   frequency]
# nFilt = frequencies to interpolate over to account for notch filter; if
#   no notch filter was applied, leave empty; format = [low high]
# vis = whether or not to visualize results; format = 0 (n) or 1 (y)
# method = which method to use for calculating coherence; format = either
#   'mat' for mscohere or 'mtm' for multitaper method
# NW = number of windows to use for multitaper method; format = integer,
#   default is 8
# overlap = percent overlap between windows for mscohere; format = decimal,
#   default is 0.5 (50#)
#__________________________________________________________________________
# OUTPUTS
# coh = data structure with one cell per event with the following fields
#   Cxy = coherence; format = channel pair X frequency X trial
#   mtCxy = mean coherence over trials; format = channel pair X band X
#       trial (replicated values across bands)
#   mBandCoh = mean coherence per band; format = channel pair X band X
#       trial
#   normBandCoh = normalized band coherence; format = channel pair X band X
#       trial (mBandCoh./mtCxy)
#   f = frequency vector corresponding to 2nd dimension of Cxy; format = Hz
#__________________________________________________________________________