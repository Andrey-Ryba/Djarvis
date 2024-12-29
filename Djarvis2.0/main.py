# КЕША 2.0

import config
import stt
import tts
from parsingCeleb import days
from fuzzywuzzy import fuzz
import datetime
import time
from num2words import num2words
import webbrowser
# from selenium import webdriver
# from selenium.webdriver.common.by import By
import random
from kerykeion import AstrologicalSubject


print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")


cmds = config.VA_CMD_LIST


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = voice
        for x in config.VA_ALIAS:
            cmd = cmd.replace(x, "").strip()
        for x in config.VA_TBR:
            cmd = cmd.replace(x, "").strip()
        execute_cmd(cmd)


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    cmd = cmd.lower()
    request = cmd

    for key, value in cmds.items():
        for x in value:
            if x in cmd:
                cmd = key
                break

    if cmd in cmds:
        lis = cmds[cmd]
        for x in lis:
            request = request.replace(x, "").strip()
    # else:
    #     tts.va_speak('ЧТО?')
    
    # if any(cmds[key] in cmd for key in cmds):
    #     print('its working!!')
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "и открывать браузер"
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейч+ас " + num2words(now.hour, lang='ru') + " " + num2words(now.minute, lang='ru')
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                'Программист это машина для преобразования кофе в код']

        tts.va_speak(random.choice(jokes))

    elif cmd == 'open_browser':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("http://python.org")
    
    elif cmd == 'YouTube':
        if request == '':
            webbrowser.open(f'https://www.youtube.com')
        else:
            webbrowser.open(f'https://www.youtube.com/results?search_query={request}')

    elif cmd == 'Zameni':
        webbrowser.open('http://www.kingim7.ru/#/4/raspisanie/zamena.php')
    
    elif cmd == 'SetevoiGorod':
        webbrowser.open('https://e-school.obr.lenreg.ru/authorize/login')
        # time.sleep(3)
        # <div class="primary-button ng-binding" ng-click="$ctrl.login()">Войти</div>
        # driver = webdriver.Chrome()
        # driver.get('https://e-school.obr.lenreg.ru/authorize/login')
        # button = driver.find_element(By.CLASS_NAME, 'primary-button ng-binding')
        # button.click()
    
    elif cmd == 'celebDay':
        tts.va_speak(days)

    else:
        tts.va_speak('Повторите, пожалуйста!')



# начать прослушивание команд
stt.va_listen(va_respond)