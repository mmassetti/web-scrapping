# -*- coding: utf-8 -*-

import json
import time
import datetime

import pygame

import requests

url = 'https://fwctickets.fifa.com/TopsAkaCalls/Calls.aspx/getRefreshChartAvaDem?l=en&c=BRA'

while True:
    # print '[!] Verificando...'
    while True:
        try:
            r = requests.get(url)
        except:
            pass
        else:
            break

    obj = r.json()['d']

    if obj['success']:
        data = json.loads(obj['data'])['BasicCodes']['PRODUCTPRICES']
    else:
        print 'Erro?'

    for partida in data:
        if int(partida['Quantity']) > 0:
            print datetime.datetime.now(), partida

            if partida['PRPProductId'] in ['IMT58', 'IMT64']:
                pygame.mixer.init()
                pygame.mixer.music.load("fire.wav")
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    continue

    print '-' * 120
    time.sleep(45)
