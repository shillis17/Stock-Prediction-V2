#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:04:58 2019

@author: seth
"""

from LSTMClass import LSTMClass as LSTMPrediction
from ProphetClass import ProhetClass as ProhetPrediction
import matplotlib.pyplot as plt
from matplotlib import rcParams
from gather_data import get_data
import numpy as np


def build_plots():
    """
    Makes plots formatted so each prediction line is on the same graph
    and formats the graph to be easily displayed in the readme.

    Makes a class for each item stock for each time frame and combines the
    results to the same figure
    """
    google, microsoft, apple, jnj, amazon = get_data()

    stocks = [['GOOGL', google], ['MSFT', microsoft], ['AAPL', apple],
              ['JNJ', jnj], ['AMZN', amazon]]

    rcParams.update({'figure.autolayout': True})
    plt.style.use('fivethirtyeight')

    lap7 = LSTMPrediction(apple, 'APPL', 7)
    lap14 = LSTMPrediction(apple, 'APPL', 14)
    lap30 = LSTMPrediction(apple, 'APPL', 30)
    pap7 = ProhetPrediction(apple, 'AAPL', 7)
    pap14 = ProhetPrediction(apple, 'AAPL', 14)
    pap30 = ProhetPrediction(apple, 'AAPL', 30)

    lam7 = LSTMPrediction(amazon, 'AMZN', 7)
    lam14 = LSTMPrediction(amazon, 'AMZN', 14)
    lam30 = LSTMPrediction(amazon, 'AMZN', 30)
    pam7 = ProhetPrediction(amazon, 'AMZN', 7)
    pam14 = ProhetPrediction(amazon, 'AMZN', 14)
    pam30 = ProhetPrediction(amazon, 'AMZN', 30)

    lgo7 = LSTMPrediction(google, 'GOOGL', 7)
    lgo14 = LSTMPrediction(google, 'GOOGL', 14)
    lgo30 = LSTMPrediction(google, 'GOOGL', 30)
    pgo7 = ProhetPrediction(google, 'GOOGL', 7)
    pgo14 = ProhetPrediction(google, 'GOOGL', 14)
    pgo30 = ProhetPrediction(google, 'GOOGL', 30)

    ljj7 = LSTMPrediction(jnj, 'JNJ', 7)
    ljj14 = LSTMPrediction(jnj, 'JNJ', 14)
    ljj30 = LSTMPrediction(jnj, 'JNJ', 30)
    pjj7 = ProhetPrediction(jnj, 'JNJ', 7)
    pjj14 = ProhetPrediction(jnj, 'JNJ', 14)
    pjj30 = ProhetPrediction(jnj, 'JNJ', 30)

    lms7 = LSTMPrediction(microsoft, 'MSFT', 7)
    lms14 = LSTMPrediction(microsoft, 'MSFT', 14)
    lms30 = LSTMPrediction(microsoft, 'MSFT', 30)
    pms7 = ProhetPrediction(microsoft, 'MSFT', 7)
    pms14 = ProhetPrediction(microsoft, 'MSFT', 14)
    pms30 = ProhetPrediction(microsoft, 'MSFT', 30)

    helper = [[lap7, pap7, 'APPL', 7], [lap14, pap14, 'APPL', 14],
              [lap30, pap30, 'APPL', 30],
              [lam7, pam7, 'AMZN', 7], [lam14, pam14, 'AMZN', 14],
              [lam30, pam30, 'AMZN', 30],
              [lgo7, pgo7, 'GOOG', 7], [lgo14, pgo14, 'GOOG', 14],
              [lgo30, pgo30, 'GOOG', 30],
              [ljj7, pjj7, 'JNJ', 7], [ljj14, pjj14, 'JNJ', 14],
              [ljj30, pjj30, 'JNJ', 30],
              [lms7, pms7, 'MSFT', 7], [lms14, pms14, 'MSFT', 14],
              [lms30, pms30, 'MSFT', 30]]

    for i in helper:
        findex = np.arange(0, i[3]+1)
        pindex = np.arange(-(i[3]*2)+1, 1)
        lstmp = i[0].predictions[-(i[3]+1):].values
        propp = i[1].forecast.yhat[-(i[3]+1):].values
        hist = i[1].train.y[-i[3]*2:]
        real = i[0].actuals
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.autoscale()
        plt.tight_layout(pad=3)
        plt.plot(pindex, hist, 'b')
        plt.plot(findex, lstmp, 'r')
        plt.plot(findex, propp, 'g')
        plt.plot(findex, real, 'b')
        plt.axvline(x=0, color='k', linestyle='dashed')
        plt.legend(['History', 'LSTM', 'Prophet', 'Actual'], prop={'size': 25})
        plt.xlabel('Days Out (From Today)')
        plt.ylabel('Value (US$)')
        plt.title(i[2] + ' Predictions ' + str(i[3]) + ' days')
        plt.savefig('../img/EDA/' + i[2] + '_' + str(i[3]) + '.png')
        plt.close()

    for i in stocks:
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.autoscale()
        plt.tight_layout(pad=3)
        plt.plot(i[1].close, 'k')
        plt.title(i[0] + ' Historical Prices')
        plt.xlabel('Date')
        plt.ylabel('Value (US$)')
        plt.savefig('../img/EDA/' + i[0] + '_EDA.png')
        plt.close()

