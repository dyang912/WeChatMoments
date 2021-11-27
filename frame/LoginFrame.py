import wx
from dialog import LoginDialog as logD, RegisterDialog as regD


class LoginFrame(wx.Frame):
    def __init__(self, parent=None, frame_id=-1, update_ui=None, sql_server=None):
        wx.Frame.__init__(self, parent, frame_id, title='LoginPage', size=(280, 400), pos=(500, 200),
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))
        self.sql_server = sql_server
        self.UpdateUI = update_ui
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        logo_title = wx.StaticText(panel, -1, 'WechatMoments', pos=(100, 120))
        logo_title.SetForegroundColour('#32CD32')

        button_login = wx.Button(panel, -1, 'Login', pos=(32, 220), size=(200, 40), style=wx.BORDER_NONE)
        button_login.SetBackgroundColour('#32CD32')
        button_login.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.loginSys, button_login)

        button_register = wx.Button(panel, -1, 'Register', pos=(32, 280), size=(200, 40), style=wx.BORDER_NONE)
        button_register.SetBackgroundColour('#CDCDB4')
        button_register.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.registorSys, button_register)

    def loginSys(self, event):
        dlg = logD.LoginDialog(self.loginFunction, '#32CD32', self.sql_server)
        dlg.Show()

    def registorSys(self, event):
        dlg = regD.RegisterDialog(self.loginFunction, '#32CD32', self.sql_server)
        dlg.Show()

    def loginFunction(self):
        self.UpdateUI(1)
