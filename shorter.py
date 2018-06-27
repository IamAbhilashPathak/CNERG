import os
import re
import sys

line_regex = re.compile("Native video element event: ended")

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <quic|http>"
    exit(2)

flag = 0
vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s.log"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "chrome_debug_%s_%s.log"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as in_file:
        for line in in_file:
            out_file.write(line)
            if (line_regex.search(line)):
                flag = 1
                break
        if (flag == 0):
            print ("Play this video %s_%s again...."%(vid,mode))        
