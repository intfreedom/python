#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import scipy.misc as misc
import matplotlib.pyplot as plt
import numpy as np

class StroopTestResult(object):
    def __init__(self, name, accuracy, responseTime):
        self.name = name
        self.ResponseTime = responseTime
        self.accuracy = accuracy

    def func(self):
        x = ["meaning and color are the same", "meaning and color are the different"]
        y1 = self.accuracy
        y2 = self.ResponseTime
        fig, ax1 = plt.subplots(figsize=(10, 10))
        # 设置ax2的坐标轴与ax1共用x轴
        ax2 = ax1.twinx()
        # 绘制第一条线
        ax1.scatter(x, y1, s=200, c="Red")
        # 共用x轴，所以设置x轴label只能通过ax1，ax2.set_xlabel('two data')无效
        ax1.set_xlabel('X data')
        ax1.set_ylabel('Y1: Accuracy, %', color='r')
        # 绘制第二条线
        ax2.scatter(x, y2, s=200, marker='H')  # blue
        ax2.set_ylabel('Y2: Average reaction time, second', color='b')
        plt.title("stroopTestResult---SubjectName: %s" % self.name, fontsize=16)
        plt.show()
