import numpy as np 
from scipy.spatial import distance

pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])

euclidean_dist = distance.euclidean(pointA, pointB)
print("Eculidean Distance:", euclidean_dist)

similarity_euclidean = 1 / (1 + euclidean_dist)
print("euclidean Similarity:",similarity_euclidean)


import numpy as np 
from scipy.spatial import distance

pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])

Manhattan_dist = distance.cityblock(pointA, pointB)
print("Manhattan Distance:", Manhattan_dist)

similarity_Manhattan = 1 / (1 + Manhattan_dist)
print("Manhattan Similarity:",similarity_Manhattan)

minkowski_dist_p3=distance.minkowski(pointA,pointB,p=2)
print("Minkowski Distance (p=3):", minkowski_dist_p3)

similarity_minkowski=1/(1 + minkowski_dist_p3)
print("Minkowski Similarity (p=2):", similarity_minkowski)

minkowski_dist_p3=distance.minkowski(pointA,pointB,p=1)
print("Minkowski Distance (p=1):", minkowski_dist_p3)

similarity_minkowski=1/(1 + minkowski_dist_p3)
print("Minkowski Similarity (p=1):", similarity_minkowski)

minkowski_dist_p3=distance.minkowski(pointA,pointB,p=3)
print("Minkowski Distance (p=3):", minkowski_dist_p3)




