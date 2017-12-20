# My *first TensorFlow program
# Into a new age of AI

import tensorflow as tf
hello = tf.constant("Hello, TensorFlow!")
sess = tf.Session()
print(sess.run(hello))
