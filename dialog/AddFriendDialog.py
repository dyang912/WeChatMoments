import wx


class AddFriendDialog(wx.Dialog):
    def __init__(self, func_callBack, themeColor, sql_server):
        wx.Dialog.__init__(self, None, -1, title='Add Friend', size=(300, 150))
        self.themeColor = themeColor
        self.func_callBack = func_callBack
        self.sql_server = sql_server

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        self.contentInput = wx.TextCtrl(panel, -1, 'Enter ID', pos=(10, 10), size=(260, 40))
        self.contentInput.SetForegroundColour('black')

        sureButton = wx.Button(panel, -1, 'OK', pos=(10, 60), size=(125, 40), style=wx.BORDER_NONE)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, 'Cancel', pos=(145, 60), size=(125, 40), style=wx.BORDER_NONE)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def sureEvent(self, event):
        content = self.contentInput.GetValue()
        result = self.sql_server.add_friend(content)
        if result:
            self.ShowMessageSucess()
        else:
            self.ShowMessageWrong()
        self.Destroy()
        self.func_callBack()

    def cancleEvent(self, event):
        self.Destroy()

    def ShowMessageWrong(self):
        dial = wx.MessageDialog(None, 'ID not exist or Already are friends', 'Error', wx.OK | wx.ICON_ERROR)
        dial.ShowModal()

    def ShowMessageSucess(self):
        dial = wx.MessageDialog(None, 'Add success!', 'info', wx.OK)
        dial.ShowModal()
