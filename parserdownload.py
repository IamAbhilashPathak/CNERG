import os
import re
import sys

line_regex = re.compile("download_complete.*startTime\":([0-9]*?),.*video.*duration\":(.*),\"t.*quality\":([0-9]*?),.*bytesLoaded\":([0-9]*?),.*curTime\":([0-9]*?.[0-9]*?)\}")

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parseddownload.txt"%(vid, mode))
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
		out_file.write(c + " " + a + " " + b + " " + d + " " + e + "\n")
            
