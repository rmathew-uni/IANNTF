import numpy as np
np.set_printoptions(precision=3)
mu, sigma = 0,1

#generate random variable
x = np.random.normal(mu, sigma, size=(5,5))
print(x)
#replace function
new_x = np.where(x>0.9, 42, x*x )

print(new_x)

#only 4 column
print(x[:,3:4])