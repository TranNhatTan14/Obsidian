```bash
# Open <file-name> in the nano text editor
nano <file-name>

# Create an empty file with the specified name
touch <file-name>

# Automatically respond yes to all prompts from command
<command> -y
```

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

###### Logs

If instead, you want to follow the logs your container is generating in real-time, you can use docker logs together with the f, for follow, flag. You will see any logs the container generates live. Even though docker ps also has a f flag, the docker ps flag allows us to filter. When working with docker logs instead, the f flag has another effect, allowing us to follow a container its logs. After using docker logs, you will see the output of a running container until either the end of the logs or until you press control plus c to exit the log view.

```bash
# See existing logs for container
docker logs <container-id>

# See live logs for container. Ctrl + C to exit
docker logs -f <container-id>
```

###### Cleaning up container and image

It's common to have multiple containers based on a single image, which can make it a tedious task to one by one remove all containers before you can remove an image. To more easily clear all stopped containers, we can use docker container prune.

```bash
docker container prune

docker image prune -a
```

Then we can use docker image prune dash a to remove all unused images. The a flag, which stands for all, makes it so that unused containers are removed and not only dangling images.

### Distributing Docker Images

###### Private Docker registries

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
###### Save and load image as file

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