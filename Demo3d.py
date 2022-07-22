
from Martinloop3d import mloopsurf
import pyvista as pv
import scipy as sp, numpy as np

k = 200
sf = 25
j = int(k / 2)
import time
actr=None
actrf = actr
s3 = mloopsurf(k, k, sf, center=True, normlen=True)
plotter = pv.Plotter()
ocam = plotter.camera.copy()
plotter.open_gif('gest{}.gif'.format(int(time.time())))
plotter.camera = ocam
camdis = max(sp.absolute(s3.update(50)).ravel()) * .25
cspins = 2
ixyz = (sp.random.random((k, k)) * 2 - 1, sp.random.random((k, k)) * 2 - 1, sp.random.random((k, k)) * 2 - 1)

dedge = True
ml=mloopsurf(k,k,20)
for j in (sp.arange(1, k, 1)):  # sp.hstack([[int(k/2)],np.arange(1,k)]):
    print("{}/{}".format(j, k))
    plotter.remove_actor(actr)
    plotter.remove_actor(actrf)
    ml.genMesh(k,j)
    mesh=ml.mesh
    meshf = mesh.flip_z(inplace=False)
    rota = j * (360 / k * cspins)
    mesh.rotate_y(rota)
    meshf.rotate_y(rota)
    actr = plotter.add_mesh(mesh, opacity=1, show_edges=dedge)
    actrf = plotter.add_mesh(meshf, opacity=1, show_edges=dedge)
    plotter.camera.position = (mesh.length * 1.2 + camdis, 0, 0)
    plotter.camera.focal_point = (0, 0, 0)
    plotter.camera.roll = 0
    labeltext = "step {}/{} smooth factor={} \n cam dist={:0.1f} cam angle={:0.1f}".format(j, k, sf,
                                                                                           mesh.length + camdis, rota)
    plotter.add_text(labeltext, position='lower_edge', font_size=25, name='bottxt')
    plotter.write_frame()
