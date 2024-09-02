---
tags:
  - Status/InProgress
links:
  - "[[Experience]]"
  - "[[Tool]]"
URL: https://app.datacamp.com/learn/courses/intermediate-docker
---
### Docker

```bash
# Run an interactive container. Use `exit` to exit the interactive mode
docker run -it <image_name>

# Adding `-d` to `docker run` will run the container in the background, giving us back control of the shell
docker run -d <image_name>

# Run container with name
docker run --name <container-name> <image_name>

# List running containers
docker ps

# Filtering running containers
docker ps -f "name=<container-name>"

# Stop a container
docker stop <container-id> or `<container-name>`

# Remove stopped container
docker container rm <container-id>
```

### Logs

If instead, you want to follow the logs your container is generating in real-time, you can use docker logs together with the f, for follow, flag. You will see any logs the container generates live. Even though docker ps also has a f flag, the docker ps flag allows us to filter. When working with docker logs instead, the f flag has another effect, allowing us to follow a container its logs. After using docker logs, you will see the output of a running container until either the end of the logs or until you press control plus c to exit the log view.

```bash
# See existing logs for container
docker logs <container-id>

# See live logs for container. Ctrl + C to exit
docker logs -f <container-id>
```

### Cleaning up container and image

It's common to have multiple containers based on a single image, which can make it a tedious task to one by one remove all containers before you can remove an image. To more easily clear all stopped containers, we can use docker container prune.

```bash
docker container prune

docker image prune -a
```

Then we can use docker image prune dash a to remove all unused images. The a flag, which stands for all, makes it so that unused containers are removed and not only dangling images.

### Distributing Docker Images

### Private Docker registries

First, we'll have a look at private Docker registry servers. 

The Docker organization maintains the official Docker images registry. Other Docker registries work the same way but are under the control of another person or group. 

This means there are no guarantees that the images will work or are safe to use. Images from any registry other than the one from the official Docker organization are easily recognizable because their name starts with the URL of the private Docker registry they come from. 

For example, the image we see here comes from dockerhub dot myprivateregistry dot com. Downloading or pulling an image from a private registry is also done using Docker pull. 

Because the image name includes the Docker registry URL, the image will automatically be pulled from the correct registry. For example, to pull the previously mentioned image, use Docker pull followed by the full name of the image. Here too, we can append a colon followed by the version.
###### Pull and Push image with a registry

```bash
# Login to private registry
docker login <private-registry-url>

# Pull from registry
docker image pull <private-registry-url>/<image-name>:<image-version>

# Name image name before push
docker tag <image-name>:<image-version> <private-registry-url>/<image-name>:<image-version>

# Push to registry
docker image push <private-registry-url>/<image-name>:<image-version>
```
### Save and load image as file

```bash
# Save image to file
docker save -o <file-path> <image-name>

# Load image from file
docker load -i <file-path>
```

### Create Docker Image

Each instruction that download files add to the total size of the image, even if file are later deleted. The solution is download, unpack, and remove file in single command.

```Dockerfile
# Start a Dockerfile from an image
FROM <image-name>

# Add a shell command to image
RUN <shell-command>

# Make sure no user input is needed for the shell command
RUN apt-get install -y python3

# Don't run application as root
USER username

# Download files efficiently
RUN curl <file-URL> - o <output-file-path> \
&& unzip <output-file-path> -d <unzipped-directory> \
&& rm <output-file-path>

WORKDIR /home/username/workspace

# Copy file and folder from host to the image
COPY <source-path-on-host> <destination-path-on-image>

# We can't copy from parent directory where we build a Dockerfile
COPY ../<file-in-parent-directory> /

# Running a shell command at startup
CMD <shell-command>
```

The shell command runs when the image is started. It doesn't increase the size of the image and add time to the build.

###### Permissions

Use root to create new user with permissions for specific tasks

The USER instruction changes the user with which the following instructions in the image are run. The last USER instruction in a Dockerfile will also control the user in any containers started from the image of this Dockerfile.

###### Variable

We can create variable with ARG and ENV

![[Pasted image 20240811181258.png]]

