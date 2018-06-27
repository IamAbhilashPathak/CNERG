import os
import re
import sys

line_regex1 = re.compile(".*\[([0-9]*?)\] AbrController \(video\).*\(buffer: ([0-9]*?.[0-9]*?)\).*")
line_regex2 = re.compile(".*\[([0-9]*?)\].*download_complete.*startTime\":([0-9]*?),.*video.*")

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_rebuffer.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s.log"%(vid, mode))

download_start_time = []
download_end_time = []
buffer_sec = []
check1 = 1
check2 = 1 

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as in_file:
        for line in in_file:
            if (line_regex1.search(line)):
                x = line_regex1.search(line).group(1) 
                y = line_regex1.search(line).group(2)
                if (check1 == 1):
                    download_start_time.append(x)
                    buffer_sec.append(y)
                    check1 = 0
                else:
                    download_start_time.pop(-1)
                    buffer_sec.pop(-1)
                    download_start_time.append(x)
                    buffer_sec.append(y)
                check2 = 1
              
            elif (line_regex2.search(line)):
                x = line_regex2.search(line).group(1)
                if (check2 == 1):
                    download_end_time.append(x)
                    check2 = 0
                else:
                    download_end_time.pop(-1)
                    download_end_time.append(x)
                check1 = 1 
                
        for i in range(len(buffer_sec)-1):
            if (float(buffer_sec[i]) != 0):
                time = (float(download_end_time[i]) - float(download_start_time[i]))/1000
                out_file.write(str(time) + " " + buffer_sec[i] + "\n") 
