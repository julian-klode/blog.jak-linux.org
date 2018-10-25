all: remote

local:
	hugo

remote: local
	rsync -aP  --exclude ".well-known" --delete --checksum public/ jak-linux.org:/var/www/virtual/jak/blog.jak-linux.org

.PHONY: local remote
