# Nano

```bash
# Open <file-name> in the nano text editor
nano <file-name>

# Create an empty file with the specified name
touch <file-name>

# Automatically respond yes to all prompts from command
<command> -y

du -sh /home/user/*
```

# wget
```bash
# Specify an output path
wget -O /home/tantn/workspace/NSAID/pipeline/annotation/GCF_000001405.40.gz.tbi https://ftp.ncbi.nih.gov/snp/latest_release/VCF/GCF_000001405.40.gz.tbi
```

# Conda

```bash
# Deactivate
conda deactivate

# Remove environment
conda env remove --name env_name
```

# Tmux

```bash
# Install Tmux
sudo apt install tmux

# Create new session with name
tmux new -s [session_name]

# Attach new session
tmux attach -t [session_name]

# Kill exist session
tmux kill-session -t [session_name]

# List of sessions
tmux ls

# Exit session
exit
```

`Ctrl + B + Page Up` to scroll and `q` to Quit