import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-v_r37ln1.pickle', 'rb') as fin:
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
filenames = ['/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-6f2vh17w.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-uw3pn0t_.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-mcqk3195.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-_syy9qea.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-g7pd6ja5.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-5j2cs3vi.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-xogolwch.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-tvaq34v4.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-9jyoeg0u.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-m6utg0ru.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
