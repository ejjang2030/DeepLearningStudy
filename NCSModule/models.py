from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.callbacks import ModelCheckpoint, EarlyStopping
(train_data, train_label), (validation_data, validation_label) = mnist.load_data()
'''
for images in train_data[:2]:
    for image in images:
        for dat in image:
            print('{:3} '.format(dat), end='')
        print()
    print(end='\n\n')
'''

train_data = train_data.reshape(train_data.shape[0], 784).astype('float64') / 255
validation_data = validation_data.reshape(validation_data.shape[0], 784).astype('float64') / 255

model = Sequential()
model.add(Dense(128, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

cb_checkpoint = ModelCheckpoint(filepath='/tmp/weights.hdf5', verbose=1, save_best_only=True)
cb_early_stopping = EarlyStopping(patience=20)
model.fit(train_data, train_label, validation_data=(validation_data, validation_label), epochs=10, batch_size=200, verbose=0, callbacks=[cb_checkpoint, cb_early_stopping])

train_label = np_utils.to_categorical(train_label, 10)
validation_label = np_utils.to_categorical(validation_label, 10)

accuracy = model.evaluate(validation_data, validation_label)[1]
print('\nAccuracy: {:2f}'.format(accuracy))
