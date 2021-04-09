# count

This is a Flask application intended to keep track of view counts.

## Endpoints

- `/count`: Increments counter and returns new value.
- `/peek`: Returns counter value.

## Running

First, in the repository, build the Docker image:

```
$ docker build -t count .
```

Then run the container, mounting a volume for the count file:

```
$ docker run -d -p 8000:80 -v /path:/var/count count
```
