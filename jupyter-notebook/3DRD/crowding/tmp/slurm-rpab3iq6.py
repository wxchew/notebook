import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-_7oiia6v.pickle', 'rb') as fin:
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
        #duration = duration*td
        obs=FixedIntervalNumberObserver(td,['E','S'])
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
filenames = ['/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-5lr6cpzm.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-lw3geobh.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-x3dtta6h.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-ufstko3m.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-stq86n05.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-z6wrrwxu.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-7lc7tlwp.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-dx6t0r2c.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-w9ll_r80.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-x5n2lrbo.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-_l7ua7ey.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-026d_1a0.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-ssqkrtwa.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-xbraofs1.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-vcjbs_1d.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-ncu1m21j.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-vh61nl0z.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-7p_o39a2.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-gy1w8k4p.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-6eczoime.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-38w64hce.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-_jgmj8o0.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-wd7f3fii.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-emt5_9lt.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-h_t_o94f.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-i94nsoey.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-lbdtioax.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-to3ewbc4.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-kzhuryqn.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-e3dup3t7.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-umpgic25.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-q9vu62m1.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-xt6w800v.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-4iemlyuf.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-mu6sij7a.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-b08s6h2t.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-zy742veo.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-g_r_4l9g.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-zw8swi6g.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-p1hnyvno.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-rqds1gz8.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-bawuxuq7.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-lgun0igo.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-zt736g7d.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-zom_mv1p.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-_unwi_df.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-xcwmkkxd.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-83c73ne2.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-a3wb8fe_.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/crowding/tmp/slurm-vm5vco0m.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
