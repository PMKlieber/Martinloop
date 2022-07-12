
import Martinloop
from Martinloop import Martinloop
import sys

from Martinloop import Martinloop
import argparse

parser = argparse.ArgumentParser(prog='genMartinLoop',add_help=True)
parser.add_argument('--steps', default=500, type=int,help='Number of steps in walk')
parser.add_argument('--smooth', default=10, type=int,help='Smoothing factor')
parser.add_argument('--center', action='store_true')
parser.add_argument('--normalize', action='store_true')
ns=(parser.parse_args(sys.argv[1:]))

ml=Martinloop(ns.steps,smoothfac=ns.smooth,center=ns.center,normunit=ns.normalize)

from matplotlib import pyplot as plt

for i in range(1,ns.steps):
    fig = plt.figure()
    fsplt = fig.add_subplot()
    #fsplt.set_xlim((-20, 20))


    #fsplt.set_ylim((-20, 20))
    xs, ys = ml.calcwalk(i, center=False)
    plt.fill(xs, ys, color='black')
    plt.fill(-xs, ys, color='black')
    #plt.text(0, -18, "Steps: {:0.2f} / {:0.2f}, Smoothing={}".format(i, ns.steps, ns.smooth),
#             horizontalalignment='center')
    plt.savefig('jgani{:02d}-{:04d}.png'.format(ns.smooth, int(i)))
    plt.close()

