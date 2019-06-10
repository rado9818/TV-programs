import wx
import urllib2

import UpdateProgramInfo
from Programs import LoadPrograms
from Constants import PROVIDERS_URL
from ProgramScreen import ProgramScreen

class ProgramsScreen(wx.Frame):

    sizer = None

    def __init__(self, *args, **kw):
        super(ProgramsScreen, self).__init__(*args, **kw)
        self.InitUI()
        self.fetchProviders()
        UpdateProgramInfo.updateProgram()


    def fetchProviders(self):
        contents = urllib2.urlopen(PROVIDERS_URL).read()
        LoadPrograms(self, contents, sizer)

    def OnClose(self, e):
        self.Close(True)

    def OnProgramClick(self, program):
        print ("Program clicked ", program)
        ProgramScreen(None).Show()


    def InitUI(self):
        global sizer

        closeBtn = wx.Button(self, label='Close')
        closeBtn.Bind(wx.EVT_BUTTON, self.OnClose)


        sizer = wx.BoxSizer(wx.VERTICAL)


        self.SetSizer(sizer)

        self.SetSize((1400, 440))
        self.SetTitle('TV Program')
        self.Centre()
        self.Show(True)


ex = wx.App()
ProgramsScreen(None)

ex.MainLoop()