The second way to define variables in Dockerfiles is by using the ENV instruction. The syntax is identical to the ARG instruction, but unlike the ARG instruction, variables set with ENV are still accessible after the image is built. While variables set with ARG are used to change the behavior of Dockerfiles during the build, variables set with ENV are used to change behavior at runtime.

![[Pasted image 20240811181544.png]]

###### Docker caching

Building Dockerfiles can take some time. However, building the same Dockerfile a second time is much faster. Let's get some insight into why and when this is the case.
### Security

Containers don't make everything automatically secure. Docker inherently provides more security over running applications locally because there is an extra layer of isolation between the application and our operating system. This makes it much safer to open an application or archive from an unknown source in a container in comparison to doing the same on your local machine. However, that doesn't mean it is 100% safe to do so. A malicious payload can escape the container's isolation and infect the host.

![[Pasted image 20240811182915.png]]

1. Images from a trusted source
2. Keep software up-to-date
3. Keep images minimal

![[Pasted image 20240811183144.png]]

### Build image from Dockerfile

```bash
# Build image from Dockerfile
docker build 

# Add image name when building an image
docker build -t <image-name> 'location/to/Dockerfile'
```

---

This course builds upon the foundations of learning Docker and containerization found in the Introduction to Docker course. We extend the concepts and tools covered in that course, adding the ideas of container image management and optimization, networking, file system communication, multi-platform and multi-container applications. When completed, you'll be able to:

- Create multi-stage builds to optimize the size, security, and reusability of containerized applications.
- Use Docker networking tools and concepts to add inter-container communications and provide networking services to the local network and the outside world.
- Share files and data between containers and the host machine using Docker file system mounts and volumes.
- Create mutli-container application deployments using Docker Compose, drastically simplifying the setup of complex tools common in data science and engineering environments.

You'll gain the most from this course if you have worked with and built some simple containers, but are looking to add to your development, testing, and distribution toolbox. We look forward to helping guide you during your journey of learning Docker.

## Mounting the host filesystem

Great work! You've successfully configured Docker to access a file on the local filesystem from within your container image. While this example is simple, the same behavior can be used for configuration files, data directories, database files, and so forth. Also note that certain versions of Docker can be a little finicky about paths - if you're having trouble, try using a full path when passing the location of the file or directory.

The filesystem in the container is updated with a reference to the new file / directory, leaving the image unchanged otherwise.

## Persistent volumes

## Volume

Perfect! You've successfully created a container using a volume shared with another container. There are many options available when doing this, but it's an effective way to write data between applications in different containers.

Which of the following answers are reasons not to create a monolithic (i.e., single) container for your applications?

Monolithic containers can use excess amounts of space
Monolithic containers are more difficult to update
Monolithic containers can have more security concerns

The speed of a running container isn't typically affected by its size.

Great work! Understanding why you're configuring containers a certain way promotes using them in an effective way.

# Determining the best image to use

All things being equal (capabilities, options, etc), which of these container images would you use for a production base image?

Note: You may wish to use a Docker command we've just learned.

Alpine is the perfect image to use for container images, if possible, due to its extremely small size.

# Docker layers

- Docker images are made up of layers
- A layer generally references a change or command within a Dockerfile
- Layers can be cached / reused
- The order of commands within a Dockerfile can affect whether layers are reused

We care about layers because of reusability: faster build time and smaller builds

```bash
# Build image from Dockerfile
docker image inspect nsaid:latest | jq '.[0] | .RootFS'd 

docker image inspect nsaid:latest | jq '.[0] | {LayerCount: .RootFS.Layers | length}'
```

`jq` is extremely powerful and can be used to query any kind of JSON data, not just Docker output.

## Single-stage builds

Typically, a docker images is created using a single FROM command or source image.

We can obviously add anything to a given 
## Multi-stage builds

A multi-stage build uses multiple stages, or multiple containers to different steps of the build, to create a final container image. Typically, a multi-stage build has one or more build stages, where data or binaries are prepared or complied in some fashion.

Terrific job! You've now created a multi-stage build for a given container, which has dropped the size of the container image from 249MB to less than 2MB! You can utilize multi-stage builds (including ones with more than 2 steps) to create optimized containers that do not contain any superfluous files.

