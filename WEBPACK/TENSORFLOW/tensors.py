# Learning about tensor and multi-dimensional thinking...

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
