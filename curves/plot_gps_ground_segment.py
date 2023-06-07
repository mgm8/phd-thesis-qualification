#
#  plot_contacts_map.py
#  
#  Copyright (C) 2020, Universidade Federal de Santa Catarina
#  
#  This file is part of FloripaSat-GRS.
#
#  FloripaSat-GRS is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  FloripaSat-GRS is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public
#  License along with FloripaSat-GRS; if not, see <http://www.gnu.org/licenses/>.
#  
#

__author__      = "Gabriel Mariano Marcelino"
__copyright__   = "Copyright (C) 2020, Universidade Federal de Santa Catarina"
__credits__     = ["Gabriel Mariano Marcelino"]
__license__     = "GPL3"
__version__     = "0.1.0"
__maintainer__  = "Gabriel Mariano Marcelino"
__email__       = "gabriel.mm8@gmail.com"
__status__      = "Development"


import matplotlib.pyplot as plt
import geopandas

def main(args):
    world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))

    fig, ax1 = plt.subplots(1, 1, figsize=(20,15))
    world.plot(ax=ax1)

    ax1.set_axis_off()

    latitude = list()
    longitude = list()

    # Colorado Springs
#    latitude.append(38.8339)
#    longitude.append(-104.8219)

    # MCS
#    plt.plot(longitude, latitude, 'rs')

#    latitude = []
#    longitude = []

    # Colorado Springs
    latitude.append(38.8339)
    longitude.append(-104.8219)
    plt.annotate("Colorado Springs", xy=(-104.8219, 38.8339), xytext=(3, 3), textcoords="offset points")

    # Hawaii
    latitude.append(19.5429)
    longitude.append(-155.6659)
    plt.annotate("Hawaii", xy=(-155.6659, 19.5429), xytext=(3, 3), textcoords="offset points")

    # Ascension Island
    latitude.append(-7.9696)
    longitude.append(-14.4122)
    plt.annotate("Ascension Island", xy=(-14.4122, -7.9696), xytext=(3, 3), textcoords="offset points")

    # Diego Garcia
    latitude.append(-7.3192)
    longitude.append(72.4241)
    plt.annotate("Diego Garcia", xy=(72.4241, -7.3192), xytext=(3, 3), textcoords="offset points")

    # Kwajalein
    latitude.append(8.72)
    longitude.append(167.73)
    plt.annotate("Kwajalein", xy=(167.73, 8.72), xytext=(3, 3), textcoords="offset points")

    # Monitor stations
    plt.plot(longitude, latitude, 'ro')

    plt.savefig("gps-ground-segment.pdf", bbox_inches='tight', dpi=600, transparent=True)
    plt.show()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
