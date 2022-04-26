# Me Following Tensor Flow Tutorial

from __future__ import print_function
import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

print("the reason why i bothered learning CS anyways:".title()) 
# What I need to build tensorflow program
# 1) I need to build the computational graph
# 2) I need to run the computational graph

# creating a file_writer here cause???
# file_writer = tf.summary.FileWriter('./logs', sess.graph)


# creating session
sess = tf.Session()

# creating some tensor nodes
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("\nThese are the node represenation of node1 and node2: ")
print(node1, node2)

print("\nThis is ran output of node1 and node2: ")
print(sess.run([node1, node2]))

print("\nThese are the results of the evaluated node3: ")
print("node3: ", node3)
print("sess.run(node3): ", sess.run(node3))


# Using Lamba functions in tensorflow
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

print(sess.run(adder_node, {a: 3, b: 4}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))

# making use of tensorboard
with tf.Session() as sess:
	writer = tf.summary.FileWriter("output",sess.graph)
	writer.close()
