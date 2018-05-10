#!/usr/bin/python3
import argparse
import json
import urllib.request
import os
import sys

parser = argparse.ArgumentParser(
    description='Downloads the latest Minecraft snapshot server.')
parser.add_argument('-d', '--dir',
                    help='the output directory',
                    default='.')
parser.add_argument('-p', '--prefix',
                    help='the server filename prefix',
                    default='minecraft_server.')

args = parser.parse_args()

print('Retrieving manifest ...')
manifest_url = 'https://launchermeta.mojang.com/mc/game/version_manifest.json'
manifest = json.loads(
    str(urllib.request.urlopen(manifest_url).read(), 'utf-8'))

latest = manifest['latest']['snapshot']
print('Latest snapshot version is ' + latest)
for version in manifest['versions']:
    if version['id'] == latest:
        print('Retrieving meta information ...')
        meta = json.loads(
            str(urllib.request.urlopen(version['url']).read(), 'utf-8'))

        server_url = meta['downloads']['server']['url']
        server_size = int(meta['downloads']['server']['size'])
        print('Downloading: ' + server_url)

        server_filename = os.path.join(args.dir, args.prefix + latest + '.jar')
        urllib.request.urlretrieve(
            server_url,
            server_filename)

        if os.path.getsize(server_filename) == server_size:
            print('Success: ' + server_filename)
            sys.exit(0)
        else:
            print('Error: size of downloaded file does not match!')
            sys.exit(1)

print('No meta information found for ' + latest)
sys.exit(1)
