import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/tmp/slurm-_5rdqka6.pickle', 'rb') as fin:
    job = pickle.load(fin)
pass
from numpy import *
from ecell4 import *
from math import *
def wrap(job,job_id,task_id):
    def singlerun(kaf,run):
        import numpy as np
        import time
        time.sleep(10)
        rng = GSLRandomNumberGenerator()
        #run+=30000
        rng.seed(run)
        voxelr=0.005
        L = 1.#350*rm
        w = spatiocyte.SpatiocyteWorld(ones()*L,voxelr)
    return     

tid = int(os.environ['SLURM_ARRAY_TASK_ID'])
retval = wrap(job, 1, tid)
filenames = ['/home/chew/notebook/jupyter-notebook/tmp/slurm-8667fnf2.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-80dv5d0e.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-teamhq7i.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-1642_gru.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-90ley72_.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-b1m006um.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-xo5ey_cs.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-t9b_937o.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-mxfi96rb.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-7rprsnfc.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-u_agmg_h.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-ub8wm663.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-apqvmgdx.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-9c5f8j9c.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-ikbuy3fg.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-n9mad_z6.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-t5el8csa.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-mc2638ay.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-uxnjq7sq.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-u1q72upy.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-wcx903mc.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-isrvi59l.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-ggslbhvs.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-semaqll5.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-ywsohrts.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-qdua883z.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-oa3oj_48.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-alltuhvi.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-7muyj4tv.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-1pr4pshs.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-hy7o1dqt.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-5cze2n4k.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-3vfc608q.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-6ep57v0h.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-bs9vodap.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-o3_z6840.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-6wvn50jm.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-6bpacvxv.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-wyv6eokj.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-zwl3pdd7.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-4vre7vrx.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-cb3b3wgk.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-m9mz_3jb.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-1112o0ny.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-z55tg2d3.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-8c383jbu.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-g0jqy80m.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-20_t2jpw.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-zx65q13n.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-zkp1qqt0.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-g_khgvpr.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-2lh_8ie9.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-pjlbbs4f.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-1l9u5olj.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-4k9sbfwd.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-wie3w_in.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-gifjrcml.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-at24kikd.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-qy4mj018.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-99ak5bip.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-3rjesxz1.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-8zlarmg3.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-ggoxvieh.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-ongd8sq4.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-sffy4571.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-45jxld5a.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-nabzg5h2.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-uhr2uah6.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-36xez5rz.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-wtqiiwc9.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-erjeu01_.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-8k4wa4jp.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-xx1lhpdc.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-jub7p47i.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-lav7bcs6.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-klbu5wca.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-ud35bkgk.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-c5f70yfd.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-v9hmajv8.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-q7vx0sf7.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-sy3jm4y2.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-rsazsakx.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-rrf3a61t.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-075nmn3e.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-1kwgu8jn.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-pk1l9ovr.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-xx0hh1wp.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-val7rmfs.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-nyrkp_pp.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-ki73hmki.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-ud0463yu.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-qfcgei0_.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-4im2mm14.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-enx0u3mn.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-4ygsfoxw.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-1uok9iz8.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-hafm4i44.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-5xz0hof1.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-frgpoep4.pickle', '/home/chew/notebook/jupyter-notebook/tmp/slurm-v63tvn5l.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))