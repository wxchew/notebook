import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-k4yyud0h.pickle', 'rb') as fin:
    job = pickle.load(fin)
pass
from numpy import *
from ecell4 import *
from math import *
def wrap(job,job_id,task_id):
    def singlerun(kaf,C,run):
        import numpy as np
        rng = GSLRandomNumberGenerator()
        rng.seed(run)
        rm = 0.005
        R=2*rm
        voxelr=rm*1.0208582  
        L = 1.
        D = 1
        kd= 4.0*math.pi*D*2*rm
        ka = kaf*kd
        kon = (ka*kd)/(ka+kd)
        tm =(2*voxelr)**2/(6*D)
        #print(tm)
        Vac=spatiocyte.SpatiocyteWorld.calculate_volume(ones()*L,voxelr)
        #print(Vac)
        N = int(C*Vac)
        assert (N>0)
        w = spatiocyte.SpatiocyteWorld(ones()*L,voxelr)

        (c,r,l)=w.shape()
        Nev=(c - 2) * (r - 2) * (l - 2)
        #print('N',N,float(N)/Nev)
        with species_attributes():
            A |  {'D': str(0), 'radius':str(voxelr)}
            B |  {'D': str(D), 'radius':str(voxelr)}

        with reaction_rules():#for spa and egfrd
            A + B > B | ka

        m2 = get_model()

        w = spatiocyte.SpatiocyteWorld(ones()*L,voxelr,rng)
        w.bind_to(m2)
        na=1
        w.add_molecules(Species('A'), na)
        w.add_molecules(Species('B'), N)
        sim = spatiocyte.SpatiocyteSimulator(w)
        sim.initialize()
        simt=0
        while na==1:
            sim.step()
            na = w.num_particles_exact(Species('A'))
            simt=sim.t()
        return simt,1./kon/C,float(N)/Nev,N
    job.update({'run':task_id})
    out=singlerun(**job)
    return out

tid = int(os.environ['SLURM_ARRAY_TASK_ID'])
retval = wrap(job, 1, tid)
filenames = ['/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-_7l3uglj.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-dlzp1ltp.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ryupudy1.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-6u3a774i.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-bonvpuux.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-lic1v2gw.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-6212ih41.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-9grsrcni.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-hfrjl1c7.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-3oowtyw4.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-o9qhva_0.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-rf8cw6it.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-x1cq5asl.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-rqqt_z8k.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ynu0dxqr.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-_1r1pm5g.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-u8hq56xi.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-4sdqwg9t.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-48jgfcb1.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-al_9zwz8.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-zc102hyr.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-hf7aqxum.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-d5meuq4e.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-xh1cn017.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-wowft9lt.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ie0lyz_r.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-_b6owgze.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-2wsue1q6.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-q3ehjz3v.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-cbp_p3h6.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-jz7hnptg.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-8k6_0wv7.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-831dzmuh.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ak3z5kyi.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-juhcqsb4.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-0rxlo4fs.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-b2c2qc9g.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-y67h9jqt.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-qltk5igb.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-0e4p9_yc.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-xvvfmomn.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-bvp1gzni.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-smm5enm_.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-7gf0rii9.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-svn9ued0.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-yjr_xfq1.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-7mmhaoit.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-v6n19rhw.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-bbayk9_i.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-23bk8k1i.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-efmaz8mr.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-_ea6nji_.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-vtuwo7_i.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-iecntg3d.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-vfqjos9n.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-vl_13y3e.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ai8ln7ug.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ce2u_noy.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-acan1ppy.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ocifs5ya.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-tztodmmf.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-rjv4wu1h.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-g8ll1p0l.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-lruzq_kr.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ag06sgb4.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-_bo3sfo0.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-0bqx9qa0.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-0eu0zgw6.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-cav4gs34.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-226tsc2l.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-65xf97g_.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-3vm__zdz.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-i1j81ht7.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-m95dq6zc.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-vr2cpt9w.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-6_arwvoo.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-qi7azqet.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-qln96dkr.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-o9qbqao1.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-mf44d17d.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-d7lne363.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-51vy1wfd.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-0jawk63v.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-1_ctbkr5.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-uuf_a7y2.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-rnmefgsi.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-as5kvylk.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-0snu_dcp.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-a1ap1_bf.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-04rhe9s8.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-w6wh7e36.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-k0lc0ji3.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-4m4zdlg2.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-id3t78e4.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-k4teq21u.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-p7uj55tk.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-fuedgeg2.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-wci7eunm.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-6gkl4b8d.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-rzc4xa_u.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
