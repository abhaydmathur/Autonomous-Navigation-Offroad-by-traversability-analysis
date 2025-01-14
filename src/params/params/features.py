##############################################################################
## Default arguments of functions used to extract features from IMU signals ##
##############################################################################
#-------------- These are not to be modified here by the user ---------------#
##############################################################################

##############
## Wavelets ##
##############

# Minimum length for a signal (depends on the wavelet and the number of levels)
SIGNAL_MIN_LENGTH = 20


#-----------#
#  Padding  #
#-----------#

# Padding mode for the signals that are too short
PADDING_MODE = "symmetric"

# The length of the padded signal
SIGNAL_LENGTH = 200


#------------------------------#
#  Discrete Wavelet Transform  #
#------------------------------#

# Number of levels for the discrete wavelet transform
NB_LEVELS = 2

# Wavelet name
WAVELET = "db3"


#--------------#
#  De-noising  #
#--------------#

# De-noising threshold for roll rate, pitch rate and vertical acceleration
# signals
DENOISE_THR = 0.005  # [rad/s | m/s^2]

# De-noising mode
DENOISING_MODE = "soft"


#############
## Fourier ##
#############

# Window size for the mean filter
WINDOW_SIZE = 5


###########
## Other ##
###########

# Length of the blocks the original signal is split into, then to be wrapped
N = 50
