from __future__ import print_function
from fungsi import averageCpuLoad, averageMemoryLoad
# import time
import psutil

# memory load
memories = []
i = 10
while i > 0:
    memories.append(psutil.virtual_memory().percent)
    i -= 1
print (memories)
avgMemory = averageMemoryLoad(memories)
print (avgMemory)

# cpu load
cpus = []
i = 10
while i > 0:
    cpus.append(psutil.cpu_percent(interval=1))
    i -= 1
print(cpus)
avgCpu = averageCpuLoad(cpus)
print(avgCpu)