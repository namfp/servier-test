
#Problem 
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.

#Run from source

```
cd src
INPUT=x,y,z python main.py x,y
```

#Test from source
```cd src
python test.py
``` 

#Build docker image
```
docker build  -t test_mdm .
```

#Run from docker
```
docker run --env INPUT=x,y,z -t test_mdm  x,y
```