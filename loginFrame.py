# coding=utf-8
import wx
# 导入wxPython中的通用Button
import wx.lib.buttons as wxButton

import xDialog


class LoginFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='登录界面', size=(280, 400), pos=(500, 200), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))

        self.UpdateUI = UpdateUI
        self.InitUI()  # 绘制UI界面

    def InitUI(self):
        panel = wx.Panel(self)

        logo_title = wx.StaticText(panel, -1, '微信朋友圈', pos=(100, 120))
        logo_title.SetForegroundColour('#32CD32')

        button_Login = wx.Button(panel, -1, '登录', pos=(32, 220), size=(200, 40), style=wx.BORDER_MASK)
        button_Login.SetBackgroundColour('#32CD32')
        button_Login.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.loginSys, button_Login)

        button_registor = wx.Button(panel, -1, '注册', pos=(32, 280), size=(200, 40), style=wx.BORDER_MASK)
        button_registor.SetBackgroundColour('#CDCDB4')
        button_registor.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.registorSys, button_registor)

    def loginSys(self, event):
        dlg = xDialog.LoginDialog(self.loginFunction, '#32CD32')
        dlg.Show()

    def registorSys(self, event):
        dlg = xDialog.RegisterDialog(self.loginFunction, '#32CD32')
        dlg.Show()

    def loginFunction(self):
        self.UpdateUI(1)

