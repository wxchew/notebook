import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-8o8na3s1.pickle', 'rb') as fin:
    job = pickle.load(fin)
pass
from numpy import *
from ecell4 import *
from math import *
def wrap(job,job_id,task_id):
    def singlerun(kaf,run,correct):
        import numpy as np
        duration=0.05
        rm = 0.005
        factor =700

        L = factor*rm        
        voxelr=rm       
        if correct==True:
            voxelr=rm*1.0208582         
        Na=4000
        Nb=4000
        #run+=30000
        rng = GSLRandomNumberGenerator()
        rng.seed(run)
        D = 1.
        kd= 4.0*math.pi*D*2*rm
        ka = kaf*kd
        kon = (ka*kd)/(ka+kd)
        tm =(2*voxelr)**2/(6*D)

        w = spatiocyte.SpatiocyteWorld(ones()*L,voxelr)
        with species_attributes():
            A |  {'D': str(0), 'radius':str(voxelr)}
            B |  {'D': str(D), 'radius':str(voxelr)}

        with reaction_rules():
            A + B > B | ka

        m2 = get_model()

        w = spatiocyte.SpatiocyteWorld(ones()*L,voxelr,rng)
        w.bind_to(m2)
        w.add_molecules(Species('A'), Na)
        w.add_molecules(Species('B'), Nb)
        sim = spatiocyte.SpatiocyteSimulator(w)
        sim.initialize()
        return
    job.update({'run':task_id})
    out=singlerun(**job)

    return out    

tid = int(os.environ['SLURM_ARRAY_TASK_ID'])
retval = wrap(job, 1, tid)
filenames = ['/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-t3r0uzca.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-8di6szgr.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-cx2pz95b.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-lt88i70a.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-q3q4oaxg.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-61f8ghy5.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-oni_cwbe.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-i14qtbwy.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-3tjrwaxi.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-p95saz3v.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
