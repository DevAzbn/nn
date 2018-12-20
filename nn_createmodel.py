import tensorflow as tf

model = tf.keras.models.Sequential([
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(512, activation=tf.nn.relu),
	tf.keras.layers.Dropout(0.2),
	tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#model.save_weights('nn.h5')
model_json = model.to_json()

with open('data/nn.json', 'w') as f:
	f.write(model_json)

del model
