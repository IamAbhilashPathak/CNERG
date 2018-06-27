import sys
import os

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <mode quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_quality_change.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsed2.txt"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as data:
         x = []
         for line in data:
             p = line.split()
             x.append(int(p[2]))
        
         inc = 0
         dec = 0
         length = len(x)

         for i in range(length-1):
             if (x[i] < x[i+1]):
                 inc += 1
             else:
                 dec += 1
         out_file.write ("%i %i" %(inc, dec))
 
