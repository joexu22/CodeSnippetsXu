# My *first TensorFlow program
# Getting into the new age of AI

# Goals:
#   Get Style-Transfer to Work
#   Teach a computer to Draw something
#   Have computer learn Animation
#   Teach a computer to learn some music
#   Compile things together to make person Animation Studio

import tensorflow as tf
hello = tf.constant("Hello, TensorFlow!")
sess = tf.Session()
print(sess.run(hello))