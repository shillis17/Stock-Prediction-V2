#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:49:58 2019

@author: seth
"""
# Gets RMSE for EDA and readme

from LSTMClass import LSTMClass as LSTMPrediction
from ProphetClass import ProhetClass as ProhetPrediction
from gather_data import get_data
import numpy as np


def rmse(predictions,targets):
    """
    Get the RMSE values for specified predictions,

    Attributes:
        predidctions (list): list of predictions from model
        targets      (list): the real values of the data
    
    Returns:
        RMSE (int) value of RMSE score
    """
    return np.sqrt(np.mean((predictions-targets)**2))


google, microsoft, apple, jnj, amazon = get_data()


lap30 = LSTMPrediction(apple, 'APPL', 30)
pap30 = ProhetPrediction(apple, 'AAPL', 30)

lam30 = LSTMPrediction(amazon, 'AMZN', 30)
pam30 = ProhetPrediction(amazon, 'AMZN', 30)

lgo30 = LSTMPrediction(google, 'GOOGL', 30)
pgo30 = ProhetPrediction(google, 'GOOGL', 30)

ljj30 = LSTMPrediction(jnj, 'JNJ', 30)
pjj30 = ProhetPrediction(jnj, 'JNJ', 30)

lms30 = LSTMPrediction(microsoft, 'MSFT', 30)
pms30 = ProhetPrediction(microsoft, 'MSFT', 30)

dictionary = {}

helper = [
              [lap30, pap30, 'APPL', 30],

              [lam30, pam30, 'AMZN', 30],

              [lgo30, pgo30, 'GOOG', 30],

              [ljj30, pjj30, 'JNJ', 30],

              [lms30, pms30, 'MSFT', 30]]

for i in helper:
    lstmp = i[0].predictions[-(i[3]+1):].values
    propp = i[1].forecast.yhat[-(i[3]+1):].values
    real = i[0].actuals
    dictionary['LSTM'+i[2]] = rmse(lstmp,real)
    dictionary['Prophet'+i[2]] = rmse(propp,real)
    