import wx
import main


class LoginDialog(wx.Dialog):
    def __init__(self, func_callBack, themeColor):
        wx.Dialog.__init__(self, None, -1, title='Login', size=(300, 200))
        self.func_callBack = func_callBack
        self.themeColor = themeColor

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        accountLabel = wx.StaticText(panel, -1, 'User', pos=(20, 25))
        accountLabel.SetForegroundColour('black')

        self.accountInput = wx.TextCtrl(panel, -1, u'', pos=(80, 25), size=(180, -1))
        self.accountInput.SetForegroundColour('black')

        passwordLabel = wx.StaticText(panel, -1, 'Password', pos=(20, 65))
        passwordLabel.SetForegroundColour('black')

        self.passwordInput = wx.TextCtrl(panel, -1, u'', pos=(80, 60), size=(180, -1), style=wx.TE_PASSWORD)
        self.passwordInput.SetForegroundColour('black')

        sureButton = wx.Button(panel, -1, u'Login', pos=(15, 105), size=(120, 40), style=wx.BORDER_NONE)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, u'Cancel', pos=(150, 105), size=(120, 40), style=wx.BORDER_NONE)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def sureEvent(self, event):
        account = self.accountInput.GetValue()
        password = self.passwordInput.GetValue()
        # check
        import SqlServer
        server = SqlServer.SqlServer()
        result = server.login(account, password)
        if result:
            main.USER = account
            self.Destroy()
            self.func_callBack()
        else:
            self.ShowMessageWrong()
            pass

    def cancleEvent(self, event):
        self.Destroy()

    def ShowMessageWrong(self):
        dial = wx.MessageDialog(None, 'User Name and Password not matched!', 'Error', wx.OK | wx.ICON_ERROR)
        dial.ShowModal()











