"""
推論を実行する
"""
def load_model(model):
    # 分類クラス数
    nb_classes = 10
    # 重みファイルパス
    full_model_weights_path = [path to weights file]

    model = Sequential()
    model.add(Dense(512, activation='relu', input_shape=(72,)))
    model.add(Dropout(0.2))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(num_classes, activation='softmax'))
    # 重みファイルをロード
    model.load_weights(full_model_weights_path)
    # コンパイル
    model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.SGD(lr=1e-4, momentum=0.9),
              metrics=['accuracy'])
    model.summary()

    return model

def init_models():
    model_copper = load_model()

def predict(filename):
    x = [read data from csv]
    x = x / 255.0
    res = model.predict(x)[0]
    return res

if __name__ == '__main__':
    main()

    # モデルの初期化
    print('Init models...')
    util_predict.init_models()

    # 推論実行
    prob = predict(save_path)
    print("prob: {0} dev: {1}".format(str(prob))
