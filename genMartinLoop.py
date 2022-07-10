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

mLoop=Martinloop(ns.steps,smoothfac=ns.smooth,center=ns.center,normunit=ns.normalize)

