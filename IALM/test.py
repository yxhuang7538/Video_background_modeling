#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2020/12/3 21:01
# @Author      : Yixiong Huang
# @Contact     : yxhuang7538@163.com
# @File        : test.py
# @Description : 视频背景建模
# @Software    : PyCharm

import IALM_model
import cv2
from glob import glob
import imageio
import numpy as np
from skimage.transform import resize

def make_video(X, file_name, flag='A'):
    """
    将图片输出为视频
    :param X:
    :param file_name:
    :return:
    """
    fps = 20
    size = (X.shape[1], X.shape[0])
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv2.VideoWriter('./result/' + flag + '/' + file_name, fourcc, fps, size, isColor=False)
    img = np.zeros([X.shape[0], X.shape[1]])
    for i in range(X.shape[2]):
        img[:, :] = X[:, :, i] * 255
        #cv2.imshow('frame', img)
        cv2.imwrite('./result/' + flag + '/%d.bmp' % i, img)
        img1 = cv2.imread('./result/' + flag + '/%d.bmp' % i, cv2.IMREAD_GRAYSCALE)

        videoWriter.write(img1)
    videoWriter.release()

if __name__ == "__main__":
    datas = sorted(glob("./datasets/ShoppingMall/*.bmp")) # 获取所有帧
    d1, d2, channels = imageio.imread(datas[0]).shape
    print(d1, d2, channels)
    D = np.zeros((d1, d2, len(datas)))
    for n, i in enumerate(datas):
        D[:, :, n] = resize(cv2.cvtColor(cv2.imread(i), cv2.COLOR_RGB2GRAY) / 255., (d1, d2))

    D = D.reshape(d1 * d2, len(datas))

    clip = len(datas) # 拿100的数据建模
    A, E = IALM_model.inexact_augmented_lagrange_multiplier(D[:, : clip])

    A = A.reshape(d1, d2, clip)
    E = E.reshape(d1, d2, clip)
    D = D.reshape(d1, d2, len(datas))

    background = np.zeros((d1, d2, 3))
    A = A.astype(np.float32)
    E = E.astype(np.float32)
    D = D.astype(np.float32)

    make_video(A, 'background.mp4', flag='A')
    make_video(E, 'prospect.mp4', flag='E')
    make_video(D, 'original.mp4', flag='D')

