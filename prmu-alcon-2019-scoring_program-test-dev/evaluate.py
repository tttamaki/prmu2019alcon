#!/usr/bin/env python
from __future__ import print_function, division
import sys, os, os.path
import numpy as np
import pandas as pd
import subprocess
import time

print('Python version', sys.version)
print('numpy version', np.__version__)
print('pandas version', pd.__version__)

# try:
#     print('uname', subprocess.call(['uname', '-a']))
# except:
#     pass
# try:
#     print('free', subprocess.call(['free', '-h']))
# except:
#     pass
# try:
#     print('/proc/cpuinfo', subprocess.call(['cat', '/proc/cpuinfo']))
# except:
#     pass

input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res') 
truth_dir = os.path.join(input_dir, 'ref')

print('===== SYSTEM INFO =====')

print('input_dir', input_dir)
print('truth_dir', truth_dir)
print('output_dir', output_dir)
print('submit_dir', submit_dir)

try:
    print('listdir(input_dir)', os.listdir(input_dir))
except:
    pass

try:
    print('listdir(submit_dir)', os.listdir(submit_dir))
except:
    pass

try:
    print('listdir(truth_dir)', os.listdir(truth_dir))
except:
    pass

if not os.path.isdir(submit_dir):
	print("%s doesn't exist" % submit_dir)

print('=======================')



if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):


    val_submit_file = os.path.join(input_dir, 'res', 'test_prediction.csv')
    val_gt_file = os.path.join(input_dir, 'ref', 'prmu-alcon-2019-reference', 'groundtruth_test.csv')

    if not os.path.exists(val_submit_file):
        print('submission file [test_prediction.csv] was not found. Error. Exit.')
        sys.exit()

    print('submission file [test_prediction.csv] found')
    st = time.time()

    df_val_pred = pd.read_csv(val_submit_file, index_col=0, header=0, names=['ID', 'pred1', 'pred2', 'pred3'])
    df_val_gt = pd.read_csv(val_gt_file, index_col=0, header=0, names=['ID', 'gt1', 'gt2', 'gt3'])

    print('submissin file has', len(df_val_pred), 'lines')
    print('reference file has', len(df_val_gt), 'lines')

    df_val_pred = df_val_pred.sort_index().drop_duplicates(keep='first')
    df_val_gt = df_val_gt.sort_index().drop_duplicates(keep='first')

    df_val_all = pd.concat([df_val_pred, df_val_gt], axis=1)    
    df_val_all['test1'] = (df_val_all.pred1 == df_val_all.gt1)
    df_val_all['test2'] = (df_val_all.pred2 == df_val_all.gt2)
    df_val_all['test3'] = (df_val_all.pred3 == df_val_all.gt3)
    df_val_all['test123'] = (df_val_all.test1 & df_val_all.test2 & df_val_all.test3)
        

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, 'scores.txt')              
    output_file = open(output_filename, 'w')

    score = df_val_all.test123[:3000].mean() # for test-dev
    # score = df_val_all.test123[3000:].mean() # for test-challenge
    # score = df_val_all.test123.mean()
    # score2 = (df_val_all.test1.mean() + df_val_all.test2.mean() + df_val_all.test3.mean()) / 3

    output_file.write("score: %.4f\n" % score)
    print('score', score)

    output_file.close()

    et = time.time() - st
    print('Elapsed time', et)


try:
    print('listdir(output_dir)', os.listdir(output_dir))
except:
    pass
