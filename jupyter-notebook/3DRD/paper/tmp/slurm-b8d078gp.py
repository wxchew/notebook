import sys
import os
import pickle
with open('/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-bb311uuu.pickle', 'rb') as fin:
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
filenames = ['/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-uy8xnnhw.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-twlifbfw.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-p0n0tyrh.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-bxpetmpo.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-uh8z46f8.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-vxmsbzuo.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-_2e4ou9u.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-08omkw7x.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-50ieldbh.pickle', '/home/chew/notebook/jupyter-notebook/3DRD/paper/tmp/slurm-ce6i1_rj.pickle']
pickle.dump(retval, open(filenames[tid - 1], 'wb'))
