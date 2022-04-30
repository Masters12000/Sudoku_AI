import psutil # needs to be installed
import os
"""print(psutil.cpu_percent(1))
print(psutil.virtual_memory())
dict(psutil.virtual_memory()._asdict())
print(psutil.virtual_memory().percent)
python_process = psutil.Process(os.getpid())
print(f"memory info: {python_process.memory_info()[0]/2.**30}")
psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
"""

import os
import psutil

print(psutil.cpu_percent(1))
print(psutil.cpu_stats())
print(psutil.cpu_freq())
print(psutil.cpu_times().user)