#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import wx
import wx.html
import requests
#import mysql.connector as mariadb


#mariadb_connection = mariadb.connect(user='root', password='kuebfynk', database='aulete',use_unicode=True, charset='utf8')
#cursor = mariadb_connection.cursor()


class Aulete(wx.Frame):

    def __init__(self, parent, title):
        super(Aulete, self).__init__(parent, title=title,size=(690, 550))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel, label='Pesquisa')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)


        self.word = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER)
        hbox1.Add(self.word, proportion=1)

        search = wx.Button(panel,label='Pesquisar')
        hbox1.Add(search, flag=wx.LEFT,border=8)

        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Resultados')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.result = wx.html.HtmlWindow(panel)
        hbox3.Add(self.result,proportion=1,flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)
        vbox.Add((-1, 25))

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.GetText, search)
        self.Bind(wx.EVT_TEXT_ENTER,self.OnKeyDown, self.word)
        if "gtk2" in wx.PlatformInfo:
            self.result.SetStandardFonts()



    def OnKeyDown(self,e):
        text = ""
        word = self.word.GetValue()
        #cursor.execute("SELECT CONVERT(sig USING utf8) FROM verbete WHERE verbete=%s", (word,))

        #for sig in cursor:
            #text = sig
        if text == "":
            url = requests.get("http://www.aulete.com.br/"+word)
            html = url.text

            soup = BeautifulSoup(html)
            for form in soup.findAll('form'):
                text =  form
                #Pesquisar como retirar a tag A
                for a in soup.findAll('a'):
                    a.replaceWithChildren()
                for img in soup.findAll('img'):
                    img.replaceWith("")
                text = text

        self.result.SetPage(str(text))
        #self.result.SetValue(resultOn)
        #self.result.SetFocus()


    def GetText(self,evt):
        text = ""
        word = self.word.GetValue()
        #cursor.execute("SELECT CONVERT(sig USING utf8) FROM verbete WHERE verbete=%s", (word,))
        #for sig in cursor:
            #text = sig
        if text == "":
            url = requests.get("http://www.aulete.com.br/"+word)
            html = url.text

            soup = BeautifulSoup(html)
            for form in soup.findAll('form'):
                text =  form
                #Pesquisar como retirar a tag A
                for a in soup.findAll('a'):
                    a.replaceWithChildren()
                for img in soup.findAll('img'):
                    img.replaceWith("")
                text = text

        self.result.SetPage(str(text))
        #self.result.SetValue(resultOn)



if __name__ == '__main__':

    app = wx.App()
    Aulete(None, title='Aulete')
    app.MainLoop()
