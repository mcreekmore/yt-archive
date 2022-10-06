# yt-archive

## Install

```bash
pip3 install yt_dlp dotenv

chmox +x yt_dl-sync.py

# make sure .env file is in the root of the directory
```

Adding to cron job is available as a Ansible playbook in the [pms](https://github.com/mcreekmore/pms) repo

## .env structure

```ini
YT_API_KEY=key
CHANNELS=channel,ids,comma,seperated
DL_PATH=/example/path
```

## Run Manually

```bash
./archive.py
```

## Next steps

- containerize
- add to docker-compose stack
