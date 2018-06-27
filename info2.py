import sys
import os

output_filename = os.path.normpath("info2.sh")

with open(output_filename, "w") as out_file:
    with open("times") as data:
         x = []
         y = []
         for line in data:
             p = line.split()
             x.append(p[0])
             y.append(p[1])
         length = len(x)

         out_file.write ("#!/bin/bash\n")
         for i in range(length):
             #out_file.write ("python ~/parsers/shorter.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/shorter.py" + " " + x[i] + " " + "quic" + "\n") 

             #out_file.write ("mv ~/%s/chrome_debug_%s_http_parsed.log ~/%s/%s_http.log"%(x[i], x[i], x[i], x[i]) + "\n")
             #out_file.write ("mv ~/%s/chrome_debug_%s_quic_parsed.log ~/%s/%s_quic.log"%(x[i], x[i], x[i], x[i]) + "\n")
             #out_file.write ("rm ~/%s/chrome_debug_%s_http.log"%(x[i], x[i]) + "\n")
             #out_file.write ("rm ~/%s/chrome_debug_%s_quic.log"%(x[i], x[i]) + "\n")

             #out_file.write ("python ~/parsers/parser1.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/parser2.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/quality_change.py" + " " + x[i] + " " + "http" + "\n") 
             #out_file.write ("python ~/parsers/parserthroughput.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/quality_playtime.py" + " " + x[i] + " " + "http" + " " + y[i] + "\n")
             #out_file.write ("python ~/parsers/parser3.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/parser4.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/stall_time.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/parserdown.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/parserdownload.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/download_time.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/parserresponse.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/response_time.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/parser1.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/parser2.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/quality_change.py" + " " + x[i] + " " + "quic" + "\n") 
             #out_file.write ("python ~/parsers/parserthroughput.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/quality_playtime.py" + " " + x[i] + " " + "quic" + " " + y[i] + "\n")
             #out_file.write ("python ~/parsers/parser3.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/parser4.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/stall_time.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/parserdown.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/parserdownload.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/download_time.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/parserresponse.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/response_time.py" + " " + x[i] + " " + "quic" + "\n")

             #out_file.write ("python ~/parsers/qoe_metrics.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/qoe_metrics.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/qoe_metrics1.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/qoe_metrics1.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/qoe_metrics_new.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/qoe_metrics_new.py" + " " + x[i] + " " + "quic" + "\n")
             #out_file.write ("python ~/parsers/rebuffer.py" + " " + x[i] + " " + "http" + "\n")
             #out_file.write ("python ~/parsers/rebuffer.py" + " " + x[i] + " " + "quic" + "\n")
