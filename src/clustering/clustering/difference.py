import os
import nibabel as nb
import numpy as np
import glob
from variables import subjects, resultsdir
import matplotlib.pyplot as plt

def find_cluster(subject_id,hemi,sim,cluster_type,n_clusters,session):
    filestring = '/volumes/clustered/_hemi_{0}/_session_{1}/_subject_id_{2}/_sim_{3}/_cluster_{4}/_n_clusters_{5}'
    filepath = resultsdir+filestring.format(hemi,session,subject_id,sim,cluster_type,n_clusters)
    os.chdir(filepath)
    clustermap = nb.load(''.join(glob.glob('*.nii'))).get_data()
    return clustermap

if __name__ == '__main__' :
    Map1=find_cluster(subjects[0],'lh','eta2','hiercluster','7','session1')
    Map2=find_cluster(subjects[0],'lh','eta2','hiercluster','7','session2')
    
    pairs = []
    matrix = np.zeros(shape=(np.max(Map1),np.max(Map1)))
    for i, cluster in enumerate(Map1):
        pairs.append(str([cluster,Map2[i]]))
        if cluster>=0:
            matrix[cluster-1][Map2[i]-1] = matrix[cluster-1][Map2[i]-1]+1
    #n, bins, patches = plt.hist(pairs)
    #plt.show()
    #plt.acorr(matrix)
