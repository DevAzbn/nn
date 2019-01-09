import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model_json = '';
with open('data/nn.json', 'r') as f:
	model_json = f.read()

model = tf.keras.models.model_from_json(model_json)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)

model.save_weights('data/nn.h5')
model_json = model.to_json()
with open('data/nn.json', 'w') as f:
	f.write(model_json)

del model