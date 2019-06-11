import wx
import urllib2

import Constants
from Constants import TIME_IN_PAST
from Constants import PROGRAM_FOR_PROVIDER_URL
from cStringIO import StringIO
import sys
import json
import subprocess as s
import TimeUtil
from threading import Timer

class ProgramScreen(wx.Frame):

    sizer = None
    browserList = None
    scheduleData = None

    def __init__(self, *args, **kw):
        super(ProgramScreen, self).__init__(*args, **kw)
        self.index = 0

        self.InitUI()


    def fetchPrograms(self):
        global scheduleData
        print ("requesting ", PROGRAM_FOR_PROVIDER_URL(1))
        contents = urllib2.urlopen(PROGRAM_FOR_PROVIDER_URL(1)).read()
        data = json.loads(contents)
        scheduleData = data
        print data


        for row in data:
            print("data ", row)
            self.list_ctrl.InsertItem(self.index, row['name'])
            self.list_ctrl.SetItem(self.index, 1, row['start_time'])
            self.index += 1
        #LoadPrograms(self, contents, sizer)

    def OnClose(self, e):
        self.Close(True)

    def scheduleNotify(self, delay):
        t = Timer(delay, self.notify)
        t.start()  # af

    def notify(self):
        s.call(['notify-send', 'Show started', 'Go watch your show!'])

    def OnItemClicked(self, event):
        global scheduleData
        print ("Program clicked ", scheduleData[event.GetIndex()])
        timeDiffence = TimeUtil.getDifference(scheduleData[event.GetIndex()]["start_time"], TimeUtil.getCurrentTime())

        if timeDiffence<TIME_IN_PAST:
            message = "Your show is over :("
        else:
            message = "You will be notified when your show starts"
            self.scheduleNotify(timeDiffence*Constants.SECONDS_IN_MINUTE)

        wx.MessageDialog(None, message, caption=wx.MessageBoxCaptionStr,
                      style=wx.OK | wx.CENTRE, pos=wx.DefaultPosition).ShowModal()
        print "difff " + str(timeDiffence)

        #self.scheduleNotify()

    def getData(self, event):
        global browserList

        count = browserList.GetItemCount()

        cols = browserList.GetColumnCount()

        for row in range(count):

            for col in range(cols):
                item = browserList.GetItem(itemId=row, col=col)

                print(item.GetText())

    def InitUI(self):
        global sizer, browserList

        closeBtn = wx.Button(self, label='Close')
        closeBtn.Bind(wx.EVT_BUTTON, self.OnClose)


        sizer = wx.BoxSizer(wx.VERTICAL)



        #test

        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT, pos=(60, 100))

        self.list_ctrl.InsertColumn(0, "Name", width=160)
        self.list_ctrl.InsertColumn(1, "Start Time")

        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemClicked)

        self.fetchPrograms()


        self.SetSizer(sizer)

        self.SetSize((1400, 440))
        self.SetTitle('TV Program')
        self.Centre()
        self.Show(True)