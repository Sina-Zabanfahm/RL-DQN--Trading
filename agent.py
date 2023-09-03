# -*- coding: utf-8 -*-
"""Agent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u4B-3c62JHks35Af6aHThpB6UxrUgpTQ
"""

from reader import *
import numpy as np
import pandas as pd
from collections import Counter, deque
import random

import keras
from keras import layers, models
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
from keras.utils import plot_model

reader = DataReader()
reader.read_data()
data = reader.get_data()

class Trading_Agent:

    def __init__(self, states_size =3, initiated = False, model_name = "", memory_len = 1000):

        self.states_size = states_size

        self.actions = ['Buy', 'Hold', 'Sell']
        self.actions_dict = Counter(self.actions)

        self.memory = deque(maxlen = memory_len)
        self.inventory = []
        self.model_name = model_name

        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995

        self.parameters_dict = {'gamma' :  self.gamma,
                                'epsilon' : self.epsilon,
                                'epsilon_min' : self.epsilon_min,
                                'epsilon_decay': self.epsilon_decay}
        self.model = None
        if initiated == False:
            self.model = self.build_model
        else: self. model =load_model("models/"+model_name)

    def build_model(self, hidden_dim = 64):
        print(self.states_size)
        model = Sequential([
            Dense(hidden_dim, input_dim = self.states_size, activation = 'relu'),
            Dense(hidden_dim//2, activation = 'relu'),
            Dense(hidden_dim//4, activation = 'relu'),
            Dense(self.states_size, activation = 'linear')
        ])
        self.compile_model(model)
        return model


    def compile_model(self, model, lr = 0.001):
        model.compile(loss = 'mse', optimizer = keras.optimizers.Adam(lr = lr))
        return

    def act(self,state):

        if self.initiated == True and random.random() <= self.epsilon:

            return random.randrange(self.action_size)

        options = self.model_predict(state)
        return np.argmax(options[0])
    def set_parameters(self,gamma = 0.95, epsilon = 1.0, epsilon_min = 0.01, epsilon_decay = 0.995):

        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay


    def get_parameters(self):

        return self.parameters_dict

    def get_model_summary(self, model):

        return model.summary()

agent = Trading_Agent(3)
model = agent.build_model()
agent.get_model_summary(model)