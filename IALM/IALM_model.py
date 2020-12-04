#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2020/12/3 17:11
# @Author      : Yixiong Huang
# @Contact     : yxhuang7538@163.com
# @File        : IALM_model.py
# @Description : 用于视频背景建模的IALM算法模型
# @Software    : PyCharm

import numpy as np
from numpy.linalg import norm, svd


def inexact_augmented_lagrange_multiplier(D, tol=1e-7, maxIter=1000):
    """
    IALM求解PCA问题的主要迭代模型，根据Algorithm 5
    :param D: 观测矩阵
    :param tol: 阈值
    :param maxIter: 最大迭代次数
    :return: A（背景），E（前景）
    """
    m, n = D.shape # m = 视频长乘宽 n = 帧数
    lmbda = 1 / np.sqrt(max(m, n))  # 用于平衡A的低秩程度和E的稀疏程度
    # 计算J（Y）
    Y_norm_two = norm(D, 2)
    Y_norm_inf = norm(D, np.inf) / lmbda
    Jy = np.max([Y_norm_two, Y_norm_inf])

    Y = D / Jy  # 计算Y
    A = np.zeros(Y.shape)
    E = np.zeros(Y.shape)
    mu = 1.25 / Y_norm_two  # mu的初始化
    rho = 1.5
    sv = 10.
    itr = 0  # 迭代次数

    # 迭代
    while True:
        Eraw = D - A + (1 / mu) * Y  # 原始E
        Eupdate = np.maximum(Eraw - lmbda / mu, 0) + np.minimum(Eraw + lmbda / mu, 0)  # 更新E
        U, S, V = svd(D - Eupdate + (1 / mu) * Y, full_matrices=False)  # 奇异值分解

        svp = (S > 1 / mu).shape[0]
        if svp < sv:
            sv = np.min([svp + 1, n])
        else:
            sv = np.min([svp + round(0.05 * n), n])

        Aupdate = np.dot(np.dot(U[:, :svp], np.diag(S[:svp] - 1 / mu)), V[:svp, :])  # 更新A
        A = Aupdate
        E = Eupdate
        Y = Y + mu * (D - A - E)

        '''
        # 更新mu
        if mu * norm(Eraw - Eupdate, 'fro') / norm(D, 'fro') < tol:
            mu = rho * mu
        else:
            mu = mu
        '''

        mu = np.min([mu * rho, mu * 1e7])
        itr += 1

        # 判断是否停止迭代
        if ((norm(D - A - E, 'fro') / norm(D, 'fro')) < tol) or (itr >= maxIter):
            break
    print("IALM Finished at iteration %d" % itr)
    return A, E

