# MinecraftSnapshotServerDownloader
This is a small Python 3 script to download the latest Minecraft snapshot server JAR.
It was written because since _18w19a_, the download URL needs to be retrieved in a more complicated and indirect way

## Requirements
Python 3 is required, that's it. Tested only with Python 3.4.2.

## Usage
Simply execute `mcdlsnapshot.py` from the shell.

By default, it will download the latest snapshot into the current working directory and name it `minecraft_server.<VERSION>.jar`.
You can change the output filename via the command-line parameters (see below or use `--help`).

```
usage: mcdlsnapshot.py [-h] [-o OUTPUT] [-d DIR] [-p PREFIX] [-m] [-s]

Downloads the latest Minecraft snapshot server.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        the output filename -- overrides -d and -p
  -d DIR, --dir DIR     the output directory
  -p PREFIX, --prefix PREFIX
                        the server filename prefix
  -m, --mapping         download the server obfuscation mapping file
  -s, --silent          silent mode - print filename only, and only if new
                        version was downloaded
```

### Return Code
The script will return _success_ (error code 0) if a new version was downloaded successfully or if the output file already is the latest version (verified via its SHA1 hash if it already exists).

On any kind of failure, error code 1 is returned.

### Silent Mode
For automated downloading in host scripts, _silent mode_ can be helpful. In silent mode, nothing is printed to the output except the output file name - and only if it was actually downloaded (i.e. if an update to the latest version has been performed).

