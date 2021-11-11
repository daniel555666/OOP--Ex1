# import datetime
# import time
import subprocess
#import sys
# timestamp = datetime.datetime.now().time() # Throw away the date information
# time.sleep(1)
# start = datetime.time(7, 55)
# end = datetime.time(12)
subprocess.Popen(["powershell.exe", "java -jar lib\Ex1_checker_V1.2_obf.jar 1111,2222,3333 input\Ex1_input\Ex1_Buildings\B5.json  output.csv  out.log"])