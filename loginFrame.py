# coding=utf-8
import wx
import wx.lib.buttons as wxButton

import LoginDialog as logD
import RegisterDialog as regD


class LoginFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='LoginPage', size=(280, 400), pos=(500, 200),
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))

        self.UpdateUI = UpdateUI
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        logo_title = wx.StaticText(panel, -1, 'WechatMoments', pos=(100, 120))
        logo_title.SetForegroundColour('#32CD32')

        button_Login = wx.Button(panel, -1, 'Login', pos=(32, 220), size=(200, 40), style=wx.BORDER_NONE)
        button_Login.SetBackgroundColour('#32CD32')
        button_Login.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.loginSys, button_Login)

        button_registor = wx.Button(panel, -1, 'Register', pos=(32, 280), size=(200, 40), style=wx.BORDER_NONE)
        button_registor.SetBackgroundColour('#CDCDB4')
        button_registor.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.registorSys, button_registor)

    def loginSys(self, event):
        dlg = logD.LoginDialog(self.loginFunction, '#32CD32')
        dlg.Show()

    def registorSys(self, event):
        dlg = regD.RegisterDialog(self.loginFunction, '#32CD32')
        dlg.Show()

    def loginFunction(self):
        self.UpdateUI(1)
