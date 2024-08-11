### Docker

![[Pasted image 20240811155800.png]]

###### An interactive Docker container

Adding `-it` to `docker run` will give us an interactive shell in the started container.

```bash
docker run -it <image_name>
```

Use `exit` to exit the interactive mode

###### Running a container detached

Adding `-d` to `docker run` will run the container in the background, giving us back control of the shell

```bash
docker run -d <image_name>
```

These containers run in the background without printing their output to our shell.

###### Listing and stopping running containers

![[Pasted image 20240811160348.png]]

###### Named containers

```bash
docker run --name <container-name> <image_name>
```

We can stop container with `<container-name>`

###### Filtering running containers

```bash
docker ps -f "name=<container-name>"
```

###### Container logs

```bash
docker logs <container-id>
```

###### Live logs

If instead, you want to follow the logs your container is generating in real-time, you can use docker logs together with the f, for follow, flag. You will see any logs the container generates live. Even though docker ps also has a f flag, the docker ps flag allows us to filter. When working with docker logs instead, the f flag has another effect, allowing us to follow a container its logs. After using docker logs, you will see the output of a running container until either the end of the logs or until you press control plus c to exit the log view.

###### Cleaning up

To fully remove an already stopped container, for example, because we want to reuse its name, we use docker container rm followed by the container-id to remove the container.

```bash
docker container rm <container-id>
```
![[Pasted image 20240811161504.png]]
###### Pulling image

```bash
docker pull <image-name>:<image-version>
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

First, we'll have a look at private Docker registry servers. The Docker organization maintains the official Docker images registry. Other Docker registries work the same way but are under the control of another person or group. This means there are no guarantees that the images will work or are safe to use. Images from any registry other than the one from the official Docker organization are easily recognizable because their name starts with the URL of the private Docker registry they come from. For example, the image we see here comes from dockerhub dot myprivateregistry dot com. Downloading or pulling an image from a private registry is also done using Docker pull. Because the image name includes the Docker registry URL, the image will automatically be pulled from the correct registry. For example, to pull the previously mentioned image, use Docker pull followed by the full name of the image. Here too, we can append a colon followed by the version.

![[Pasted image 20240811163321.png]]
###### Pushing to a registry

![[Pasted image 20240811163426.png]]

###### Docker images as files

![[Pasted image 20240811163546.png]]

### Create Docker Image

![[Pasted image 20240811172819.png]]

![[Pasted image 20240811172519.png]]
###### Buiding a Dockerfile

```shell
docker build -t <image-name> <location of Dockerfile>
```

###### Customizing images

###### Downloading file efficiently

![[Pasted image 20240811174036.png]]

![[Pasted image 20240811174104.png]]
![[Pasted image 20240811175452.png]]
###### Docker caching
Building Dockerfiles can take some time. However, building the same Dockerfile a second time is much faster. Let's get some insight into why and when this is the case.

###### Changing users and working directory

![[Pasted image 20240811180512.png]]

![[Pasted image 20240811180633.png]]
###### User

The USER instruction changes the user with which the following instructions in the image are run. The last USER instruction in a Dockerfile will also control the user in any containers started from the image of this Dockerfile.

![[Pasted image 20240811180811.png]]

###### Variable

We can create variable with ARG and ENV

![[Pasted image 20240811181258.png]]

The second way to define variables in Dockerfiles is by using the ENV instruction. The syntax is identical to the ARG instruction, but unlike the ARG instruction, variables set with ENV are still accessible after the image is built. While variables set with ARG are used to change the behavior of Dockerfiles during the build, variables set with ENV are used to change behavior at runtime.

![[Pasted image 20240811181544.png]]

### X

Containers don't make everything automatically secure. Docker inherently provides more security over running applications locally because there is an extra layer of isolation between the application and our operating system. This makes it much safer to open an application or archive from an unknown source in a container in comparison to doing the same on your local machine. However, that doesn't mean it is 100% safe to do so. A malicious payload can escape the container's isolation and infect the host.

![[Pasted image 20240811182915.png]]

1. Images from a trusted source
2. Keep software up-to-date
3. Keep images minimal
4. Don't run application as root

![[Pasted image 20240811183144.png]]