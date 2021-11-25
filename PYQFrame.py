# coding=utf-8
import wx
import time
import main

import LoginDialog


class PYQFrame(wx.Frame):
    account = main.USER

    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='我的朋友圈', size=(280, 400), pos=(500, 200),
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX))

        #self.scroller = wx.ScrolledWindow(self, -1)
        #self.scroller.SetScrollbars(0, 1, 20, 2000)

        self.UpdateUI = UpdateUI
        self.InitUI()  # 绘制UI界面

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        logo_title = wx.StaticText(panel, -1, '%s的朋友圈' % self.account, pos=(100, 0))
        logo_title.SetForegroundColour('#32CD32')
        hbox1.Add(logo_title, flag=wx.RIGHT, border=25)

        button_addf = wx.Button(panel, label="添加朋友", size=(60, 30))
        hbox1.Add(button_addf, flag=wx.ALIGN_RIGHT, border=10)
        self.Bind(wx.EVT_BUTTON, self.addFSys, button_addf)

        button_add = wx.Button(panel, label="添加新朋友圈", size=(100, 30))
        hbox1.Add(button_add, flag=wx.ALIGN_RIGHT, border=10)
        vbox.Add(hbox1, flag=wx.ALIGN_RIGHT, border=10)
        self.Bind(wx.EVT_BUTTON, self.addSys, button_add)

        panel.SetSizer(vbox)

        result = self.generate(panel, main.USER)
        vbox.Add(result)

    def generate(self, panel, account):
        import SqlServer
        server = SqlServer.SqlServer()
        temp = server.search(account)
        temp.reverse()

        vbox = wx.BoxSizer(wx.VERTICAL)

        for index in temp:
            vbox.Add(wx.StaticText(panel, -1, ' '))
            mSizer = wx.GridBagSizer(3, 3)

            writer = wx.StaticText(panel, -1, '%s:' % index[0].rstrip())
            writer.SetForegroundColour('#32CD32')
            mSizer.Add(writer, span=(1, 2), pos=(0, 0), flag=wx.LEFT, border=10)

            content = wx.StaticText(panel, -1, '%s' % index[2].rstrip())
            mSizer.Add(content, span=(1, 2), pos=(1, 0), flag=wx.LEFT, border=10)

            ti = wx.StaticText(panel, -1, '%s' % index[1])
            mSizer.Add(ti, pos=(2, 0), flag=wx.LEFT, border=10)

            if self.likeCheck(index[3]):
                buttonlike = wx.Button(panel, label="取消赞", size=(60, 30), name=str(index[3]))
                mSizer.Add(buttonlike, pos=(2, 1), flag=wx.LEFT, border=5)
                self.Bind(wx.EVT_BUTTON, lambda evt, i=buttonlike.GetName(): self.likeConfirm(evt, i), buttonlike)
            else:
                buttonlike = wx.Button(panel, label="赞", size=(60, 30), name=str(index[3]))
                mSizer.Add(buttonlike, pos=(2, 1), flag=wx.LEFT, border=5)
                self.Bind(wx.EVT_BUTTON, lambda evt, i=buttonlike.GetName(): self.likeConfirm(evt, i), buttonlike)

            buttont = wx.Button(panel, label="更多", size=(60, 30), name=str(index[3]))
            mSizer.Add(buttont, pos=(2, 2), flag=wx.LEFT, border=0)
            self.Bind(wx.EVT_BUTTON, lambda evt, i=buttont.GetName(): self.likeComment(evt, i), buttont)

            vbox.Add(mSizer)
        return vbox

    def likeConfirm(self, event, index):
        import SqlServer
        server = SqlServer.SqlServer()
        server.likeConfirm(index, self.account)
        self.UpdateUI(1)

    def likeCheck(self, index):
        import SqlServer
        server = SqlServer.SqlServer()
        return server.checkLike(index, self.account)

    def likeComment(self, event, index):
        dlg = xDialog.LikeCommentDialog(self.likeComment, '#32CD32', index, self.account)
        dlg.Show()

    def addSys(self, event):
        dlg = xDialog.AddDialog(self.refresh, '#32CD32')
        dlg.Show()

    def addFSys(self, event):
        dlg = xDialog.AddFDialog(self.refresh, '#32CD32')
        dlg.Show()

    def refresh(self):
        self.UpdateUI(1)



