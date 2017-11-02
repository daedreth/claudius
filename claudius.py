#!/usr/bin/env python3

import asyncio
import discord
import sys
import os
import time
import configparser
import subprocess

# Global
client = discord.Client()
config = configparser.ConfigParser()
config.read(os.environ['HOME'] + '/.config/claudius/config.ini')

filePath = os.environ['HOME'] + '/.config/claudius/uploadFileTmp'
regionFilePath = os.environ['HOME'] + '/.config/claudius/newScreen.png'
command = config['Main']['terminal'] + ' -e sh -c "ranger --choosefile="' + filePath

@client.event
async def on_ready():
    print('Connected!')
    print('Monitoring for: ' + client.user.name)

@client.event
async def on_message(message):
    if message.author == client.user:
        if message.content == config['Main']['qtuploadcommand']:
            await client.delete_message(message)
            proc = subprocess.Popen('imagedialogqt', stdout=subprocess.PIPE)
            proc.wait()
            output = proc.stdout.readlines()
            for line in output:
                line = str(line, 'utf-8')
                print('Uploading: ' + line)
                with open(filePath, 'w') as uploadFile:
                    uploadFile.write(line)
                await client.send_file(message.channel, line)
        
        if message.content == config['Main']['uploadcommand']:
            await client.delete_message(message)
            os.system(command)
            with open(filePath) as uploadFile:
                pathToUpload = uploadFile.readline()
                print('Uploading: ' + pathToUpload)
                await client.send_file(message.channel, pathToUpload)

        if message.content == config['Main']['reuploadcommand']:
            await client.delete_message(message)
            with open(filePath) as uploadFile:
                pathToUpload = uploadFile.readline()
                print('Uploading: ' + pathToUpload)
                await client.send_file(message.channel, pathToUpload)

        if message.content == config['Main']['regionuploadcommand']:
            await client.delete_message(message)
            os.system('import ' + regionFilePath)
            os.system('convert ' + regionFilePath + ' -shave 1x1 ' + regionFilePath)
            await client.send_file(message.channel, regionFilePath)
            print('Uploaded region')
            os.remove(regionFilePath)

if __name__ == '__main__':
    print('Connecting, please wait...')
    client.run(config['Main']['token'], bot=False)

    #MADE BY RAI OBVIOUSLY
