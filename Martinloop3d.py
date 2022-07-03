
from scipy import signal
from scipy.fftpack import fft2, ifft2

def fftconvolve2d(x, y):
    # This assumes y is "smaller" than x.
    f2 = ifft2(fft2(x, shape=x.shape) * fft2(y, shape=x.shape)).real
    f2 = np.roll(f2, (-((y.shape[0] - 1)//2), -((y.shape[1] - 1)//2)), axis=(0, 1))
    return f2


class mloopsurf:
    def __init__(self, xsize, ysize, smooth=1, normlen=False, center=False, initvals=None):
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

    def calcwalk(self, kn):
        # stepfilter=((sp.arange(0,self.xsteps.shape[0])<kn)*(sp.arange(0,self.xsteps.shape[1])[:,None]<kn))+0.0
        stepfilter = sp.ones((int(kn) + 1, int(kn) + 1))
        stepfilter[-1] = kn - (int(kn))
        stepfilter[:, -1] = kn - (int(kn))
        xs = fftconvolve2d(self.xsteps, stepfilter)
        ys = fftconvolve2d(self.ysteps, stepfilter)
        zs = fftconvolve2d(self.zsteps, stepfilter)
        return (xs.ravel(), ys.ravel(), zs.ravel())
