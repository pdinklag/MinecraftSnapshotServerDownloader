#!/usr/bin/python3
import argparse
import hashlib
import json
import urllib.request
import os
import sys

def sha1(filename):
    with open(filename, 'rb') as file:
        return hashlib.sha1(file.read()).hexdigest()

parser = argparse.ArgumentParser(
    description='Downloads the latest Minecraft snapshot server.')
parser.add_argument('-o', '--output',
                    help='the output filename -- overrides -d and -p',
                    default='')
parser.add_argument('-d', '--dir',
                    help='the output directory',
                    default='.')
parser.add_argument('-p', '--prefix',
                    help='the server filename prefix',
                    default='minecraft_server.')
parser.add_argument('-m', '--mapping',
                    action='store_true',
                    help='download the server obfuscation mapping file')
parser.add_argument('-s', '--silent',
                    action='store_true',
                    help='silent mode - print filename only, and only if new version was downloaded')
parser.add_argument('--print-always',
                    action='store_true',
                    help='always print the filename in silent mode, even if nothing new was downloaded')

args = parser.parse_args()

if not args.silent: print('Retrieving manifest ...')
manifest_url = 'https://launchermeta.mojang.com/mc/game/version_manifest.json'
manifest = json.loads(
    str(urllib.request.urlopen(manifest_url).read(), 'utf-8'))

latest = manifest['latest']['snapshot']
if not args.silent: print('Latest snapshot version is ' + latest)
for version in manifest['versions']:
    if version['id'] == latest:
        if not args.silent: print('Retrieving meta information ...')
        meta = json.loads(
            str(urllib.request.urlopen(version['url']).read(), 'utf-8'))

        server_url = meta['downloads']['server']['url']
        server_hash = meta['downloads']['server']['sha1']

        if args.output:
            server_filename = args.output
        else:
            server_filename = os.path.join(
                args.dir, args.prefix + latest + '.jar')

        if os.path.isfile(server_filename):
            if sha1(server_filename) == server_hash:
                if not args.silent: print('Nothing to do!')
                if args.print_always: print(server_filename)
                sys.exit(0)

        if not args.silent: print('Downloading: ' + server_url)
        urllib.request.urlretrieve(
            server_url,
            server_filename)

        if sha1(server_filename) == server_hash:
            if args.mapping:
                mapping_filename = server_filename[:-4] + '.mapping.txt'
                mapping_url = meta['downloads']['server_mappings']['url']
                if not args.silent: print('Downloading: ' + mapping_url)
                urllib.request.urlretrieve(mapping_url, mapping_filename)
        
            print(server_filename)
            sys.exit(0)
        else:
            if not args.silent: print('Error: size of downloaded file does not match!')
            sys.exit(1)

if not args.silent: print('No meta information found for ' + latest)
sys.exit(1)
