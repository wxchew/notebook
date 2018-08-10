import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-_d9tuqdp.pickle', 'rb') as fin:
    job = pickle.load(fin)
pass
from numpy import *
from ecell4 import *
from math import *
def wrap(job,job_id,task_id):
    def singlerun(ka,kd,D,NA,L,run,duration,rm,interval,mode):
        import numpy as np
        rng = GSLRandomNumberGenerator()
        rng.seed(run)   
        voxelr=rm    
        LL=4*L
        td =(2*voxelr)**2/(6*D)   
        ori = Real3(0.5*LL,0,0)
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

        with reaction_rules():#for spa and egfrd
            A + M > B | ka
            B > A |kd

        m2 = get_model()
        w.bind_to(m2)
        w.add_molecules(Species('A'), NA)
        sim = spatiocyte.SpatiocyteSimulator(w)
        sim.initialize()
        pid = [p[0] for p in w.list_particles_exact(Species('A'))]
        obs = FixedIntervalTrajectoryObserver(interval,pids=pid,resolve_boundary=False)
        #obs=FixedIntervalNumberObserver(td*500,['A'])
        sim.run(duration,obs)        
        #dat=[tuple(pos) for pos in obs.data()[0]]
        return [obs.data(),obs.t()]
    job.update({'run':task_id})
    out=singlerun(**job)
    return out

tid = int(os.environ['SLURM_ARRAY_TASK_ID'])
retval = wrap(job, 1, tid)
filenames = ['/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ruu5leqf.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-2pti1ea2.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-qr_dvr61.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-__66_ua6.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-o4e5z7p3.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ibhyv26f.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-smz2iibm.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-88cezgas.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-n6yiocp8.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-96_0vzr8.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-fpcnk2a4.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ia99b318.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-s10rmve9.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-35hggoie.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-pphbiss8.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-eqemrjea.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ib9240bx.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-sbvlk70n.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-lv8to0zq.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-gwr1qyf6.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-i__r5kqi.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-716et754.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-9idpghrx.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-7b6sn31d.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-n2_plcrv.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-vcmfyj9m.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ybowyx7r.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-84f6ysnn.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-_vnjbjhg.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-yp1g87pu.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-0_oaen6v.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-lef5b3nb.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-7xjtatx6.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-15qtuie1.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-54xra0hs.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-2vthylpx.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-m7565ajj.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-i4swngte.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-wi3w38bu.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-sq2pd3lr.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-1uakctmt.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-cwq62xmf.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-q31wtjtg.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-pgwzpl55.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-x0ce5har.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-jnxs_26o.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-160qts0i.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-c9lkho62.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-r_pe29tf.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-puq7zci8.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-6srkdlrf.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-gnkrw7ep.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-14wjzmib.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-b6lnf2lp.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-c7as93qm.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-kr9l6gie.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-_qpinhq_.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-yl0ws9f1.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-s1m4qwv_.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-jxuw8o5s.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-jq1aqtcb.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-5p_ttjln.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-in9gzq3v.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-j9uc940x.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-67g8c0ki.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-52u18s7m.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-qnp7n9d0.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-e5biyw14.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-jmlcydh6.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-r2pt5ato.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-k92mdwa9.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-3tc4h65j.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-m811hi1a.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-eni1ea0l.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-lsi_dgty.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-_g4woayp.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-l2nrboln.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-a3czfk4o.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-ndnf1at2.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-9jq1_sxq.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-96y46sya.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-85pfxk_n.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-mhpevwop.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-oh1963ej.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-06i74vba.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-lt8bpyiq.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-aw1c7478.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-xg7wjjvq.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-8nbi6rol.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-16h4pa84.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-qldc2zg8.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-x0lw6bex.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-za2m89pu.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-d3ydrjuw.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-7l19rw5z.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-_lsla95l.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-7jzi8dfc.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-psl4y_9h.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-o0zikey_.pickle', '/home/chew/notebook/jupyter-notebook/2DRD/2ndpaper/tmp/slurm-4l62jjmd.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
