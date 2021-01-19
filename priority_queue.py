# Priority queue.
# Amazon: Kth top movies

rating = [3,4,5,2,4,5,1,1,2]

priority_queue = []
k = 3

for i in rating:
    priority_queue.append(i)
    if len(priority_queue) > k:
        # TODO: Need to implement it in better way.
        priority_queue = sorted(priority_queue, reverse=True)[0:3]
    print("priority queue .... \n", priority_queue)
