# Global Variable
MAX = 70

def avg(value):
    length = len(value)
    sum = 0
    for x in value:
        sum += x
    result = sum/length
    return result

def averageCpuLoad(loads):
    return avg(loads)

def averageMemoryLoad(loads):
    return avg(loads)

def dynamicThreshold(hostList, vmList):
    migrationList = []
    vmList.sort()
    for h in hostList:
        hUtil = h['util']
        bestFitUtil = MAX
        bestFitVm = None
        while hUtil > h['upThresh']:
            for vm in vmList:
                if vm > hUtil - h['upThresh']:
                    t = vm - hUtil + h['upThresh']
                    if t < bestFitUtil:
                        bestFitUtil = t
                        bestFitVm = vm
                else:
                    if bestFitUtil == MAX:
                        bestFitVm = vm
                    break
            hUtil = hUtil - bestFitVm
            migrationList.append(bestFitVm)
            vmList.remove(vm)
    return migrationList