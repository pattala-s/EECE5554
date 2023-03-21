import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bagpy import bagreader

known_bag= bagreader('/home/srinidhi/EECE5554/LAB3/src/Data/known.bag')

known_bag= known.bag.message_by_topic('/imu')

df = pd.read_csv(imu_data_5hrf)
