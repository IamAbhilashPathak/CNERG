import os
import re
import sys

line_regex = re.compile("\[([0-9]*?)\] A.*bitrate\":([0-9]*?),.*qualityIndex\":([0-9]*?)\},\"curTime\":([0-9]*?.[0-9]*?)\}")
  
if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsed2.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsed1.log"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as in_file:
        for line in in_file:
	    a = line_regex.search(line).group(1)
            x = float(a)/1000
            b = line_regex.search(line).group(2)
            y = int(b)/1000
            c = line_regex.search(line).group(3)
            d = line_regex.search(line).group(4)

            out_file.write ("%f %i %s %s \n" % (x, y, c, d))
          



