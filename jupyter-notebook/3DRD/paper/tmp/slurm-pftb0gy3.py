import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-8o0gkrz4.pickle', 'rb') as fin:
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
filenames = ['/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-89p9d_tf.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-mbz6itdu.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-x5knyeaj.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-nal_unnw.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-gup5a7kw.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-nc45er49.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-8rf6_ae6.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-v3obqns8.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-bljt11ld.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-59586mef.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
