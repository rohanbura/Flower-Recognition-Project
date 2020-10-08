#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from keras.models import load_model
from keras.preprocessing import image


class flower:
    def __init__(self,filename):
        self.filename = filename

    def predictionflower(self):
        model = load_model('model.h5')

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        if result[0][0] == 1:
            prediction = 'daisy'
            return [{ "Image Predicted" : prediction}]

        elif result[0][1] == 1:
            prediction = 'dandelion'
            return [{ "Image Predicted" : prediction}]

        elif result[0][2] == 1:
            prediction = 'rose'
            return [{ "Image Predicted" : prediction}]

        elif result[0][3] == 1:
            prediction = 'sunflower'
            return [{ "Image Predicted" : prediction}]

        else:
            prediction = 'tulip'
            return [{ "Image Predicted" : prediction}]