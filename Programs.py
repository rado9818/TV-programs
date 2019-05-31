import wx
import json
import urllib2
from cStringIO import StringIO

def LoadPrograms(self, content, sizer):
    self.pos = 0
    sizerProgrmas = wx.BoxSizer(wx.HORIZONTAL)
    for program in json.loads(content):
        buf = urllib2.urlopen(program["image"]).read()
        sbuf = StringIO(buf)
        Image = wx.Image(sbuf).ConvertToBitmap()
        staticImage = wx.StaticBitmap(self, -1, Image, (0.5, 0.5))
        print("setting label to ", self.pos)
        staticImage.SetLabel(str(self.pos))
        self.pos += 1

        def action(event):
            print(int(event.GetEventObject().GetLabel()))
            self.OnProgramClick(json.loads(content)[int(event.GetEventObject().GetLabel())])

        staticImage.Bind(wx.EVT_LEFT_DOWN, action)

        sizerProgrmas.Add(staticImage)

    sizer.Add(sizerProgrmas)