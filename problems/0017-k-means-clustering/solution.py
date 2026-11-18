def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    # Your code here
    #for loop max max_iterations
        #assign cluster 
        
    final_centroids = initial_centroids.copy()
    for i in range (max_iterations):
        pointincntroid = [[] for _ in range(len(initial_centroids))]
        for point in points:
            nowcentroid = 0
            nowdistance = -1
            for k in range(len(initial_centroids)):
                sum = 0
                for d in range (len(point)):
                    sum+=(point[d]-initial_centroids[k][d])**2
                if(nowdistance == -1 or sum<nowdistance):
                    nowcentroid = k
                    nowdistance = sum
            pointincntroid[nowcentroid].append(point)
        #recalculate centroid 
        for p in range (len(pointincntroid)):
            if(len(pointincntroid[p]) == 0 ):
                final_centroids[p] = initial_centroids[i]
            else:
                sum = [0 for _ in range (len(points[0]))]
                for m in range(len(pointincntroid[p])):
                    for n in range(len(pointincntroid[p][m])):
                        sum[n]+=pointincntroid[p][m][n]
                for m in range(len(sum)):
                    sum[m]/=len(pointincntroid[p])
                final_centroids[p] = tuple(sum)

    return final_centroids