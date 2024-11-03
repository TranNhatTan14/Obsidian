---
tags:
  - Tool
---
```bash
# Install Tmux
sudo apt install tmux

# List of sessions
tmux ls

# Create new session with name
tmux new -s [session_name]

# Attach new session
tmux attach -t [session_name]

# Kill exist session
tmux kill-session -t [session_name]

# Kill all sessions
tmux kill-server

# Exit session
exit
```

`Ctrl + B + Page Up` to scroll and `q` to Quit