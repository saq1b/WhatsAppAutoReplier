# -*- coding: utf-8 -*- 

import wx
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep

# br = webdriver.Chrome()
global br
class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		# self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.heading = wx.StaticText( self, wx.ID_ANY, u"WhatsApp Auto Replier", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.heading.Wrap( -1 )
		self.heading.SetFont( wx.Font( 24, 70, 90, 90, False, "Terminal" ) )
		
		bSizer1.Add( self.heading, 0, wx.ALL|wx.EXPAND, 5 )
		
		self._instruction = wx.StaticText( self, wx.ID_ANY, u"Enter Reply Message", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._instruction.Wrap( -1 )
		bSizer1.Add( self._instruction, 0, wx.ALL, 5 )
		
		self._message = wx.TextCtrl( self, wx.ID_ANY, u"Thank You", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self._message, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		# self._initializeButton = wx.Button( self, wx.ID_ANY, u"Initialize Setup", wx.DefaultPosition, wx.DefaultSize, 0 )
		# bSizer1.Add( self._initializeButton, 1, wx.ALL, 5 )
		
		self._startButton = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self._startButton, 1, wx.ALL|wx.EXPAND, 5 )

		self._stopButton = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self._stopButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		self._logs = wx.StaticText( self, wx.ID_ANY, u"Logs :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._logs.Wrap( -1 )
		bSizer1.Add( self._logs, 0, wx.ALL, 5 )
		
		self._logText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self._logText, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		# self._initializeButton.Bind( wx.EVT_BUTTON, self.initialize )
		self._stopButton.Bind( wx.EVT_BUTTON, self.stop )
		self._startButton.Bind( wx.EVT_BUTTON, self.start )
	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def initialize( self, event ):				
		event.Skip()
	
	def stop( self, event ):   
		event.Skip()
	
	def start( self, event ):
		br = webdriver.Chrome()
		br.get("https://web.whatsapp.com")
		while 1:
			newM = br.find_elements_by_class_name("OUeyt")
			print("start")
			if(len(newM)>0):
				newM = newM[-1]
				print("New Message")
				action = webdriver.common.action_chains.ActionChains(br)
				action.move_to_element_with_offset(newM, 0, -20)
				try:
					action.click()
					action.perform()
					action.click()
					action.perform()
					print("clicked",end=' ')
				except Exception as e:
					pass
				try:
					# name = br.find_elements_by_class_name("_25Ooe").text
					# print(name)   #_3zb-j ZhF0n  ->
					message=""
					while(not message):
						# I SUSPECT, HERE IS THE FAULT (may work next time, changed lower to lower()) NOW ITS WORKING
						message = br.find_elements_by_class_name("vW7d1")[-1].text.split('\n')[0] # message = br.find_elements_by_css_selector("._3zb-j.ZhF0n")
						print(message)
				#			message = br.find_elements_by_class_name("vW7d1")[-1]
					if(message.lower().find("happy birthday")!=-1):   # regex ^.*happy birthday.*$
						print("Happy Birthday Found",end=' ')
						textBox = br.find_elements_by_class_name("_2S1VP")[-1]
						# textBox.clear()
						reply=self._message.Text()+'\n' # put \n to send 
						textBox.send_keys(reply) 
						print("Replied",end=' ')
				except Exception as e:
					pass
			sleep(2)
		#event.Skip()

app=wx.App()
frame=MyFrame1(None)
frame.Show(True)
app.MainLoop()
