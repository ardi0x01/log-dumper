from importlib.resources import path
import sys, json, os
from sh import tail


def write_data(path, typeFormat, pathOut = None):
    arr = []
    print("Path out : ", pathOut)
    
    for line in tail("-q", path, _iter = True):
        arr.append(line)
    if(pathOut == None): pathOut = 'output.txt'
    else: pathOut = os.path.join(pathOut, 'output.txt')

    f = open(pathOut, 'w')

    if(typeFormat == 'text'):
        for i in range(len(arr)):
            f.write(arr[i])
    elif(typeFormat == 'json'):
        jsonToArr = {"logs" : arr}
        f.write(json.dumps(jsonToArr))

def write_log(path, paramArr):
    if (paramArr[0] == '-h'):
        print("\n") 
        print("== GUIDE ==")
        print("Parameter (path_log, flag_type, type)")
        print("also for create in path just add 1 more parameter after 'type' parameter")   
        print("\n") 
        return
    
    flagType = paramArr[1]
    typeParam = paramArr[2]
    flagOutput = paramArr[3]
    pathFull = paramArr[4]
    
    print("Write logs...", typeParam)
    
    if (flagType == '-t'):
        if (flagOutput == '-o'):
            if(typeParam == None):
                write_data(path, 'text', pathFull)
            else:
                write_data(path, typeParam, pathFull)
        else:
            write_data(path, typeParam)
    elif(flagType == '-o'):
        pathParam = typeParam
        write_data(path, "text", pathParam)
    elif (flagType == None):
        write_data(path, 'text')
    

try:
    pathFolder = sys.argv[1]
    argsArr = []
    for i in range(1, len(sys.argv)):
        argsArr.append(sys.argv[i])
    
    numNeeded = len(argsArr) - 6

    for i in range(abs(numNeeded)):
        argsArr.append(None)
   
    write_log(pathFolder, argsArr)


except ValueError:




        

