# -*- coding: utf-8 -*-

from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.callbacks import TensorBoard

import numpy as np

batch_size = 10
num_classes = 18
epochs = 20

x_train = np.loadtxt("sample_train_data/x_train.csv",delimiter=",")
y_train = np.loadtxt("sample_train_data/y_train.csv",delimiter=",")
x_test = np.loadtxt("sample_train_data/x_train.csv",delimiter=",")
y_test = np.loadtxt("sample_train_data/y_train.csv",delimiter=",")


x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')


model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(72,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])

callbacks = [keras.callbacks.ModelCheckpoint('./checkpoints/weights_epoch:{epoch:03d}_valloss:{val_loss:.3f}_valacc:{val_acc:.3f}.hdf5',
                                verbose=1,
                                save_best_only=True,
                                mode='auto',
                                save_weights_only=True,
                                period=3),
             keras.callbacks.EarlyStopping(monitor='val_acc', min_delta=0.01, patience=25, verbose=1, mode='auto'),
             TensorBoard(log_dir='./graph', histogram_freq=0, write_graph=True, write_grads=True, write_images=True)]

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test),
                    callbacks=callbacks)
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

