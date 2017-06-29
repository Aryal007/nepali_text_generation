from __future__ import absolute_import, division, print_function

import tflearn
from tflearn.data_utils import *
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

path = "./data/sports_news_nepali_1000.txt"

maxlen = 50

string_utf8 = open(path, "r").read()
X, Y, char_idx = \
    string_to_semi_redundant_sequences(string_utf8, seq_maxlen=maxlen, redun_step=3)

g = tflearn.input_data(shape=[None, maxlen, len(char_idx)])
g = tflearn.lstm(g, 256, return_seq=True, name='lstm_1')
g = tflearn.dropout(g, 0.5, name='dropout_1')
g = tflearn.lstm(g, 256, return_seq=True, name='lstm_2')
g = tflearn.dropout(g, 0.5, name='dropout_2')
g = tflearn.lstm(g, 256, name='lstm_3')
g = tflearn.dropout(g, 0.5, name='dropout_3')
g = tflearn.fully_connected(g, len(char_idx), activation='softmax')
g = tflearn.regression(g, optimizer='adam', loss='categorical_crossentropy',
                       learning_rate=0.001)

m = tflearn.SequenceGenerator(g, dictionary=char_idx,
                              seq_maxlen=maxlen,
                              clip_gradients=5.0,
                              tensorboard_verbose = 0,
                              checkpoint_path='./models/nepali_rnn')

seed = random_sequence_from_string(string_utf8, maxlen)

while(1):
	m.fit(X, Y, validation_set=0.1, batch_size=256,
	      n_epoch=100, run_id='nepali_rnn')
	m.save('./nepali_model')
	print("-- TESTING...")
	print("-- Test with temperature of 1.2 --")
	print(m.generate(200, temperature=1.2, seq_seed=seed))
	print("-- Test with temperature of 1.0 --")
	print(m.generate(200, temperature=1.0, seq_seed=seed))
	print("-- Test with temperature of 0.5 --")
	print(m.generate(200, temperature=0.5, seq_seed=seed))
