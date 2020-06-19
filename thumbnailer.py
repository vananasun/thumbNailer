import os
import sys
import subprocess
import shlex
import time



if (len(sys.argv) < 3):
    print("Usage: thumbnailer.py <output_dir> <file1> [file2] [file3] ...")
    sys.exit();
output_dir = sys.argv[1]
sys.argv.pop(0)
sys.argv.pop(0)



resolutions = [
    [ 160 ,   90 ],
    [ 640 ,  360 ],
    [ 1024,  576 ],
    [ 1280,  720 ],
    [ 1920, 1080 ],
    [ 2560, 1440 ],
    [ 3200, 1800 ],
    [ 3840, 2160 ]
]
extensions = [ 'webp', 'jpg' ]
quality = 50



for filepath in sys.argv:
    for size in resolutions:
        for ext in extensions:
            outputpath = output_dir + "/" + os.path.splitext(os.path.basename(filepath))[0]
            outputpath += '_' + str(size[0]) + 'x' + str(size[1]) + '.' + ext
            # print("Processing " + filepath + " to " + outputpath)
            os.system('echo ' + "Processing " + filepath + " to " + outputpath)

            args = "convert ";
            args += "-resize \""+str(size[0])+"x"+str(size[1])+"^\" "
            args += "-gravity center "
            args += "-crop "+str(size[0])+"x"+str(size[1])+"+0+0 "
            args += "+repage "
            args += "-quality " + str(quality) + " "
            args += "\"" + filepath + "\" "
            args += "\"" + outputpath + "\""

            os.system(args)