```bash
FROM golang:1.21-alpine3.19 AS gobuild

WORKDIR /src
COPY src/main.go /src/main.go

# Build the go application from source code
RUN go build -o /bin/app_runner /src/main.go

# Create application in standalone container
# Update with the image name from instructions

FROM scratch

# Update with name of previous build stage
COPY --from=gobuild /bin/app_runner /bin/app_runner

CMD ["/bin/app_runner"]
```

Congratulations - You've demonstrated a successful understanding of the varying steps in building a multi-stage containerized application. Sometimes it can be difficult to determine exactly which steps in a Dockerfile are analogous to the steps the Docker engine executes. One way to learn this is to make varying changes to a Dockerfile and rebuild the image to see the steps performed in order.

![[Pasted image 20240822145315.png]]

## Multi-platform builds

# Docker Compose

Combine the the volume, networking, and container handling capabilities of Docker into multi-container applications using Docker Compose. Update and manage application deployments via the docker-compose.yml file.

How to create multi-container applications using Docker Compose.

- Additional command-line tool for Docker
- Define and manage multi-container application
- Specify containers, networking, and storage volumes in a single file `compose.yml` or `compose.yaml`
- Easy to share / demo applications

To start an application, change to a directory containing the docker-compose.yaml and run

```bash
# Starting an application
docker compose up
docker compose -f <YAML> up

# Checking status of applications
docker compose ls

# Stopping an application
docker compose down
docker compose -f <YAML> down
```

Perfect! You can start to see the power of what Docker Compose enables for your workflow. This particular compose file started and created a new Postgresql based application to start managing it. Using the basic `up` and `down` options provides a lot of power when working with applications without requiring knowledge of the underlying systems.

### Dependencies and troubleshooting in Docker Compose

Dependencies define the order of resource startup.

- Resources (containers) may required other resources

Example of website application consisting of three resources

1. Database container running postgresql must start prior to the others. Otherwise, the application will throw errors until the database is available.
2. Python application that controls communications between the website and the database
3. The nginx resource starts up the website server and actually serves the website content

==Shutting down applications occurs in reverse order==

The condition attribute tells Docker Compose when a dependency is successfully started and is ready.

service_started
service_completed_successfully
service_healthy

Docker Compose has additional troubleshooting tools

```bash
# Gathers output from all resources in application
docker compose logs

# Show status of resource with an application
docker compose top
```

## YAML

YAML originally stood for Yet Another Markup Language, but now has the more amusing moniker of YAML Ain't Markup Language

Different sections handle different components

- `services:` list the containers to load
- `networks:` handles networking definition
- `volumes:` controls any volume mounting
- `configs:` handles configuration options without custom images
- `secrets:` provides options to handle password, tokens, API keys, ...

https://docs.docker.com/reference/compose-file
## Services section

- Defines all required resources for the application
- Primarily specifies the containers and images to be used\
- Extensive options available, but only apply to the individual container(s)
- Indention is applied as needed

Note that it is typically not required to build a compose-dot-yaml from scratch. It is far better to start with an initial configuration and modify it from there.

```yml
version: '3.8'

services:
  app:
    image: myapp:latest
    depends_on:
      - db
      - redis
    networks:
      - app-network
    volumes:
      - app-data:/var/lib/app
    configs:
      - source: app-config
        target: /etc/app/config.yaml
    secrets:
      - db_password
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    networks:
      - app-network
    volumes:
      - db-data:/var/lib/postgresql/data
    secrets:
      - db_password
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "user"]
      interval: 30s
      timeout: 10s
      retries: 3

  redis:
    image: redis:alpine
    networks:
      - app-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 5s

networks:
  app-network:
    driver: bridge

volumes:
  app-data:
  db-data:

configs:
  app-config:
    file: ./config/app-config.yaml

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

# Docker & WSL

https://www.freedium.cfd/https://onlyutkarsh.medium.com/running-docker-in-wsl2-ubuntu-distro-without-docker-desktop-6ec495e8bb4d

If you want to easily access your Windows "Documents" folder from WSL, you can create a symbolic link from your home directory:

```
ln -s '/mnt/c/Users/YourUserNameHere/Documents' ./WinDocuments
```

You can do that for Documents or you could just link your Windows home directory.