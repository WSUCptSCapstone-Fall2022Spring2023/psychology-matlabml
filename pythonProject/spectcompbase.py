
# Preproccesses data and calculates the following metrics: power,
#  coherence, and power coupling. Read input documentation for more detail
#  on the options for these analyses and necessary information to run the
#  function. N.B. scbParamsSingle.m and scbParamsMulti.m can be used to
#  help generate the inputs need to fun this function; scbParamsMulti.m is
#  especially useful for batch processing files.
#__________________________________________________________________________
# INPUTS:
# cfg = config structure with the following fields:
#   sdir = source directory of data; format: string
#   file = file name w/o extension; format: string
#   nFilt = wether or not to use a filter; format: 'y' or 'n'
#   dsf = factor with which to downfactor; format: whole integer
#   thresh = threshold for detecting noise artifacts; format: mV (or other
#       y-axis scale for time series)
#   onset = number of samples to NaN before noise event; format: seconds
#   offset = number of samples to NaN after noise event; format: seconds
#   foi = frequencies of interest; format = [lower step upper] in Hz
#   bands = structure with bands of interest starting with lowest; format:
#       {'band1',[lower upper];'band2',[lower upper];...}
#   overlap = amount of overlap to use with sliding windows; format:
#       percent in decimal form (1-percent; e.g. 90# overlap = 0.1)
#   eoi = events of interest alongside window around that event to be
#       consider a single epoch; format: cell {'tag1',[0 3];'tag2',[-1.5
#       1.5]} indicates to use a 3 second window startint at tag1
#       (interval) and a 3 second window centered at the scalar tag2.
#       N.B.: if all the data use the tag 'all', otherwise use tags
#       corresponding to event markers.
#   vis = whether or not to plot power and coherence; format = 'y' or 'n'
#   saveParent = parent directory path to save plots and files; format:
#       string N.B.: if directory/file exists will warn about overwritting
#__________________________________________________________________________
# OUTPUTS:
# LFPTs = local field potential structure containing the following
# information
#   type = kind of data structure; if created through Pl2tomvdmGenFile.m
#       then this will be 'tsd', i.e. "time stamped data" (See
#       Pl2tomvdmGenFile.m and tsd.m)
#   tvec = vector of time stamps
#   data = local field potential data; chan X timestamp
#   label = channel labels
#   cfg = history structure of what had been done to data when converted
#       and processed
#   oneChan =
# trls =
# clnTrls =
# clnEvents =
# relPower =
# psdTrls =
# coh =
# stdPower =
# stdCoh =
# hist =
#__________________________________________________________________________


def spectcompbase(cfg):





























