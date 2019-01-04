#!/usr/bin/python3

import sys

import numpy
import tensorflow as tf

import azbn as azbnpy

arguments = sys.argv

numpy.random.seed(42)

azbn = azbnpy.AzbnConstructor()


def main(argv):

	d_input = []
	d_output = []

	for i in range(1000):
		
		ri = []
		for j in range(10):
			ri.append(azbn.randpart())
		ri.sort()
		d_input.append(ri)

		ro = []
		for j in range(2):
			ro.append(azbn.randpart())
		ro.sort()
		d_output.append(ro)
	
	azbn.saveJSON('data_input', d_input)
	azbn.saveJSON('data_output', d_output)

	model = tf.keras.models.Sequential()
	#model.add(tf.keras.layers.Flatten())
	model.add(tf.keras.layers.Dense(10, input_dim=10, activation='relu', kernel_initializer='normal'))
	model.add(tf.keras.layers.Dense(2, activation='softmax', kernel_initializer='normal'))
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

	#print(model.summary())
	
	model.fit(numpy.array(d_input), numpy.array(d_output), batch_size=32, epochs=10)


	d_test_i = []
	for j in range(10):
		d_test_i.append(azbn.randpart())
	d_test_i.sort()

	d_test_o = []
	for j in range(2):
		d_test_o.append(azbn.randpart())
	d_test_o.sort()

	# Оцениваем качество обучения сети на тестовых данных
	scores = model.evaluate(numpy.array([d_test_i]), numpy.array([d_test_o]), verbose=0)
	print("Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))

	d_test_i = []
	for j in range(10):
		d_test_i.append(azbn.randpart())
	d_test_i.sort()

	result = model.predict(numpy.array([d_test_i]))
	print(result)

	pass


if __name__ == '__main__':
	main(arguments)
