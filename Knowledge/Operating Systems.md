# nano

```bash
# Open <file-name> in the nano text editor
nano <file-name>

# Create an empty file with the specified name
touch <file-name>

# Automatically respond yes to al
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

# Use conda with Jupyter Notebook
conda install -c anaconda ipykernel

conda env export > environment.yml
conda env export --no-builds > environment.yml
```

# tmux

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

# OpenCore

https://dortania.github.io/OpenCore-Install-Guide/extras/spoof.html#windows-gpu-selection

NOTE: This version of ocvalidate is only compatible with OpenCore version 1.0.1!

https://github.com/benbaker76/Hackintool
https://github.com/ic005k/OCAuxiliaryTools

-v alcid=8 revpatch=sbvmm igfxonln=1 -igfxblt -vi2c-force-polling amfi_get_out_of_my_way=0x1 ngfxcompat=1 ngfxgl=1 nvda_drv_vrl=1

-v alcid=8 amfi_get_out_of_my_way=0x1 ngfxcompat=1 ngfxgl=1 nvda_drv_vrl=1

https://dortania.github.io/OpenCore-Post-Install/gpu-patching/#intel-igpu-patching
https://www.youtube.com/watch?v=pCyonAMQrzw

# bcftools

https://www.nagraj.net/notes/bcftools

ls -1 /home/tantn/workspace/STR/web_crosscheck/result/20241022_HID49/20241022_HID49.phieuKQ | wc -l