import numpy as np

data = [1.0, 4.5, 2.3, -0.5, 0.5, 2.8]

np.mean(data)
#output --> 1.766666666
np.median(data)
#output -->  1.6499999999999999

np.std(data)
#output --> 1.6407992632318622

np.var(data)
#output -->  2.6922222222222221

np.nan + 1
#output -->  nan
data =  np.random.normal(size=20)
plt.hist(data);

print("====================")

clf()
data = np.random.poisson(lam=0.5, size=10000)
ax1 = plt.subplot(1, 2, 1)
ax1.hist(data, normed=True)
ax2 = plt.subplot(1, 2, 2)
ax2.hist(data, cumulative=True);
#output --> graph

print("====================")

for i in range(1, 5):
    ax = plt.subplot(2, 2, i)
    ax.text(0.0,0.5, 'plot number %d' % i)
#output --> graph
    
print("=============")

clf()

data = np.random.chisquare(7, size=10000)
ax1 = plt.subplot(1, 2, 1)
ax1.hist(data, normed=True)
ax2 = plt.subplot(1, 2, 2)
ax2.hist(data, cumulative=True);
#output --> graph

print("===================")

#random numbers
np.random.seed(27)

np.random.random()
#output -->  0.4257214105188958

print("================")

data = np.random.normal(loc=10, scale=2, size=1000)

np.percentile(data, 50)
#output -->  9.9916481921815539

np.median(data)
#output -->  9.9916481921815539

np.percentile(data, [25, 50,75])
#output --> array([  8.62196334,   9.99164819,  11.34885341])

print("==================")

data = np.random.normal(0, 100, size=5)

data
#output --> array([ 215.64141609,  -10.58085898,  -81.94316487,   66.6058758 , -104.34260935])

np.random.shuffle(data)

np.random .permutation(10)
#output --> : array([9, 2, 4, 0, 3, 7, 5, 1, 6, 8])

np.random.permutation(data)
#output --> array([  66.6058758 ,  -10.58085898,  -81.94316487,  215.64141609, -104.34260935])

print("==========")

data = np.random.permutation(5)

data
#Output --> array([1, 0, 4, 2, 3])

np.random.choice(data)
#output --> 2

np.random.choice(data, size=5)
#output -->  array([2, 0, 0, 3, 1])

np.random.choice(data, size=4, replace=False)
#output --> array([0, 1, 2, 3])

