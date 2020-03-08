# pinboard-mark-read

HTTP endpoint to mark Pinboard bookmarks as read.

## Installation

```
git clone https://github.com/christianhans/pinboard-mark-read.git
cd pinboard-mark-read
python3 -m venv env
source env/bin/activate
python setup.py install
deactivate
sudo cp pinboard-mark-read.service /etc/systemd/system/pinboard-mark-read.service
```

Open `/etc/systemd/system/pinboard-mark-read.service` and adjust all file paths to point to the location of the `pinboard-mark-read` folder.
