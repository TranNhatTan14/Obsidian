---
tags:
  - Knowledge
---
# OpenCore

https://dortania.github.io/OpenCore-Install-Guide/extras/spoof.html#windows-gpu-selection

NOTE: This version of ocvalidate is only compatible with OpenCore version 1.0.1!

https://github.com/benbaker76/Hackintool
https://github.com/ic005k/OCAuxiliaryTools
https://dortania.github.io/OpenCore-Post-Install/gpu-patching/#intel-igpu-patching
https://www.youtube.com/watch?v=pCyonAMQrzw

## Hackintosh

# Linux

## nano

```bash
# Open <file-name> in the nano text editor
nano <file-name>

# Create an empty file with the specified name
touch <file-name>

# Automatically respond yes to al
<command> -y

# Check folder size
du -sh /home/user/*

du -sh * | sort -h

du -sh --exclude='*' /path/to/folder

# Check how many folder in folder
find . -maxdepth 1 -type d | wc -l
```

## wget

```bash
# Specify an output path
wget -O /home/tantn/workspace/NSAID/pipeline/annotation/GCF_000001405.40.gz.tbi https://ftp.ncbi.nih.gov/snp/latest_release/VCF/GCF_000001405.40.gz.tbi
```

```bash
ls -1 /home/tantn/workspace/STR/web_crosscheck/result/20241022_HID49/20241022_HID49.phieuKQ | wc -l
```

## Zip

```bash
zip -r archive_name.zip folder_name
```

### tmux

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

`Ctrl + B + Shift + "` to divide to multiple tmux

# Windows

# MacOS