import os
import re
import sys

line_regex1 = re.compile(".*metric_updated.*")
line_regex2 = re.compile("curTime\":([0-9]*?.[0-9]*?),")

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]
time = 1000 #for first mismatch

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsedmet.log"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s.log"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as in_file:
        for line in in_file:
            if (line_regex1.search(line)):
                x = line_regex2.search(line).group(1)
                if (x != time):
                    out_file.write(line)
                    time = x
