# Learning about tensor and multi-demensional thinking...
# This is "crazy" - Is AI thinking just an application of multidemensional
# thinking. Basically, I would assume people are only able to program so far
# as much as human brain allows. How much do I understand my own brain, so
# that I am able to program it into a computer?

# Tensors - just some complicated arrays
rank_0_tenser = 3.0 # []
rank_1_tensor = [1.0, 2.0, 3.0] # [3]
rank_2_tensor_0 = [[1.0, 2,0, 3,0],[4.0, 5.0, 6.0]] # [2, 3]
rank_2_tensor_1 = [[1.0, 2,0, 3,0]] # [1, 3]
rank_3_tensor_a = [[[1.0, 2,0, 3,0]], [[1.0, 2,0, 3,0]]] # [2, 1, 3]

rank_3_tensor_0 = [[[3.0]]] # [1, 1, 1]
rank_3_tensor_1 = [[[1.0, 2.0, 3.0]]] # [1, 1, 3]

# the following is: [3, 1, 3]
rank_3_tensor_2 = [[[1.0, 2.0, 3.0]], [[1.0, 2.0, 3.0]], [[1.0, 2.0, 3.0]]]

