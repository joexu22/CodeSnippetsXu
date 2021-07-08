# Programming a straight line using tensor flow

from __future__ import print_function
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

print("when do we get to the good stuff".title()) # Script Title
sess = tf.Session()

# tensor-flow application of a x-y coordinate graph
M = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = M * x + b

# tensorflow requires explicit call to initialize all the variables
init = tf.global_variables_initializer()
sess.run(init)

# produce outputs for the machine learning program
print(sess.run(linear_model, {x: [1, 2, 3, 4]}))

# finding out the regression... (loss)...
y = tf.placeholder(tf.float32)

squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
# this should cause a loss value: 23.66
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

# we want to loss value to be 0.0
# a.k.a. we want to figure out the appropriate variables are given a "y"

# Here we manually "guess" the solution... <rando sort it>
fix_M = tf.assign(M, [-1.])
fix_b = tf.assign(b, [1.])
sess.run([fix_M, fix_b])
# The correct loss value: 0
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

# "Here" - we have the magic of "machine learning"
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init)  # reset the variables to incorrect defaults

# Doing gradual regression/correction until the correct answer is obtained
# So, I was able to solve this problem through "machine learning"...
# Somewhat like using a nuke to kill a fly
for i in range(1000):
	sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})
print(sess.run([M, b]))
