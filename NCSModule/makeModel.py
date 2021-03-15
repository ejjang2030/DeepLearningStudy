from keras.datasets import mnist
from keras.models import Sequential
from keras.utils import np_utils
from keras.layers import Activation, Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping
import os

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

(train_data, train_label), (validation_data, validation_label) = mnist.load_data()

for images in train_data[:2]:
    for image in images:
        for dat in image:
            print("{:3} ".format(dat), end='')
        print()
    print(end='\n\n')

train_data = train_data.reshape(train_data.shape[0], 784).astype('float64') / 255
validation_data = validation_data.reshape(validation_data.shape[0], 784).astype('float64') / 255

train_label = np_utils.to_categorical(train_label, 10)
validation_label = np_utils.to_categorical(validation_label, 10)

model = Sequential()
model.add(Dense(128, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# cb_checkpoint = ModelCheckpoint(filepath='/tmp/weights.hdf5', verbose=1, save_best_only=True)
# cb_early_stopping = EarlyStopping(patience=20)
# model.fit(train_data, train_label, validation_data=(validation_data, validation_label), epochs=1, batch_size=32, verbose=0, callbacks=[cb_checkpoint, cb_early_stopping])
model.fit(train_data, train_label, epochs=1, batch_size=32, validation_data=(validation_data, validation_label))

accuracy = model.evaluate(validation_data, validation_label)[1]
print('\nAccuracy: {:.2f}'.format(accuracy))

'''
# 6. 모델 저장하기
MODEL_SAVE_FOLDER_PATH = './model/service/'
if not os.path.exists(MODEL_SAVE_FOLDER_PATH):
    os.mkdir(MODEL_SAVE_FOLDER_PATH)
service_model_path = MODEL_SAVE_FOLDER_PATH + 'aip_model.h5'
model.save(service_model_path)
'''