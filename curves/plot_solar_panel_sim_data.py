#
#  plot_solar_panel_sim_data.py
#  
#  Copyright (C) 2021, SpaceLab.
#  
#  This file is part of FloripaSat-2.
#
#  FloripaSat-2 is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  
#  FloripaSat-2 is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public
#  License along with FloripaSat-2; if not, see <http://www.gnu.org/licenses/>.
#  
#

__author__      = "Gabriel Mariano Marcelino"
__copyright__   = "Copyright (C) 2021, SpaceLab"
__credits__     = ["Gabriel Mariano Marcelino"]
__license__     = "GPL3"
__version__     = "0.2.0"
__maintainer__  = "Gabriel Mariano Marcelino"
__email__       = "gabriel.mm8@gmail.com"
__status__      = "Development"


import csv
import matplotlib.pyplot as plt
from statistics import mean


def main(args):
    sim_filename = "InputPowerSimulation.csv"

    Vmppt15 = list()
    Vmppt26 = list()
    Vmppt34 = list()
    Isp1 = list()
    Isp2 = list()
    Isp3 = list()
    Isp4 = list()
    Isp5 = list()
    Isp6 = list()
    time_sec = list()
    time_counter = int(0)

    with open(sim_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        try:
            for row in reader:
                if time_counter < 14000:
#                if (time_counter > 3979) and (time_counter < 9815): # Single orbit
                    Vmppt15.append(float(row[0]))
                    Vmppt26.append(float(row[1]))
                    Vmppt34.append(float(row[2]))
                    Isp1.append(2*1000*float(row[3]))
                    Isp2.append(2*1000*float(row[4]))
                    Isp3.append(2*1000*float(row[5]))
                    Isp4.append(2*1000*float(row[6]))
                    Isp5.append(1000*float(row[7]))
                    Isp6.append(1000*float(row[8]))
                    time_sec.append(time_counter)
                time_counter = time_counter + 1
        except:
            pass

    # Solar Panels Voltage
#    plot_data(time_sec, Vmppt15, "Voltage [V]", "", "1", "0", "v_mppt_15.pdf")
#    plot_data(time_sec, Vmppt26, "Voltage [V]", "", "1", "0", "v_mppt_26.pdf")
#    plot_data(time_sec, Vmppt34, "Voltage [V]", "", "1", "0", "v_mppt_34.pdf")

#    fig = plt.figure(figsize=(6.4, 4.5))
#    ax = fig.add_subplot(111)
#    ax1 = fig.add_subplot(311)
#    ax2 = fig.add_subplot(312, sharex=ax1, sharey=ax1)
#    ax3 = fig.add_subplot(313, sharex=ax1, sharey=ax1)
#
#    ax.spines['top'].set_color('none')
#    ax.spines['bottom'].set_color('none')
#    ax.spines['left'].set_color('none')
#    ax.spines['right'].set_color('none')
#    ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)
#    ax.set_ylabel('Voltage [V]')
#
#    ax1.plot(time_sec, Vmppt15, '-r', label='MPPT$_{15}$', linewidth=1.0)
#    ax1.legend(loc='upper right')
#    ax1.grid(True, linestyle=':')
#    ax2.plot(time_sec, Vmppt26, '-g', label='MPPT$_{26}$', linewidth=1.0)
#    ax2.legend(loc='upper right')
#    ax2.grid(True, linestyle=':')
#    ax3.plot(time_sec, Vmppt34, '-b', label='MPPT$_{34}$', linewidth=1.0)
#    ax3.legend(loc='upper right')
#    ax3.grid(True, linestyle=':')
#
#    plt.setp(ax1.get_xticklabels(), visible=False)
#    plt.setp(ax2.get_xticklabels(), visible=False)
#
#    plt.xlabel("Time [sec]")
#
#    plt.savefig("v_mppt.pdf", bbox_inches='tight', dpi=600, transparent=True)
#    plt.show()
#
#   # Solar Panels Current
#    fig = plt.figure(figsize=(6.4,9))
#    ax = fig.add_subplot(111)
#    ax1 = fig.add_subplot(611)
#    ax2 = fig.add_subplot(612, sharex=ax1, sharey=ax1)
#    ax3 = fig.add_subplot(613, sharex=ax1, sharey=ax1)
#    ax4 = fig.add_subplot(614, sharex=ax1, sharey=ax1)
#    ax5 = fig.add_subplot(615, sharex=ax1, sharey=ax1)
#    ax6 = fig.add_subplot(616, sharex=ax1, sharey=ax1)
#
#    ax.spines['top'].set_color('none')
#    ax.spines['bottom'].set_color('none')
#    ax.spines['left'].set_color('none')
#    ax.spines['right'].set_color('none')
#    ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)
#    ax.set_ylabel('Current [mA]')
#
#    ax1.plot(time_sec, Isp1, '-r', label='+X', linewidth=1.0)
#    ax1.legend(loc='upper right')
#    ax1.grid(True, linestyle=':')
#    ax2.plot(time_sec, Isp2, '-g', label='-X', linewidth=1.0)
#    ax2.legend(loc='upper right')
#    ax2.grid(True, linestyle=':')
#    ax3.plot(time_sec, Isp3, '-b', label='+Y', linewidth=1.0)
#    ax3.legend(loc='upper right')
#    ax3.grid(True, linestyle=':')
#    ax4.plot(time_sec, Isp4, '-c', label='-Y', linewidth=1.0)
#    ax4.legend(loc='upper right')
#    ax4.grid(True, linestyle=':')
#    ax5.plot(time_sec, Isp5, '-m', label='+Z', linewidth=1.0)
#    ax5.legend(loc='upper right')
#    ax5.grid(True, linestyle=':')
#    ax6.plot(time_sec, Isp6, '-y', label='-Z', linewidth=1.0)
#    ax6.legend(loc='upper right')
#    ax6.grid(True, linestyle=':')
#
#    plt.setp(ax1.get_xticklabels(), visible=False)
#    plt.setp(ax2.get_xticklabels(), visible=False)
#    plt.setp(ax3.get_xticklabels(), visible=False)
#    plt.setp(ax4.get_xticklabels(), visible=False)
#    plt.setp(ax5.get_xticklabels(), visible=False)
#
#    plt.xlabel("Time [sec]")
#
#    plt.savefig("sim_i_sp.pdf", bbox_inches='tight', dpi=600, transparent=True)
#    plt.show()

    # Solar Panels Power
    cur_y_x = [x + y for x, y in zip(Isp1, Isp2)]
    cur_x_z = [x + y for x, y in zip(Isp3, Isp4)]
    cur_z_y = [x + y for x, y in zip(Isp5, Isp6)]
    pwr_y_x = [x * y for x, y in zip(cur_y_x, Vmppt15)]
    pwr_x_z = [x * y for x, y in zip(cur_x_z, Vmppt26)]
    pwr_z_y = [x * y for x, y in zip(cur_z_y, Vmppt34)]
    pwrs = [pwr_y_x, pwr_x_z, pwr_z_y]
    sp_power = [sum(x) for x in zip(*pwrs)]

    max_sp_power = max(sp_power[3979:9815])
    average_sp_power = mean(sp_power[3979:9815])
    average_sp_power_sun = mean(sp_power[3979:7691])
    average_sp_power_eclipse = mean(sp_power[7691:9815])

    print("Max solar panel power: ", max_sp_power)
    print("Average: ", average_sp_power)
    print("Average (sun): ", average_sp_power_sun)
    print("Average (eclipse): ", average_sp_power_eclipse)

    plt.plot(time_sec, sp_power, '-b', linewidth=0.75, label='Input power')
    plt.plot(time_sec, [average_sp_power]*len(time_sec), '-g', linewidth=1, label='Average (orbit)')
    plt.plot(time_sec[:1855], [average_sp_power_sun]*len(time_sec[:1855]), '-r', linewidth=1, label='Average (sun light)')
    plt.plot(time_sec[3979:7691], [average_sp_power_sun]*len(time_sec[3979:7691]), '-r', linewidth=1)
    plt.plot(time_sec[9815:13525], [average_sp_power_sun]*len(time_sec[9815:13525]), '-r', linewidth=1)

    plt.grid(True, linestyle=':')
    plt.xlabel("Time [sec]")
    plt.ylabel("Power [mW]")
    plt.legend(loc='upper right')

    ratio = 0.5
#    xleft, xright = plt.axes().get_xlim()
#    ybottom, ytop = plt.axes().get_ylim()
#    plt.axes().set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
#    plt.axes().set_aspect(0.5)

    plt.savefig("_sp_sim_power.pdf", bbox_inches='tight', dpi=600, transparent=True)
    plt.show()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
