---
tags:
  - Programming
  - Tool
  - Microsoft
links:
  - "[[Programming]]"
---
# Port

### Forward port from server to local host

```bash
ssh -L 5000:localhost:5000 tantn@10.124.64.139 -p 8022
```

# Run Docker to delete file

```bash
docker run -v /home/tantn/workspace:/workspace -it ubuntu /bin/bash
```

# Command line

```bash
# Create file in folder
touch script.sh

# Open file in Editor
code script.sh
```