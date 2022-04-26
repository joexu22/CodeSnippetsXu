# Classic Alien Invasion Game

This is the simple, classic alien invasion game that will be implemented using python.
This project is inspired and directed by "Python Crash Course"

## Setup (WSL2)

Set up the GUI at:
	- https://medium.com/@japheth.yates/the-complete-wsl2-gui-setup-2582828f4577

Notes:
Need to run this for the Xserver to work

```bash
	export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
	export LIBGL_ALWAYS_INDIRECT=1
	sudo /etc/init.d/dbus start &> /dev/null
```

Uses Python3 Virtual Environment:
  	- ```source .venv/bin/activate```