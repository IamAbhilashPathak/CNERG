import sys
import os

if len(sys.argv) < 3:
    print >> sys.stderr, "Use %s <video id> <mode quic|http>"
    exit(2)

vid = sys.argv[1]
mode = sys.argv[2]

output_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_response_time.txt"%(vid, mode))
input_filename = os.path.join(os.path.expanduser('~'), vid, "%s_%s_parsedresponse.txt"%(vid, mode))

with open(output_filename, "w") as out_file:
    with open(input_filename, "r") as data:
         a = []
         b = []
         c = []
         d = []
         e = []
         f = []
         g = []
         h = []
         for line in data:
             p = line.split()
             a.append(int(p[0]))
             b.append(int(p[1]))
             c.append(int(p[2]))
             d.append(float(p[3]))
             e.append(int(p[4]))
             f.append(int(p[5]))
             g.append(int(p[6]))
             h.append(float(p[7]))
        
         sum = 0.0
         avg = 0.0
         num = len(a)

         for i in range(num):
             if (a[i] == e[i]):
                 sum += (((f[i]-b[i])*3600) + ((g[i]-c[i])*60) + (h[i]-d[i]))  
             else:
                 sum += ((((f[i]+24)-b[i])*3600) + ((g[i]-c[i])*60) + (h[i]-d[i]))
         avg = sum / num
         out_file.write ("%f" %(avg))
