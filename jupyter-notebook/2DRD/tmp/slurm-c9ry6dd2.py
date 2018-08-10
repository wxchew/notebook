import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-zs52kjpm.pickle', 'rb') as fin:
    job = pickle.load(fin)
pass
from numpy import *
from ecell4 import *
from math import *
def wrap(job,job_id,task_id):
    def singlerun(ka,kd,NA,L,run,duration,rm):
        import numpy as np
        D=1
        rng = GSLRandomNumberGenerator()
        rng.seed(run)   
        voxelr=rm    
        LL=4*L
        td =(2*voxelr)**2/(6*D)
        ori = Real3(LL*0.5,0,0)
        unit0 = Real3(0,0,L)
        unit1 = Real3(0,L,0)        
        w = spatiocyte.SpatiocyteWorld(Real3(LL,L,L),voxelr,rng)
        size=tuple(w.calculate_shape(Real3(LL,L,L),voxelr))
        lx,ly,lz=w.actual_lengths()
        Ns = size[1]*size[2]
        Area= ly*lz
        V=ly*lz*lx
        if run==1:
            print('actual A {}, V{},Ns{},td{}'.format(Area,V,Ns,td))
        w.add_structure(Species('M'),PlanarSurface(ori,unit0,unit1))
        with species_attributes():
            A |  {'D': str(D), 'radius':str(voxelr)}
            B |  {'D': str(D), 'radius':str(voxelr),'location':'M'}

        #with reaction_rules():#for spa and egfrd
        #    A + M > B | ka
            #B > A |kd
            #A+M>M | ka

        m2 = get_model()
        w.bind_to(m2)
        w.add_molecules(Species('A'), NA)
        sim = spatiocyte.SpatiocyteSimulator(w)
        sim.initialize()
        pid = [p[0] for p in w.list_particles_exact(Species('A'))]
        obs = FixedIntervalTrajectoryObserver(duration/5,pids=pid,resolve_boundary=False)
        #obs=FixedIntervalNumberObserver(td*500,['A'])
        sim.run(duration,obs)        
        #dat=[tuple(pos) for pos in obs.data()[0]]
        return obs.data(),obs.t()
    job.update({'run':task_id})
    out=singlerun(**job)
    return out

tid = int(os.environ['SLURM_ARRAY_TASK_ID'])
retval = wrap(job, 1, tid)
filenames = ['/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-d09mjjp_.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-kdj3t81v.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-1zkdi_a1.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-vqwzch08.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-p4ujdrkl.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-7lghho8n.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-z9jukf8h.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-sx4l2yxd.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-5rj2uz74.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-l8o29qsp.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
