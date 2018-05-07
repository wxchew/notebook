import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-jcdlimz7.pickle', 'rb') as fin:
    job = pickle.load(fin)
pass
from numpy import *
from ecell4 import *
from math import *
def wrap(job,job_id,task_id):
    def singlerun(kf,K,correct,NA,NB,L,run,durfac):
        import numpy as np
        rng = GSLRandomNumberGenerator()
        rng.seed(run)
        rm = 0.005
        factor = (2 * sqrt(2.0) + 4 * sqrt(3.0) + 3 * sqrt(6.0) + sqrt(22.0))**2/(72 * (6 * sqrt(2.0) + 4 * sqrt(3.0) + 3 * sqrt(6.0)))
        R=2*rm
        voxelr=rm
        D = 1.
        ka=kf*2*pi*D
        gamma=0.577
        td =(2*voxelr)**2/(4*D)
        duration=2#td*10**durfac
        H = 3*voxelr*2
        kd=ka/K        
        if correct==True:
            PP=1./(1+math.sqrt(3)*(math.log(1./12)+(4*math.pi*D/ka)-2*gamma)/2/math.pi)
            ka = PP*D/factor
        ori = Real3(0.5*H,0,0)
        unit0 = Real3(0,0,L)
        unit1 = Real3(0,L,0)        
        w = spatiocyte.SpatiocyteWorld(Real3(H,L,L),voxelr,rng)
        #size=tuple(w.calculate_shape(Real3(H,L,L),voxelr))
        #Nmv=size[1]*size[2]    
        #print('phil=',N/Nmv)
        lx,ly,lz=w.actual_lengths()
        Area= ly*lz
        #Area=Nmv*(2*voxelr)**2
        c0=NB/Area
        sinf=kd/(kd+c0*ka)
        #print(ka,kd)
        with species_attributes():
            A |  {'D': str(0), 'radius':str(voxelr),'location':'X'}
            B |  {'D': str(D), 'radius':str(voxelr),'location':'X'}
            C |  {'D': str(0), 'radius':str(voxelr),'location':'X'}

        with reaction_rules():#for spa and egfrd
            A + B == C | (ka,kd)

        m2 = get_model()
        w.bind_to(m2)
        w.add_structure(Species('X'),PlanarSurface(ori,unit0,unit1))
        w.add_molecules(Species('A'), NA)
        w.add_molecules(Species('B'), NB)
        sim = spatiocyte.SpatiocyteSimulator(w)
        sim.initialize()
        obs=FixedIntervalNumberObserver(td,'A')
        sim.run(duration,obs)
        out=np.array(obs.data()).T
        if correct==True:
            #name = '/home/chew/outputdata/2DRD/newP/kfac'+str(kaf)+'/run'+str(run)
            name = '/home/chew/outputdata/2DRD/newP/kf'+str(kf)+'K'+str(K)+'/run'+str(run)
        else:
            #name = '/home/chew/outputdata/2DRD/oriP/kfac'+str(kaf)+'/run'+str(run)
            name = '/home/chew/outputdata/2DRD/oriP/kf'+str(kf)+'K'+str(K)+'/run'+str(run)
        #filename=open(name,'w')
        #np.savetxt(name,np.column_stack((out[0],out[1])),delimiter=',',fmt='%s')
        #filename.close()          
        return 
    job.update({'run':task_id})
    out=singlerun(**job)
    return 

tid = int(os.environ['SLURM_ARRAY_TASK_ID'])
retval = wrap(job, 1, tid)
filenames = ['/home/chew/notebook/jupyter-notebook/2DRD/tmp/slurm-_t45prf8.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
