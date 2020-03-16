# pinboard-mark-read

HTTP endpoint to mark Pinboard bookmarks as read.

Used by [pinboard-to-kindle](https://github.com/christianhans/pinboard-to-kindle) to allow the user to mark Pinboard bookmarks as read – directly from the delivered eBook.

**Note**: It's strongly recommended to expose this application via HTTPS/SSL only. The HTTP endpoint requires a `?h=...` URL parameter which has to match a hash value of `PINBOARD_MARK_READ_SECRET` concatenated with the requested URL. Serving this application over non-encrypted channels will expose those hashed values. Moreover, keep in mind that any HTTP access log files will also contain those hashed values.

## Installation on Debian/Raspian 10.x

Prerequisites:

```
sudo apt-get install git python3 nginx pwgen
```

Clone this repository and set up a Python virtual environment:

```
git clone https://github.com/christianhans/pinboard-mark-read.git
cd pinboard-mark-read
python3 -m venv env
source env/bin/activate
python setup.py install
deactivate
```

Open `config.env` to set your Pinboard API token and choose a secret passphrase (e.g. via `pwgen 32`):

```
PINBOARD_TOKEN="..."
PINBOARD_MARK_READ_SECRET="..."
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

Check if the application started successfully (any potential error messages will be shown here – it should say `Active: active (running)`):

```
sudo systemctl status pinboard-mark-read
```

In case the application runs properly enable it to start on system boot:

```
sudo systemctl enable pinboard-mark-read
```

Adjust your nginx configuration to serve the application (adjust the `proxy_pass` file path accordingly):

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
