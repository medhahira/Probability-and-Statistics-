import math
import matplotlib.pyplot as plt
import numpy as np 

#here I have hard coded the time intervals in which messages are received in a list called data
data = [5, 6, 3, 22, 17, 5, 1, 13, 4, 16, 19, 9, 8, 7, 11, 18, 10, 2, 23, 20, 1, 12, 3, 13, 2, 11, 14, 3, 20, 19]
print(len(data))

number_of_value = len(data)
sum = 0
sum_square = 0

def gaussian_function(x, mu, sig):
    denom = sig*((2*math.pi)**0.5)
    numerator = np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    return numerator/denom

def exponential_function(lambda_exp,x):
    denominator = np.exp(lambda_exp*x)
    ans = lambda_exp/denominator
    return ans 

for i in data:
    sum+=i
average = sum/number_of_value
for j in data:
    sum_square += (j - average) ** 2

variance = sum_square/(number_of_value-1)
standard_dev = variance**0.5
print(f"average of the 30 values is {average}")
print(f"variance of the 30 values is {variance}")
print(f"standard deviation of 30 values if {standard_dev}")

sum_i = 0
sum_square_i = 0
avg = [] #list of averages upto the i th element in the data set
var = [] #list of variances upto the i th element in the data set
sd = [] #list of standard deviations upto the i th element in the data set
mu_sig =[] 
for k in range(30):
    sum_i = 0 
    sum_square_i = 0
    l = []
    if k == 0:
        avg.append(data[0])
        sd.append(0)
        var.append(0)
        l.append(0)
        l.append(0)
        mu_sig.append(l)
    else:
        for j in data[:k+1]:
            sum_i += j
        average_i = sum_i/(k+1)
        for j in data[:k+1]:
            sum_square_i += (j - average_i)**2
        l = []
        l.append(average_i)
        #used k as a denominator as k already has num-1 value 
        variance_i = sum_square_i/k
        sd_i = variance_i**0.5
        l.append(sd_i)
        mu_sig.append(l)
        avg.append(average_i)
        var.append(variance_i)
        sd.append(sd_i)
print(len(var))
print(avg)
print(var)
print(sd)

i = int(input("enter the index for mean, sd, var: "))
print(f"average: {avg[i-1]}")
print(f"variance: {var[i-1]}")
print(f"standard deviation: {sd[i-1]}")
#print(mu_sig)
#print(sum_square_i)
#print(f"average of the 30 values is {average_i}")
#print(f"variance of the 30 values is {variance_i}")

#PLOTTING TIME GAP(values of data set) vs their corresponding frequencies
l = []
freq = []
s = set(data)
unique = []
for i in s:
    freq.append(data.count(i))
f = plt.figure(1)
plt.plot(list(s), freq)
plt.xlabel('time gap')
plt.ylabel('frequency')
plt.title('time gap vs frequency graph')
f.show() 

g = plt.figure(2)
y = data
x = []
for i in range(30):
    x.append(i)
plt.plot(x,y)
plt.xlabel('time gap')
plt.ylabel('index')
plt.title('graph representing the data set')
g.show()

gaussian = plt.figure(3)
data = np.array(data)
x = np.linspace(-40,40,100)
plt.xlabel('time gap')
plt.ylabel('normal pdf')
plt.plot(x, gaussian_function(x, average, variance**0.5))
plt.show()

data.sort()
lambda_inverse = variance**0.5
lambda_exp = 1/lambda_inverse
x = np.linspace(0,20,100)
plt.xlabel('time gap')
plt.ylabel('exponential pdf')
plt.plot(x,exponential_function(lambda_exp, x))
plt.show()

print("THE GAUSSIAN NORMAL PDF IS MORE ACCURATE AND MATCHES BETTER")
