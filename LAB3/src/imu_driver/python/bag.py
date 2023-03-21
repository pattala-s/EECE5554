import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from bagpy import bagreader

imu_data_5hrbg=bagreader('/home/srinidhi/EECE5554/LAB3/src/Data/known.bag')

imu_data_5hrf= imu_data_5hrbg.message_by_topic('/imu')

df = pd.read_csv(imu_data_5hrf)
