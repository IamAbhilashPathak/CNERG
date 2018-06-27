import os
import re
import sys

line_regex = re.compile("requestStartDate\":\"[0-9]*?-[0-9]*?-([0-9]*?)[A-Z]*?([0-9]*?):([0-9]*?):([0-9]*?.[0-9]*?)Z\",\"firstByteDate\":\"[0-9]*?-[0-9]*?-([0-9]*?)[A-Z]*?([0-9]*?):([0-9]*?):([0-9]*?.[0-9]*?)Z\",")

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsedresponse.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parseddown.log"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as in_file:
        for line in in_file:
            if (line_regex.search(line)):
	        a = line_regex.search(line).group(1)
		b = line_regex.search(line).group(2)
                c = line_regex.search(line).group(3)
		d = line_regex.search(line).group(4)
		e = line_regex.search(line).group(5)
                f = line_regex.search(line).group(6)
		g = line_regex.search(line).group(7)
		h = line_regex.search(line).group(8)
		out_file.write(a + " " + b + " " + c + " " + d + " " + e + " " + f + " " + g + " " + h + "\n")
            
