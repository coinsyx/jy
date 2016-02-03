import sys
import urllib2
from sys import stdin
from time import gmtime, strftime
import numpy


def minite_gap(minite, gap):
    x = minite / gap
    n = x * gap
    return '%02d' % n 
    

gap = 10
fin_file = 'history.btcc.dat'
fout_file = 'basic_stat_%d.dat' % gap
fout = open(fout_file, 'w')
d = {}
for line in open(fin_file):
    rcd = eval(line.strip())
    prc = rcd['price']
    tm = gmtime(int(rcd['date']))
    tms = strftime('%Y%m%d-%H', tm) + minite_gap(tm.tm_min, gap)
    if tms not in d:
        d[tms] = []
    d[tms].append(prc) 

for tms in sorted(d.keys()):
    n = len(d[tms])
    std = numpy.std(d[tms])    
    avg = numpy.mean(d[tms])
    amax = numpy.amax(d[tms])
    amin = numpy.amin(d[tms])
    p25 = numpy.percentile(d[tms], 25)    
    p75 = numpy.percentile(d[tms], 75)    
    fout.writelines(tms + '\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%d\n' % (avg, std, amin, amax, p25, p75, n)) 

fout.close()
    


