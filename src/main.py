from sparse_array import SparseArray
import os
import sys

if __name__ == "__main__":
    words = os.environ['INPUT'].split(",")
    sparse_array = SparseArray(words)
    args = sys.argv
    if len(args) == 1:
        raise Exception("You must specify the query. Example toto,tata,titi")
    else:
        query = args[1]
        result = sparse_array.compute(query.split(','))
        print(result)