import os
import sys

import numpy as np
import pickle

#np.random.seed(0)

args = sys.argv

# text = open('text.txt', 'rb').read().decode(encoding='utf-8')
# vocab = sorted(set(text))
# char2idx = {u:i for i, u in enumerate(vocab)}
# idx2char = np.array(vocab)
# text_as_int = np.array([char2idx[c] for c in text])
# print('{')
# for char,_ in zip(char2idx, range(20)):
# 	print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))
# print('  ...\n}')
# print ('{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]), text_as_int[:13]))


# Z = np.zeros(10, [ ('position', [ ('x', float, 1),('y', float, 1)]), ('color', [ ('r', float, 1), ('g', float, 1), ('b', float, 1)])])
# print(Z)


# mu, sigma = 0, 0.4
# rowcount = 3
# colcount = 2
# a = np.random.normal(mu, sigma, size = (rowcount, colcount))
# b = np.random.normal(mu, sigma, size = (colcount, rowcount))
# print(a)
# print(b)
# print(np.dot(a, b))


# mu, sigma = 0, 0.4
# rowcount = 3
# colcount = 2
# a = np.random.normal(mu, sigma, size = (rowcount, colcount))
# m = np.absolute(a).max()
# b = a / m
# print(a)
# print(b)




# a = {'hello': 'world'}
# with open('filename.pickle', 'wb') as handle:
# 	pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)
# with open('filename.pickle', 'rb') as handle:
# 	b = pickle.load(handle)
# print(a == b)

# a = np.array([1, 2, 3, 4])
# print(type(a), a)
# print([ x*9/5 + 32 for x in a])

# a1 = np.linspace(-5, 5, 12)
# print(a1)
# print((a1 / 2).round())
# print(type(a1.tolist()))



# ones = np.ones(50)
# rnd = np.random.random(50) * 0.1 #np.random.normal(loc=0, scale=5, size=100000) Помимо нормального и равномерного распределения NumPy также предлагает beta, dirichlet, gamma, binomial, exponential, и другие.
# samples = ones + rnd

# print(samples)
# print(np.average(samples))
# print(np.mean(samples))
# print(np.median(samples))
# print(np.percentile(samples, 75))

# print(samples.min())
# print(samples.max())
# print(samples.ptp())

# print(np.std(samples))
# print(np.var(samples))


# a2 = np.arange(1, 10).reshape(3,3)
# #np.identity(3)
# print(a2)
# print(a2.transpose())
# print(a2.trace())
# print(np.linalg.det(a2))
# print(np.linalg.inv(a2))



# a3 = (np.random.random(9) * 0.1).reshape(3,3)
# a4 = (np.random.random(9) * 0.1).reshape(3,3)
# print(a3)
# print(a4)
# print(a3 + a4)


# import matplotlib.pyplot as plt
# x = np.linspace(-5, 5, 100)
# def sigmoid(alpha):
# 	return 1 / ( 1 + np.exp(- alpha * x) )
# dpi = 80
# fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
# plt.plot(x, sigmoid(0.5), 'ro-')
# plt.plot(x, sigmoid(1.0), 'go-')
# plt.plot(x, sigmoid(2.0), 'bo-')
# plt.legend(['A = 0.5', 'A = 1.0', 'A = 2.0'], loc = 'upper left')
# fig.savefig('sigmoid.png')
