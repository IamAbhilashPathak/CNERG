import sys
import os

output_filename = os.path.normpath("totalstalls.txt")

with open(output_filename, "w") as out_file:
    with open("times", "r") as data:
         x = []
         for line in data:
             p = line.split()
             x.append(p[0])
         totalfiles = len(x)
          
         http_time = [0] * 10
         quic_time = [0] * 10

         for i in range(totalfiles):
             filename1 = os.path.join(os.path.expanduser('~'), x[i], "%s_http_stall_time.txt"%(x[i]))
             with open(filename1, "r") as httpfile:
                  qindex = []
                  for l in httpfile:
                      p = l.split()
                      qindex.append(int(p[1]))                
                  #MaxQ = max(qindex)
                  #print MaxQ
                  stalls = len(qindex)
                  for j in range(stalls):
                      http_time[qindex[j]] += 1
  
             filename2 = os.path.join(os.path.expanduser('~'), x[i], "%s_quic_stall_time.txt"%(x[i]))
             with open(filename2, "r") as quicfile:
                  qindex = []
                  for l in quicfile:
                      p = l.split()
                      qindex.append(int(p[1]))                
                  #MaxQ = max(qindex)
                  #print MaxQ
                  stalls = len(qindex)
                  for j in range(stalls):
                      quic_time[qindex[j]] += 1   
         for k in range(10):
             if (http_time[k] != 0 or quic_time[k] != 0):
                  out_file.write ("%i %i %i\n" % (k, http_time[k], quic_time[k]))
