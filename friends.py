def mean_num_friends(x):
    mean = 0
    for el in x:
        mean = mean + el
    mean = mean / len(x)
    return mean

def median_num_friends(x):
    x.sort()
    median_spot = int(len(x) / 2)
    return x[median_spot]    

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

print("dataset: %s" % num_friends )
print("mean= {} ".format(mean_num_friends(num_friends)))
print("median = {}".format(median_num_friends(num_friends)))

