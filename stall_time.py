import sys
import os

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <mode quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

check = 0

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_stall_time.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsed4.txt"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as data:
         x = []
         y = []
         z = []
         for line in data:
             if (check == 0):
                p = line.split()
                x.append(float(p[0]))
                y.append(int(p[1]))
                z.append(float(p[2]))
                check = 1
             else :
                x.append(float(line))
                check = 0

    
         num_stall = len(x)/2
         print num_stall

         stall_time = []
         for i in range(0,len(x),2):
             stall_time.append((x[i+1] - x[i]) / 1000)

         for i in range(num_stall):
             out_file.write ("%f %i %f\n" % (stall_time[i], y[i], z[i]))
 
