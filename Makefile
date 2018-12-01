all: remote

local:
	hugo

remote: local
	rsync -aP  --exclude ".well-known" --delete --checksum public/ root@blog.jak-linux.org:/var/www/blog.jak-linux.org

.PHONY: local remote
