#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from quamash import QEventLoop
from gbcore.config import make_config
from gbcore.logger import make_logger
from gbclient.image_editor_dialog import ImageEditorDialog
from gbclient.templates.client_window import Ui_client_window
import aiohttp
import asyncio


class Client(object):

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.loop = QEventLoop(self.app)
        asyncio.set_event_loop(self.loop)

        self.config = make_config(
            os.path.join('config', 'env.json'))
        self.logger = make_logger(self.config)
        self.port = self.config['CLIENT']['PORT']
        self.host = self.config['CLIENT']['HOST']
        self.encode = self.config['CLIENT']['ENCODE']

        self.path_img_ab = os.path.join(self.config.root_path, 'app', 'client', 'templates', 'imgs', 'ab.gif')
        self.path_img_ac = os.path.join(self.config.root_path, 'app', 'client', 'templates', 'imgs', 'ac.gif')
        self.path_img_ai = os.path.join(self.config.root_path, 'app', 'client', 'templates', 'imgs', 'ai.gif')

        self.window = QMainWindow()
        self.ui = self.init_ui()
        self.ie_dialog = ImageEditorDialog(self.config)
        self.font = QFont()
        asyncio.ensure_future(self.check_connection(), loop=self.loop)

    def run(self):
        self.window.show()
        self.create_users()
        with self.loop:
            self.loop.run_forever()

    def init_ui(self):
        """
        Инициализация UI.

        Компоненты UI:
            dialogs_list - список контактов
            messanges_list - переписка, список сообщений переписки с выбранным контактом
            messanger_edit - строка редактирования сообщения

            send_button - кнопка отправки сообщения выбранному контакту
            tb_i - кнопка, курсив
            tb_b - кнопка, жирный
            tb_u - кнопка, подчеркнутый
            tb_smile_1 - кнопка, смаил 1
            tb_smile_2 - кнопка, смаил 2
            tb_smile_3 - кнопка, смаил 3
            tb_smile_4 - кнопка, смаил 4
        """
        ui = Ui_client_window()
        ui.setupUi(self.window)
        # Set icons for font buttons
        ui.tb_b.setIcon(QIcon(os.path.join(
            self.config.root_path, 'app', 'client', 'templates', 'imgs', 'b.jpg')))
        ui.tb_i.setIcon(QIcon(os.path.join(
            self.config.root_path, 'app', 'client', 'templates', 'imgs', 'i.jpg')))
        ui.tb_u.setIcon(QIcon(os.path.join(
            self.config.root_path, 'app', 'client', 'templates', 'imgs', 'u.jpg')))
        # Set icons for smile buttons
        ui.tb_smile_1.setIcon(QIcon(self.path_img_ab))
        ui.tb_smile_2.setIcon(QIcon(self.path_img_ac))
        ui.tb_smile_3.setIcon(QIcon(self.path_img_ai))
        # Set icon for image edit dialog
        ui.tb_smile_4.setIcon(
            QIcon(os.path.join(
                self.config.root_path, 'app', 'client', 'templates', 'imgs', 'open.png')))
        # Connect up the buttons.
        ui.send_button.clicked.connect(self.action_send_button_clicked)
        # Connect up the font buttons.
        ui.tb_b.clicked.connect(lambda: self._insert_html_tag('b'))
        ui.tb_i.clicked.connect(lambda: self._insert_html_tag('i'))
        ui.tb_u.clicked.connect(lambda: self._insert_html_tag('u'))
        # Connect up smile buttons
        ui.tb_smile_1.clicked.connect(lambda: self._insert_image(self.path_img_ab))
        ui.tb_smile_2.clicked.connect(lambda: self._insert_image(self.path_img_ac))
        ui.tb_smile_3.clicked.connect(lambda: self._insert_image(self.path_img_ai))
        # Image edit dialog
        ui.tb_smile_4.clicked.connect(self.action_image_edit)
        return ui

    def create_users(self):
        users = ['cnn', 'egor', 'bobr']
        for user in users:
            icon = QIcon(os.path.join(self.config.root_path, '..', 'upload', user + '.jpg'))
            item = QListWidgetItem(user)
            item.setIcon(icon)
            self.ui.dialogs_list.addItem(item)

    def action_send_button_clicked(self):
        asyncio.ensure_future(self.send_message('new'), loop=self.loop)
        # text = self.ui.messanger_edit.toPlainText()
        # future = asyncio.Future()
        # self._loop.run_until_complete(self.send_message(text, future))
        # if future.result() == 200:
        #     self.logger.info("{} | {}".format(__name__, 'Message delivered ...'))
        # else:
        #     self.logger.info("{} | {}".format(__name__, 'Request error ...'))
        # item = QListWidgetItem(text)
        # self.ui.messanges_list.addItem(item)
        # self.ui.messanger_edit.clear()

    async def send_message(self, message):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.github.com/events') as resp:
                print(resp.status)
                print(message)
                print(await resp.text())

    async def check_connection(self):
        async with aiohttp.ClientSession() as session:
            url = 'http://{host}:{port}/'.format(host=self.host, port=self.port)
            async with session.get(url) as resp:
                if resp.status == 200:
                    self.logger.info("{} | {}".format(__name__, 'Server online ...'))
                else:
                    self.logger.info("{} | {}".format(__name__, 'Connection error ...'))

    def action_image_edit(self):
        self.ie_dialog.exec_()

    def _insert_html_tag(self, tag_name):
        text_cursor = self.ui.messanger_edit.textCursor()
        selected_text = text_cursor.selectedText()
        self.ui.messanger_edit.insertHtml("<{tag}>{text}</{tag}>".format(tag=tag_name, text=selected_text))

    def _insert_image(self, image_path):
        self.ui.messanger_edit.insertHtml('<img src="{image_path}" />'.format(image_path=image_path))
