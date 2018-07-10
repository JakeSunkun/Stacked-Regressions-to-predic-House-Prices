import numpy as np
a = (np.square(159 - 241.5) + np.square(280 - 241.5) +np.square(101 - 241.5) +np.square(212 - 241.5) +np.square(224 - 241.5) +\
    np.square(379 - 241.5) +np.square(179 - 241.5) +np.square(264 - 241.5) +np.square(222 - 241.5) +np.square(362 - 241.5) +\
    np.square(168 - 241.5) +np.square(250 - 241.5) +np.square(149 - 241.5) +np.square(260 - 241.5) +np.square(485 - 241.5) +\
    np.square(170 - 241.5))/15
b = np.sqrt(a)

c = (np.square(159) + np.square(280) +np.square(101 ) +np.square(212) +np.square(224 ) +\
    np.square(379) +np.square(179 ) +np.square(264 ) +np.square(222) +np.square(362) +\
    np.square(168 ) +np.square(250) +np.square(149) +np.square(260 ) +np.square(485 ) +\
    np.square(170 ) - 16*np.square(241.5))/15
d = np.sqrt(c)