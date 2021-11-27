import wx


class RegisterDialog(wx.Dialog):
    def __init__(self, func_callback, theme_color, sql_server):
        wx.Dialog.__init__(self, None, -1, title='Register', size=(300, 280))
        self.sql_server = sql_server
        self.func_callBack = func_callback
        self.themeColor = theme_color

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

        nameLabel = wx.StaticText(panel, -1, 'Nickname', pos=(20, 105))
        nameLabel.SetForegroundColour('black')
        self.nameInput = wx.TextCtrl(panel, -1, u'', pos=(80, 100), size=(180, -1))
        self.nameInput.SetForegroundColour('black')

        genderLabel = wx.StaticText(panel, -1, 'Gender', pos=(20, 145))
        genderLabel.SetForegroundColour('black')
        list = ['Male', 'Female']
        self.genderChoice = wx.Choice(panel, -1, pos=(80, 140), choices=list)

        sureButton = wx.Button(panel, -1, u'Register', pos=(15, 185), size=(120, 40), style=wx.BORDER_NONE)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, u'Cancel', pos=(150, 185), size=(120, 40), style=wx.BORDER_NONE)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def sureEvent(self, event):
        account = self.accountInput.GetValue()
        password = self.passwordInput.GetValue()
        name = self.nameInput.GetValue()
        genderc = self.genderChoice.GetCurrentSelection()

        if genderc == 0:
            gender = 'Male'
        else:
            gender = 'Famale'

        self.sql_server.register(account, name, gender, password)
        self.Destroy()

    def cancleEvent(self, event):
        self.Destroy()

