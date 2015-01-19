#!/usr/bin/python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import wx
import urllib
import urllib2


numberDicDown  = ['1','2','3','4','5','6','7','8','9','10']
numberDicUp  = ['11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40']


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
		###################################################################
		###################################################################
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		st2 = wx.StaticText(panel, label='Resultados')
		st2.SetFont(font)
		hbox2.Add(st2)
		vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

		vbox.Add((-1, 10))

		###################################################################
		###################################################################

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		self.result = wx.TextCtrl(panel,style=wx.TE_MULTILINE)
		hbox3.Add(self.result, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)

		vbox.Add((-1, 25))

		panel.SetSizer(vbox)

		self.Bind(wx.EVT_BUTTON, self.GetText, search)
		self.Bind(wx.EVT_TEXT_ENTER,self.OnKeyDown, self.word)

		###################################################################
		###################################################################


	def OnKeyDown(self,e):
		word = self.word.GetValue()
		word = word.encode('utf8')

		url = urllib2.urlopen("http://www.aulete.com.br/"+word)
		html = url.read()

		soup = BeautifulSoup(html)
		for form in soup.findAll('form'):
			text =  form
		for br in soup.findAll('br'):
			br.extract()
		resultOn = text.getText()
		resultOn = resultOn.replace('1    ','\n\n')
		resultOn = resultOn.replace('1   ','\n\n')
		resultOn = resultOn.replace('1  ','\n\n')
		for number in numberDicUp:
			resultOn = resultOn.replace(number+'.','\n\n'+number+'-')
		for number in numberDicDown:
			resultOn = resultOn.replace(number+'.','\n\n'+number+'-')




		self.result.SetValue(resultOn)
		self.result.SetFocus()


	def GetText(self,evt):
		word = self.word.GetValue()

		url = urllib2.urlopen("http://www.aulete.com.br/"+word)
		html = url.read()

		soup = BeautifulSoup(html)
		for form in soup.findAll('form'):
			text =  form
			for br in soup.findAll('br'):
				br.extract()
			resultOn = text.getText()
			resultOn = resultOn.replace('1    ','\n\n')
			resultOn = resultOn.replace('1   ','\n\n')
			resultOn = resultOn.replace('1  ','\n\n')
			for number in numberDicUp:
				resultOn = resultOn.replace(number+'.','\n\n'+number+'-')
			for number in numberDicDown:
				resultOn = resultOn.replace(number+'.','\n\n'+number+'-')



		self.result.SetValue(resultOn)



if __name__ == '__main__':

	app = wx.App()
	Aulete(None, title='Aulete')
	app.MainLoop()
