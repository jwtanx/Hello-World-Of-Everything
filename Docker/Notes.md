# List of Docker notes

## Listing all the docker images
```bash
docker ps -a
````

## Running the docker image (NOTE: ONLY FOR FIRST TIME)
```bash
docker start 4ed769366c2e
````

## Starting the docker container (NOTE FOR FOLLOWING TIME OR ELSE THE CONTAINER IS CORRUPTED)
```bash
docker run 4ed769366c2e
```

## Change into interactive mode for docker that is running
```bash
docker exec -it 4ed769366c2e sh

````
