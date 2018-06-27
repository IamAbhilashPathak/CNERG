import subprocess
import sys
import shlex
import shutil
import os
import time

TEMP_CHROME_PROF_DIRECTORY = "/tmp/chrome_prof/"
CMD_SCRIPT = "/tmp/cmd.sh"
FIFO_FILE = "/tmp/chrom_prof_fifo"

def createAndSaveCmd(fpath, cmd):
	fp = open(fpath, "w")
	print >> fp, "#!/bin/bash"
	print >> fp, cmd+" &"
	print >> fp, "pid=$!"
	print >> fp, "mkfifo " + FIFO_FILE
	print >> fp, "cat " + FIFO_FILE
	print >> fp, "kill $pid"
	print >> fp, "wait $pid"
	print >> fp, "rm " + FIFO_FILE
        print >> fp, "exit"
	fp.close()

if len(sys.argv) < 5:
    print >> sys.stderr, "Use %s <video id> <duration in sec> <mode quic|http> <trace path>"
    exit(2)

duration = float(sys.argv[2])
vid = sys.argv[1]
mode = sys.argv[3]
trace = sys.argv[4]
LOG_DIR = sys.argv[1]

if mode <> 'quic' and mode <> 'http':
	print >> sys.stderr, "Use quic or http as mode only"
	exit(3)

try:
    shutil.rmtree(TEMP_CHROME_PROF_DIRECTORY)
except OSError:
    pass

os.mkdir(TEMP_CHROME_PROF_DIRECTORY)

mahi_cmd = "mm-delay 40 mm-link %s %s bash "%(trace, trace)

cmd_http="chromium-browser --user-data-dir='%s' --no-proxy-server --autoplay-policy=no-user-gesture-required --enable-logging --log-level=0 --start-maximized --no-default-browser-check 'http://10.5.20.129:9893/index2.html#dash/%s/media/vid.mpd'"%(TEMP_CHROME_PROF_DIRECTORY, vid)
cmd_quic="chromium-browser --user-data-dir='%s' --no-proxy-server --autoplay-policy=no-user-gesture-required --enable-quic --origin-to-force-quic-on=www.sml2.org:443 --enable-logging --log-level=0 --host-resolver-rules='MAP www.sml2.org:443 10.5.20.129:6121' --start-maximized --no-default-browser-check 'https://www.sml2.org/index2.html#dash/%s/media/vid.mpd'"%(TEMP_CHROME_PROF_DIRECTORY, vid)

# createAndSaveCmd(CMD_SCRIPT, )

cmd = cmd_http#"chromium-browser --no-proxy-server --user-data-dir=%s"%(TEMP_CHROME_PROF_DIRECTORY)
if mode == 'quic':
	cmd = cmd_quic

createAndSaveCmd(CMD_SCRIPT, cmd)

cmd = mahi_cmd + CMD_SCRIPT

cmdArr = shlex.split(cmd)
proc = subprocess.Popen(cmdArr)
time.sleep(duration + 300)
fp = open(FIFO_FILE, "w")
print >> fp, "echo"
fp.close()
time.sleep(5)
# proc.kill()

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

shutil.move(os.path.join(TEMP_CHROME_PROF_DIRECTORY, "chrome_debug.log"), os.path.join(LOG_DIR, "chrome_debug_%s_%s.log"%(vid, mode)))
