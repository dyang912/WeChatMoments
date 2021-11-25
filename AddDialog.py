import wx


class AddDialog(wx.Dialog):
    def __init__(self, func_callBack, themeColor):
        wx.Dialog.__init__(self, None, -1, title='Post new moment', size=(300, 300))
        self.themeColor = themeColor
        self.func_callBack = func_callBack

        self.InitUI()  # 绘制Dialog的界面

    def InitUI(self):
        panel = wx.Panel(self)

        self.contentInput = wx.TextCtrl(panel, -1, u'Content', pos=(10, 10), size=(260, 195), style=wx.TE_MULTILINE)
        self.contentInput.SetForegroundColour('black')

        sureButton = wx.Button(panel, -1, u'OK', pos=(10, 215), size=(125, 40), style=wx.BORDER_MASK)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, u'Cancel', pos=(145, 215), size=(125, 40), style=wx.BORDER_MASK)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def sureEvent(self, event):
        content = self.contentInput.GetValue()
        # addPYQ
        import SqlServer
        server = SqlServer.SqlServer()
        server.addPYQ(content)
        self.Destroy()
        self.func_callBack()

    def cancleEvent(self, event):
        self.Destroy()
