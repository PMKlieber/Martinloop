import scipy as sp
import numpy as np
from matplotlib.animation import FuncAnimation

minmax = lambda i: (np.min(i), np.max(i))

# Center an array
acent = lambda i: i - np.mean(i)

# Generate a random value between -j and +j
crnd = lambda j=1: np.random.random() * j * 2 - j

# Generate n random values between -j and +j
crnda = lambda j=1, n=100: np.random.random(n) * j * 2 - j


class Martinloop:
    def __init__(self, nsteps, smoothfac=3, center=True, normunit=False):
        self.nsteps = nsteps
        # Generate random steps for the walk
        self.stepx = np.random.random(nsteps) * 2 - 1
        self.stepy = np.random.random(nsteps) * 2 - 1
        # Put steps through smoothing filter
        if smoothfac > 1:
            self.stepx = np.array(
                [np.mean(self.stepx[[j % nsteps for j in range(l, l + smoothfac)]]) for l in range(0, nsteps)])
            self.stepy = np.array(
                [np.mean(self.stepy[[j % nsteps for j in range(l, l + smoothfac)]]) for l in range(0, nsteps)])
        # Normalize steps to unit vector
        if (normunit):
            steplen = np.sqrt(self.stepx ** 2 + self.stepy ** 2)
            self.stepx = self.stepx / steplen
            self.stepy = self.stepy / steplen
        # Center the steps so the end ip at the origin
        if (center):
            self.stepx = self.stepx - np.mean(self.stepx)
            self.stepy = self.stepy - np.mean(self.stepy)
        # Use matrix multiplication to calculate the walk halfway through to find approx bounds
        afc = nsteps / 2
        gg = np.minimum(1, np.maximum(0, afc - (((np.arange(0, nsteps)) + np.arange(nsteps, 0, -1)[:, None]) % nsteps)))
        cxlim = minmax(np.matmul(gg, self.stepx) * 1.4)
        cylim = minmax(np.matmul(gg, self.stepy) * 1.4)
        tlim = np.max(np.absolute([cxlim, cylim]))
        cxlim = (-tlim, tlim)
        cylim = (-tlim, tlim)
        self.nudgesmat = ((
                    smoothfac > (((np.arange(0, nsteps)) + np.arange(nsteps, 0, -1)[:, None]) % nsteps))) / smoothfac

    # Alter all steps by "nudging" them a random value between -amt,+amt
    def nudgeSteps(self, amt):
        self.stepx += np.matmul(self.nudgesmat, acent(crnda(amt, self.nsteps)))
        self.stepy += np.matmul(self.nudgesmat, acent(crnda(amt, self.nsteps)))

    # Calculate the random walk where each step affects the next afc positions, wrapping around
    def calcwalk(self, afc, nudge=0, center=False):
        kn2 = 1
        # Create a matrix of each position in the walk, and which steps affect that position
        wmat = np.minimum(1, np.maximum(0, afc - (
                    ((np.arange(0, self.nsteps)) + np.arange(self.nsteps, 0, -1)[:, None]) % self.nsteps)))
        # Use Matrix Multiplication to calculate the positions of the walk
        xs = np.matmul(wmat, self.stepx)
        ys = np.matmul(wmat, self.stepy)
        # Make last step loop back around to first
        xs = np.hstack([xs, xs[0]])
        ys = np.hstack([ys, ys[0]])
        return xs, ys
