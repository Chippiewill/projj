all:
	rm -f "${HOME}/.local/bin/pcd" "${HOME}/.local/bin/pcl" "${HOME}/.local/bin/pcd.py"
	ln -s "$(CURDIR)/bin/pcd" "${HOME}/.local/bin/pcd"
	ln -s "$(CURDIR)/bin/pcd.py" "${HOME}/.local/bin/pcd.py"
	ln -s "$(CURDIR)/bin/pcl" "${HOME}/.local/bin/pcl"