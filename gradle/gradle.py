import os
import subprocess

def gradle(cwd):

    cmds = ['gradle', 'test', '--rerun-tasks']

    #assn_name = cwd.split('/')[-1]

    p = subprocess.Popen(cmds, stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE,
                         cwd=cwd)
    out, err = p.communicate()

    if ':compileJava FAILED' in out:
        err = 2
    elif 'BUILD SUCCESSFUL' in out:
        err = 0
    else:
        err = 1

    return out, err

if __name__ == '__main__':
    print gradle('/Users/tristanhearn/Dropbox/adj/BW/hw/hw2')