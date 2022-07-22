

def rplane(x1=-10, x2=10, y1=-10, y2=10, xres=.01, yres=.01):
    """ Generates a complex plane
    Parameters
    ----------
    x1 : start x coordinate
    x2 :  end x coordinate
    y1 :  start y coordinate
    y2 :  end y coordinate
    xres : x resolution
    yres : y resolution

    Returns
    -------

    """
    r = []
    for i in sp.arange(x1, x2, xres):
        rr = []
        for j in sp.arange(y1, y2, yres):
            rr.append(i + j * 1j)
        r.append(rr)
    return sp.array(r)


def cpshow(cp):
    hsv = sp.zeros((cp.shape) + (3,))
    hsv[..., 0] = (sp.angle(cp) / sp.pi) / 2 + 0.5
    hsv[..., 1] = 1
    hsv[..., 2] = 1
    plt.matshow(hsv_to_rgb(hsv))
    plt.show()


from matplotlib import pyplot as plt
import scipy as sp
import numpy as np
from matplotlib.animation import FuncAnimation


crnd = lambda j=1: np.random.random() * j * 2 - j
crnda = lambda j=1, n=100: np.random.random(n) * j * 2 - j


fenum = lambda j: [1 if k < j - 1 or j % 1 == 0 else j % 1 for k in range(0, int(np.ceil(j)))]
from numpy import ceil, floor

minmax = lambda i: (np.min(i), np.max(i))
cxlim = (-10, 10)
cylim = (-10, 10)
pp = 45

from scipy import signal

unorm = lambda i: i / sp.sum(i)

from scipy.fftpack import fft2, ifft2


# Two-dimensional convolution fonction
def fftconvolve2d(x, y):
    # This assumes y is "smaller" than x.
    f2 = ifft2(fft2(x, shape=x.shape) * fft2(y, shape=x.shape)).real
    f2 = np.roll(f2, (-((y.shape[0] - 1) // 2), -((y.shape[1] - 1) // 2)), axis=(0, 1))
    return f2


class mloopsurf:
    def __init__(self, xsize, ysize, smooth=1, normlen=False, center=False, initvals=None):
        self.mesh=None
        smoothfilter = np.ones((smooth, smooth)) / smooth ** 2
        if initvals is None:
            initx, inity, initz = sp.random.random((xsize, ysize)) * 2 - 1, sp.random.random(
                (xsize, ysize)) * 2 - 1, sp.random.random((xsize, ysize)) * 2 - 1
        else:
            initx, inity, initz = initvals
        self.xsteps = fftconvolve2d(initx, smoothfilter)
        self.ysteps = fftconvolve2d(inity, smoothfilter)
        self.zsteps = fftconvolve2d(initz, smoothfilter)
        if normlen:
            stepl = np.sqrt(self.xsteps ** 2 + self.ysteps ** 2 + self.zsteps ** 2)
            self.xsteps /= stepl
            self.ysteps /= stepl
            self.zsteps /= stepl
        if center:
            self.xsteps -= np.mean(self.xsteps)
            self.ysteps -= np.mean(self.ysteps)
            self.zsteps -= np.mean(self.zsteps)

    def genMesh(self, gridSize,stepNum):
        xs, ys, zs = self.update(stepNum)
        meshl = sp.arange(0, gridSize) + sp.arange(0, gridSize * gridSize, gridSize)[:, None]
        tris = sp.array(
            [(4, meshl[i, j], meshl[(i + 1) % gridSize, j], meshl[(i + 1) % gridSize, (j + 1) % gridSize], meshl[i, (j + 1) % gridSize]) for i in
             range(0, gridSize) for j in range(0, gridSize)]).ravel()
        verts = np.transpose([xs, ys, zs])
        self.mesh = pv.PolyData(verts, tris)

    def update(self, kn):
        # stepfilter=((sp.arange(0,self.xsteps.shape[0])<kn)*(sp.arange(0,self.xsteps.shape[1])[:,None]<kn))+0.0
        stepfilter = sp.ones((int(kn) + 1, int(kn) + 1))
        stepfilter[-1] = kn - (int(kn))
        stepfilter[:, -1] = kn - (int(kn))
        xs = fftconvolve2d(self.xsteps, stepfilter)
        ys = fftconvolve2d(self.ysteps, stepfilter)
        zs = fftconvolve2d(self.zsteps, stepfilter)
        return (xs.ravel(), ys.ravel(), zs.ravel())


import pyvista as pv

