#!/usr/bin/python3

import sys

import numpy
import tensorflow as tf
import tensorflowjs as tfjs

import azbn as azbnpy

arguments = sys.argv

numpy.random.seed(42)

azbn = azbnpy.AzbnConstructor()


def main(argv):

	input_size = 10
	output_size = 3

	d_input = []
	d_output = []

	for i in range(1000):
		
		ri = []
		for j in range(input_size):
			ri.append(azbn.randpart())
		ri.sort()
		d_input.append(ri)

		ro = []
		for j in range(output_size):
			ro.append(azbn.randpart())
		ro.sort()
		d_output.append(ro)
	
	azbn.saveJSON('data_input', d_input)
	azbn.saveJSON('data_output', d_output)

	inputs = tf.keras.Input(shape=(input_size,))
	#x = tf.keras.layers.Dense(input_size, activation=tf.nn.relu)(inputs)
	outputs = tf.keras.layers.Dense(output_size, activation=tf.nn.softmax)(inputs)
	model = tf.keras.Model(inputs=inputs, outputs=outputs)
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

	#model = tf.keras.models.Sequential()
	##model.add(tf.keras.layers.Flatten())
	#model.add(tf.keras.layers.Dense(input_size, input_dim=input_size, activation='relu', kernel_initializer='normal'))
	#model.add(tf.keras.layers.Dense(output_size, activation='softmax', kernel_initializer='normal'))
	#model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

	#print(model.summary())
	
	model.fit([d_input], [d_output], batch_size=input_size, epochs=output_size)


	d_test_i = []
	for j in range(input_size):
		d_test_i.append(azbn.randpart())
	d_test_i.sort()

	d_test_o = []
	for j in range(output_size):
		d_test_o.append(azbn.randpart())
	d_test_o.sort()

	# Оцениваем качество обучения сети на тестовых данных
	scores = model.evaluate([[d_test_i]], [[d_test_o]], verbose=0)
	print("Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))

	d_test_i = []
	for j in range(input_size):
		d_test_i.append(azbn.randpart())
	d_test_i.sort()

	result = model.predict([[d_test_i]])
	print(result)
	sum = 0
	for j in result[0]:
		sum = sum + j
	print(sum)
	
	#tf.keras.utils.plot_model(model, to_file='model.png')

	model.save_weights('data_model.h5')
	model_json = model.to_json()
	with open('data_model.json', 'w') as f:
		f.write(model_json)
	tfjs.converters.save_keras_model(model, './tfjs')

	pass


if __name__ == '__main__':
	main(arguments)
