from tests.testData import SensorData
import numpy as np

t = np.arange(1.0, 1201.0)


sensor_ex = SensorData(t)

temps = np.clip(np.array([sensor_ex.outer_heat(i) for i in range(len(t))]), sensor_ex.t_start, 70)
