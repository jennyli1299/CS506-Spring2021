def euclidean_dist(x, y):
    if x == [] or y == []:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    if x == [] or y == []:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res
    # raise NotImplementedError()

def jaccard_dist(x, y):
    # raise NotImplementedError()
    ''' 
    Definition of Jaccard Distance: 1 - Jaccard Similarity
    Definition of Jaccard Similarity: len( x intersection y ) / len( x union y )
    '''
    if x == [] or y == []:
        raise ValueError("lengths must not be zero")

    #convert list x, y to sets
    setX = set(x)
    setY = set(y)

    intersection_X_Y = setX & setY
    union_X_Y = setX | setY

    return 1 - (len(intersection_X_Y)/len(union_X_Y))


def dot_product(x, y):
    if x == [] or y == []:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += x[i]*y[i]
    return res

def norm(x):
    if x == []:
        raise ValueError("lengths must not be zero")
    res = 0
    for i in range(len(x)):
        res += (x[i])**2
    return res**(1/2)

def cosine_sim(x, y):
    # raise NotImplementedError()
    '''
    A similarity function is a function that takes 2 objects (data points) and
    returns a large value if these objects are similar

    To get a corresponding dissimilarity function, we can usually try
        d(x, y) = 1 / s(x, y)
                or
        d(x, y) = k - s(x, y) for some k

    Cosine Similarity: 
        s(x, y) = cos(theta), where theta is the angle between x and y
    Cosine Disimilarity: 1 - s(x, y) since 1 is the max of cos(theta)

    Use cosine (dis)similarity over euclidean distance when direction matters more than magnitude
    '''
    if x == [] or y == []:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    '''
    a . b = |a|*|b|*cos<a,b>
    cos<a,b> = (a.b) / (|a|*|b|) = (scalar product of vectors a and b) / (product of magnitudes of a & b; norms of vectors a & b)
    '''
    return dot_product(x, y) / (norm(x) * norm(y))

# Feel free to add more
