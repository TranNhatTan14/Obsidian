---
tags:
  - Programming
  - Tool
  - Microsoft
links:
  - "[[Github Copilot]]"
---
- We can use on brower at https://vscode.dev/tunnel/superman/c:/Users/Superman

# Port

```bash
# Forward port from server to local host
ssh -L 5000:localhost:5000 tantn@10.124.64.139 -p 8022
```

# Command line

```bash
# Create file in folder
touch script.sh

# Open file in Editor
code script.sh

# Run Docker to delete file
docker run -v /home/tantn/workspaces:/workspaces -it ubuntu /bin/bash
```