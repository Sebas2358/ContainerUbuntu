
# 🐳 Docker Custom Ubuntu: Command Summary

This cheat sheet summarizes the essential Docker commands for building, running, and using a **custom Ubuntu container** with volumes and Docker Compose.

---

## 🔧 1. Build the custom image from Dockerfile
```bash
docker build -t custom-ubuntu .
```
Builds a Docker image named `custom-ubuntu` using the `Dockerfile` in the current directory.

---

## 🚀 2. Run the custom Ubuntu container
```bash
docker run -it custom-ubuntu
```
Starts an interactive session with your custom Ubuntu container.

---

## 💾 3. Run with a named volume to persist data
```bash
docker run -it -v mydata:/data custom-ubuntu
```
Mounts the named volume `mydata` to `/data` in the container, persisting files across runs.

---

## 📂 4. Use a bind mount (host folder mapped into container)
```bash
docker run -it -v $(pwd)/myfiles:/data custom-ubuntu
```
Maps your local `./myfiles` folder into `/data` in the container.

---

## 🧭 5. List all volumes
```bash
docker volume ls
```
Shows all named volumes Docker is managing.

---

## 🔍 6. Inspect a specific volume
```bash
docker volume inspect mydata
```
Shows the host path and details of the `mydata` volume.

---

## 🧼 7. Remove a volume
```bash
docker volume rm mydata
```
Deletes the named volume (only if no container is using it).

---

## 🛠 8. Use Docker Compose to build and run
```bash
docker-compose up --build
```
Builds and runs all services defined in `docker-compose.yml`.

```bash
docker-compose down
```
Stops and removes containers and networks. Volumes persist unless `-v` is used.

---

## 📥 9. Attach to a running container
```bash
docker exec -it <container_name_or_id> bash
```
Opens a shell inside the running container.

---

## 🔚 10. Exit the container
```bash
exit
```
Closes the shell. If container was run interactively, it also stops.

---

## 📁 Where Docker Volumes Are Stored on Host

### Named volumes:
Inspect volume to find the host location:
```bash
docker volume inspect mydata
```
Path is usually like:
```bash
/var/lib/docker/volumes/mydata/_data
```

### Bind mounts:
If using this in Compose or `docker run`:
```yaml
volumes:
  - ./myfiles:/data
```
Then data lives directly in your project folder.

---
