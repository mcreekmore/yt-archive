# yt-archive

A python script for automatically downloading the latest video from a YouTube channel

## Prerequisites

- python 3

## Install and run manually

```bash
pip3 install yt_dlp dotenv

chmox +x yt-archive.py

# make sure .env file is in the root of the directory

# run
./yt-archive.py
```

Adding to cron job is available as a Ansible playbook in the [pms](https://github.com/mcreekmore/pms) repo

## .env structure

```ini
YT_API_KEY=key
CHANNELS=channel,ids,comma,seperated
DL_PATH=/example/path
```

## Next steps

- containerize
- add to docker-compose stack
