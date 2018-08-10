import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-x6z0vzgt.pickle', 'rb') as fin:
    job = pickle.load(fin)
pass
from numpy import *
from ecell4 import *
from math import *
def wrap(job,job_id,task_id):
    def singlerun(kf,phit,phi,L,run,duration):
        import numpy as np
        rm=0.005
        D=1.
        R=2*rm
        rng = GSLRandomNumberGenerator()
        rng.seed(run)   
        f=1.0208582         
        rv=rm*f
        td =(2*rv)**2/(6*D)   
        kd = 4*math.pi*R*D*2
        kb=kf*kd
        with species_attributes():
            C | {'D':str(0.0),'radius':str(rv)}
            E | {'D':str(D),'radius':str(rv)}
            S | {'D':str(D),'radius':str(rv)}
            ES | {'D':str(0.0),'radius':str(rv)}
        with reaction_rules():
            #E+S >ES | kb
            E+S>~E+~S|kb


        m=get_model()
        w = spatiocyte.SpatiocyteWorld(Real3(L,L,L),rv,rng)
        w.bind_to(m)
        size=tuple(w.calculate_shape(Real3(L,L,L),rv))    
        Nev = size[0]*size[1]*size[2]
        NS=int(Nev*phit)
        NE=int(NS/5)
        Nc=int(Nev*phi)            
        w.add_molecules(Species('C'), Nc)
        w.add_molecules(Species('S'), NS)
        w.add_molecules(Species('E'), NE)
        sim = spatiocyte.SpatiocyteSimulator(w)
        sim.initialize()
        duration = duration*td
        obs=FixedIntervalNumberObserver(50*td,['E','S'])
        sim.run(duration,obs)        
        #tlogs,nalog=np.array(obs.data()).T
        if run==1:
            print('kf={},phit={},phi={},L={}'.format(kf,phit,phi,L))
            #print('td={:.4e},kb={:.4e},kr={:.4e},kub={:.4e},kon={:.4e},Nc={},NE={},NS={},duration={:.4e}'.format(td,kb,kr,kub,kon,Nc,NE,NS,duration))
        return obs.data()#tlogs,nalog
    job.update({'run':task_id})
    out=singlerun(**job)
    return out

tid = int(os.environ['SLURM_ARRAY_TASK_ID'])
retval = wrap(job, 1, tid)
filenames = ['/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-el1w3od9.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-20x1ba1y.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-qrf9p7ja.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
