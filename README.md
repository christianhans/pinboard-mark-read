# pinboard-mark-read

HTTP endpoint to mark Pinboard bookmarks as read.

## Installation on Debian/Raspian 10.x

**Note**: It's strongly recommended to expose this application via HTTPS/SSL only.

Prerequisites:

```
sudo apt-get install git python3 nginx
```

Clone and set up a Python virtual environment:

```
git clone https://github.com/christianhans/pinboard-mark-read.git
cd pinboard-mark-read
python3 -m venv env
source env/bin/activate
python setup.py install
deactivate
```

Set up a system service to run the application:

```
sudo cp pinboard-mark-read.service /etc/systemd/system/pinboard-mark-read.service
```

Open `/etc/systemd/system/pinboard-mark-read.service` and adjust all file paths to point to the location of the `pinboard-mark-read` folder. Also ensure that the directive `user` is set to the name of the user under which the application should run.

Start the application:

```
sudo systemctl start pinboard-mark-read
```

Check if the application started successfully (any potential error messages will be shown here – it should say "Active: active (running)"):

```
sudo systemctl status pinboard-mark-read
```

In case the application runs properly enable it to start on system boot:

```
sudo systemctl enable pinboard-mark-read
```

Adjust your nginx configuration to serve the application (adjust the file path in line 6 accordingly):

```
server {
    ...
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/user/pinboard-mark-read/pinboard_mark_read.sock;
    }
    
    ...
}
```

Reload nginx:

```
sudo systemctl reload nginx
```
