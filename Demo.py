import scipy as sp
from matplotlib import pyplot as plt
from Martinloop import Martinloop
k = 500
ticr = 1
for pp in [1,2,5,10,25,50]:
    ml=Martinloop(k,pp)
    for i in sp.arange(1, k, ticr):
        fig = plt.figure()
        xs,ys=ml.calcwalk(i,center=False)
        plt.fill(xs,ys,color='black')
        plt.fill(-xs, ys,color='black')
        plt.text(0, .8, "Steps: {:0.2f} / {:0.2f}, Smoothing={}".format(i, k, pp),
                 horizontalalignment='center')
        plt.savefig('jgani{:02d}-{:03d}.png'.format(pp, int(i / ticr)))
        plt.close()

ml=Martinloop(500,20)
for i in sp.arange(1, 100, 1):
    fig = plt.figure()
    ml.nudgeSteps(.1)
    xs,ys=ml.calcwalk(100,center=False)
    plt.fill(xs,ys,color='black')
    plt.fill(-xs, ys,color='black')
    plt.savefig('nudge{:03d}.png'.format(i))
    plt.close()
