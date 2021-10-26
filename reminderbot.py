from pytz import timezone
from datetime import datetime
from bs4 import BeautifulSoup
import discord
import os
import requests
import time
from asyncio import sleep as s

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('.running'):
        await message.channel.send('Yes :slight_smile:')

    if msg.startswith('.help'):
        await message.channel.send('".running" -> to check active or not')

    if msg.startswith('.fhdfgjkfjkfyjyxrthhtherhdfetjmudyah'):
        # await message.channel.send('Reminder Set')
        while (True):

            # await message.channel.send('still running')

            url = 'https://codeforces.com/contests'
            r = requests.get(url)
            htmlContent = r.content

            soup = BeautifulSoup(htmlContent, 'html.parser')

            datatable = soup.find(class_='datatable')

            l = list(datatable.stripped_strings)
            # l.pop(15)
            now = datetime.now(timezone("Asia/Kolkata"))

            current_time = now.strftime("%H:%M:%S")
            current_time = current_time[3:]
            # curdate = now.strftime("%b/%d")

            # await message.channel.send(current_time + ' ' + curdate)

            # if ((current_time == '32:00') or (current_time == '32:01')):
            l = l[5:]

            # await message.channel.send('Inside!!')
            for i in range(len(l)):
                if (l[i] == 'Before start'):

                    contimeleft = l[i + 1]
                    # condate = l[i-2][0:6]
                    # await message.channel.send(contimeleft)

                    # if(curdate == condate):
                    if (len(contimeleft) == 8):
                        # print(contimeleft[0:5])

                        conname = ''

                        if (contimeleft[0:2] == '12'):

                            j = i
                            while (l[j] != 'Until closing' and j != 0):
                                j -= 1

                            if j <= 0:
                                conname = l[0]
                            else:
                                if (l[j + 2] != '*has extra registration'):
                                    conname = l[j + 2]
                                else:
                                    conname = l[j + 3]

                            await message.channel.send('Codeforce Contest')
                            await message.channel.send(conname + ' - ' +
                                                       '11 hr ' +
                                                       contimeleft[3:5] +
                                                       ' min left')
                            await message.channel.send('<@&788645408343719947>')
                            # time.sleep(2)

                        elif (contimeleft[0:2] == '01'):

                            j = i
                            while (l[j] != 'Until closing' and j != 0):
                                j -= 1

                            if j <= 0:
                                conname = l[0]
                            else:
                                if (l[j + 2] != '*has extra registration'):
                                    conname = l[j + 2]
                                else:
                                    conname = l[j + 3]

                            await message.channel.send('Codeforce Contest')
                            await message.channel.send(conname + ' - ' +
                                                       '01 hr ' +
                                                       contimeleft[3:5] +
                                                       ' min left')
                            await message.channel.send('<@&788645408343719947>')
                            # time.sleep(2)

                        elif (contimeleft[0:2] == '00'):

                            j = i
                            while (l[j] != 'Until closing' and j != 0):
                                j -= 1

                            if j <= 0:
                                conname = l[0]
                            else:
                                if (l[j + 2] != '*has extra registration'):
                                    conname = l[j + 2]
                                else:
                                    conname = l[j + 3]

                            await message.channel.send('Codeforce Contest')
                            await message.channel.send(conname + ' - ' +
                                                       '00 hr ' +
                                                       contimeleft[3:5] +
                                                       ' min left')
                            await message.channel.send('<@&788645408343719947>')
                            # time.sleep(2)
            await s(60*60)


client.run(os.getenv('TOKEN'))
