import os
import re
import sys

line_regex1 = re.compile("\[([0-9]*?)\] N")
line_regex2 = re.compile("\[([0-9]*?)\] B")
line_regex3 = re.compile("Quality\":([0-9]*?),\"curTime\":([0-9]*?.[0-9]*?)\}")
 
if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

check = 1 
# 0 for playing ; 1 for stalling

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsed4.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsed3.log"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as in_file:
        for line in in_file:
            if (line_regex1.search(line) and check == 0):
               x = line_regex1.search(line).group(1)
               out_file.write(x + "\n")
               check = 1
            elif (line_regex2.search(line) and check == 1):
               x = line_regex2.search(line).group(1)
               out_file.write(x + " ")
               check = 2
            elif (check == 2):
               x = line_regex3.search(line).group(1)
               y = line_regex3.search(line).group(2)
               out_file.write(x + " " + y + "\n")
               check = 0

