# MinecraftSnapshotServerDownloader
This is a small Python 3 script to download the latest Minecraft snapshot server JAR.
It was written because since _18w19a_, the download URL needs to be retrieved in a more complicated and indirect way

## Requirements
Python 3 is required, that's it. Tested only with Python 3.4.2.

## Usage
Simply execute `mcdlsnapshot.py` from the shell.

By default, it will download the latest snapshot into the current working directory and name it `minecraft_server.<VERSION>.jar`.
You can change the output directory and filename prefix via command-line parameters (see below or use `--help`).

```
usage: mcdlsnapshot.py [-h] [-o OUTPUT] [-d DIR] [-p PREFIX]

Downloads the latest Minecraft snapshot server.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        the output filename -- overrides -d and -p
  -d DIR, --dir DIR     the output directory
  -p PREFIX, --prefix PREFIX
                        the server filename prefix
```
