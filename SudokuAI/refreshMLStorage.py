import os
import shutil

def refresh():
    """
    Refreshes the Machine Learning training dataset with its equivalent non-trained dataset,
    balancing results between runs
    @return: None
    """
    ML = [ "ML_1000", "ML_2500", "ML_5000", "ML_10000", "ML_25000", "ML_50000", "ML_100000", "ML_250000", "ML_500000", "ML_1000000" ]
    for ml in ML:
        root_src_dir = "Machine_Learning/Without_Training/" + ml + ".txt"
        root_dst_dir = "Machine_Learning/With_Training/" + ml + ".txt"

        if os.path.isdir(root_dst_dir):
            shutil.rmtree(root_dst_dir)

        elif os.path.isfile(root_dst_dir):
            os.remove(root_dst_dir)

        shutil.copy(root_src_dir, root_dst_dir)


refresh()
