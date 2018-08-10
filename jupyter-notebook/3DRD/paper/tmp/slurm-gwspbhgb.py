import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-1dxwxjor.pickle', 'rb') as fin:
    job = pickle.load(fin)
pass
def singlerun(job, job_id, task_id):
    import ecell4.util
    import ecell4.extra.ensemble
    rndseed = ecell4.extra.ensemble.getseed(job.pop('myseed'), task_id)
    job.update({'return_type': 'array', 'rndseed': rndseed})
    data = ecell4.util.run_simulation(**job)
    return data

tid = int(os.environ['SLURM_ARRAY_TASK_ID'])
retval = singlerun(job, 1, tid)
filenames = ['/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-8m1yv_ii.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-mc301j7p.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-emgs4sh8.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-aw57ut9_.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-jxxl84e5.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-0jo761vu.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-j_lxhe7x.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-g0yps8qy.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-mtfp5_kb.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ygb5if6i.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
