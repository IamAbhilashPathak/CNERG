import sys
import os

if len(sys.argv) < 4:
    print >> sys.stderr, "Use %s <video id> <mode quic|http> <duration in sec>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]
duration = float(sys.argv[3])

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_quality_time.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsed2.txt"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as data:
         x = []
         y = []
         for line in data:
             p = line.split()
             x.append(int(p[2]))
             y.append(float(p[3]))
        
         length = len(x)
         unique_list = []
         for q in x:
             if q not in unique_list:
                unique_list.append(q)
         MaxQ = max(unique_list)
         #print MaxQ
         playback_time = [0.0] * (MaxQ+1)
         for i in range(length-1):
             playback_time[x[i]] += int(y[i+1]) - y[i]
         playback_time[x[length-1]] += duration - y[length-1]

         ssum = 0.0
         for i in range(MaxQ+1):
             out_file.write ("%i %f\n" % (i, playback_time[i]))
             ssum += playback_time[i]
         print ssum
 
