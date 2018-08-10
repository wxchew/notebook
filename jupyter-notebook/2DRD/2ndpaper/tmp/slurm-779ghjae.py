import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-g7gfx8qv.pickle', 'rb') as fin:
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
        td =(2*voxelr)**2/(6*D)
        ori = Real3(0.5*L*2,0,0)
        unit0 = Real3(0,0,L)
        unit1 = Real3(0,L,0)        
        w = spatiocyte.SpatiocyteWorld(Real3(L*2,L,L),voxelr,rng)
        size=tuple(w.calculate_shape(Real3(L*2,L,L),voxelr))
        lx,ly,lz=w.actual_lengths()
        Ns = size[1]*size[2]
        Area= ly*lz
        V=ly*lz*lx
        #if run==1:
        #    print('actual A {}, V{},Ns{},td{}'.format(Area,V,Ns,td))
        w.add_structure(Species('M'),PlanarSurface(ori,unit0,unit1))
        with species_attributes():
            A |  {'D': str(D), 'radius':str(voxelr)}
            B |  {'D': str(D), 'radius':str(voxelr),'location':'M'}

        with reaction_rules():#for spa and egfrd
            A + M > B | ka
            #B > A |kd
            #A+M>M | ka

        m2 = get_model()
        w.bind_to(m2)


        w.add_molecules(Species('A'), NA)
        sim = spatiocyte.SpatiocyteSimulator(w)
        sim.initialize()
        obs=FixedIntervalNumberObserver(td*500,['A'])
        sim.run(duration,obs)        
        tlogs,nalog=np.array(obs.data()).T
        return tlogs,nalog,V,Area,Ns
    job.update({'run':task_id})
    out=singlerun(**job)
    return out

tid = int(os.environ['SLURM_ARRAY_TASK_ID'])
retval = wrap(job, 1, tid)
filenames = ['/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-2jh1k1tm.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-cgcdbpqz.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-9s46q9vq.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-bj_xcf4x.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ydadmxiu.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-c9kz6p00.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-f0do4iu0.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-xssacr1y.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-x1e9fcpq.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-vzgps2f2.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-q1gikpev.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-h_92w_6z.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-gg0vuney.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-3e7_btx3.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-f54zj1g5.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-_x8x02s9.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-saylqhp9.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-anys6ezx.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ub5migy0.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-q0i7aru3.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-yeg275a6.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-79oqlyha.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-evis4um0.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-5076ebfy.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-_5abywbs.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-gvg9jo5o.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-0zc3top4.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-88zfb3xx.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-99fras6n.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-fcixbavr.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-vt_nc584.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-pup2po_g.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-rnbnefln.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-xi9tse01.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-12u78ah4.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-8ilmxcll.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-3euqvy3m.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-sg3irsvh.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-8jg2qxow.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-6heb78bw.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-cwwag325.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-yccjsc2a.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-g1ljcb61.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-qevttur9.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-m6n_8ysa.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-dtd13iaz.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-m_umeqrr.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-408ww8ob.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-sdhnzt5f.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-hvwez5d9.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-5auwu25p.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-nunr1j9f.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-gj4ppk7c.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ru55yut3.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-qxr_13rs.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-kxj8xxiw.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-exzfnnk1.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ept1ra1t.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-3e9pw5ma.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-sf5zpxv4.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-_4yh_8n1.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-o5vkf8sg.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-b2y13cky.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-zmb72j23.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-sogy6cs5.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-mmolbd3k.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-wiwzx5jq.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-2uqhjdag.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-gkkqmkik.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-__wembmr.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-y443jppp.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-rtvuykjp.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-fomidpvy.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-yp3w4s25.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-q67noc1r.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-xh61k8no.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-giyn5nz7.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-9333d6cm.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-bdo8nuzk.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-n4qk2niw.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-8hsnfnuh.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ah3ln18n.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-6ncev_tj.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-d4zpblio.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-4t6vfolr.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-x74csoqt.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-x1dc88o_.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-1ztbllzc.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-a3n3aumd.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-gu9zq5u7.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-p5fuitiy.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-lhtpxjty.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-g423kcsi.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-vrd578ya.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-4fl3wlc6.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-zi6b7nzp.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-dm1w72g2.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-azpkcz_a.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-u28du2d9.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-v1c_m1ue.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
