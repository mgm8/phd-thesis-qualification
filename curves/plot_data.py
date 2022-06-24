# -*- coding: utf-8 -*-

import sys
import csv
import matplotlib.pyplot as plt

time_days = list()
altitude = list()

with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=str(','), quotechar=str('|'))
    try:
        for row in reader:
            time_days.append(float(row[0]))
            altitude.append(float(row[1]))
    except:
        pass

plt.plot(time_days, altitude, '-b', linewidth=1.0)

plt.grid(True, linestyle=':')
plt.xlabel('Time [days]')
plt.ylabel('Altitude [km]')
#plt.legend(loc='best')

ratio = 0.5
xleft, xright = plt.axes().get_xlim()
ybottom, ytop = plt.axes().get_ylim()
plt.axes().set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

plt.savefig('lifetime.pdf', bbox_inches='tight', dpi=600, transparent=True)

plt.show()
