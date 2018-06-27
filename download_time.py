import sys
import os

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <mode quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_download_time.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parseddownload.txt"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as data:
         x = []
         y = []
         z = []
         for line in data:
             p = line.split()
             x.append(int(p[0]))
             y.append(float(p[2]))
             z.append(int(p[3]))
         length = len(x)
         unique_list = []
         for q in x:
             if q not in unique_list:
                unique_list.append(q)
         MaxQ = max(unique_list)
         #print MaxQ
         download_time = [0.0] * (MaxQ+1)
         download_bytes = [0] * (MaxQ+1)
         for i in range(length):
             download_time[x[i]] += y[i]
             download_bytes[x[i]] += z[i]

         ssum = 0
         tsum = 0.0
         for i in range(MaxQ+1):
             out_file.write ("%i %f %i\n" % (i, download_time[i], download_bytes[i]))
             ssum += download_bytes[i]
             tsum += download_time[i]
         print ssum
         print tsum
 
