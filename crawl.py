import sys
import urllib2
import time

def read_url(url, trynum = 3):
    for i in range(trynum):
        try:
            f = urllib2.urlopen(url)
            rst = f.read()
            return rst
        except:
            continue
    return None

fout_file = 'history.btcc.dat.1'
fout_logfile = 'log.dat'
fout = open(fout_file, 'a')
fout_log = open(fout_logfile, 'w')
tid = '15878334'
n = 0
while tid < '44167137':
    n += 1
    url = 'https://data.btcchina.com/data/historydata?since=' +tid+ '&limit=10000'
    rst = read_url(url)
    if rst == None:
        fout_log.writelines('%d read url failed\n' % n)
        fout_log.flush()
        continue
    l = eval(rst)
    if len(l) == 0:
        continue
    for record in l:
        fout.writelines(str(record) + '\n')
    fout.flush()
    record = l[-1] 
    tid = record['tid'] 
            

