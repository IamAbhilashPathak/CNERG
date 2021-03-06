import os
import re
import sys

line_regex1 = re.compile(".*video Average throughput.*")
line_regex2 = re.compile(".*\[([0-9]*?)\] T.*video Average throughput ([0-9]*?) kbps.*")

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsedthroughput.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s.log"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as in_file:
        for line in in_file:
            if(line_regex1.search(line)):
               x = line_regex2.search(line).group(1)
               y = line_regex2.search(line).group(2)
               a = (float(x))/1000
               b = int(y)
               out_file.write ("%f %i \n" % (a, b))

