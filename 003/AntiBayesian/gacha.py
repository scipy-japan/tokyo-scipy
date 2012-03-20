#!/usr/bin/env python
# See Also http://d.hatena.ne.jp/AntiBayesian/20120318/1332024867

import numpy as np
import pylab as plt

def gachaMain(weight, trialNum):
    length = len(weight)
    sumWeight = sum(weight)
    return [gachaDo(weight, length, sumWeight) for i in range(trialNum)]

def gachaDo(weight, length, sumWeight):
    cnt = 0
    gachaCompStatus = [0] * length
    while 0 in gachaCompStatus:
        cnt += 1
        rnd = np.random.randint(sumWeight) + 1
        for i in range(length + 1):
            if sum(weight[:i]) < rnd and rnd <= sum(weight[:i + 1]):
                gachaCompStatus[i] += 1
                break
    return cnt

iter = 10000

plt.subplot(221)
gachaWeight = [1, 1, 1, 1, 1, 1]
gachaCompData = gachaMain(gachaWeight, iter)
plt.hist(gachaCompData)
plt.figtext(0.35, 0.85, 'Weight = ' + str(gachaWeight))
plt.figtext(0.35, 0.83, 'mean:' + str(np.mean(gachaCompData)))
plt.figtext(0.35, 0.81, 'std:' + str(np.std(gachaCompData)))

plt.subplot(222)
gachaWeight = [100, 50, 10, 10, 3, 1]
gachaCompData = gachaMain(gachaWeight, iter)
plt.hist(gachaCompData)
plt.figtext(0.78, 0.85, 'Weight = ' + str(gachaWeight))
plt.figtext(0.78, 0.83, 'mean:' + str(np.mean(gachaCompData)))
plt.figtext(0.78, 0.81, 'std:' + str(np.std(gachaCompData)))

plt.subplot(223)
gachaWeight = [5, 5, 3, 3, 2, 1]#sum weight := 19
gachaCompData = gachaMain(gachaWeight, iter)
plt.hist(gachaCompData)
plt.figtext(0.35, 0.4, 'Weight = ' + str(gachaWeight))
plt.figtext(0.35, 0.37, 'mean:' + str(np.mean(gachaCompData)))
plt.figtext(0.35, 0.35, 'std:' + str(np.std(gachaCompData)))

plt.subplot(224)
gachaWeight = [10, 3, 2, 2, 1, 1]#sum weight := 19
gachaCompData = gachaMain(gachaWeight, iter)
plt.hist(gachaCompData)
plt.figtext(0.78, 0.4, 'Weight = ' + str(gachaWeight))
plt.figtext(0.78, 0.37, 'mean:' + str(np.mean(gachaCompData)))
plt.figtext(0.78, 0.35, 'std:' + str(np.std(gachaCompData)))

plt.show()
