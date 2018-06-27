import os
import re
import sys

line_regex = re.compile(".*quality_changed.*video.*")

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsed1.log"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s.log"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as in_file:
        for line in in_file:
            if (line_regex.search(line)):
                out_file.write(line)
