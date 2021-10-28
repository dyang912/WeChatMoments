# coding:utf-8
import wx
import guiManager as FrameManager
'''
def login_event(event):
    id = user_text.GetValue()
    pw = password_text.GetValue()


def quit_event(event):     # 定义打开文件事件
    frame.Close()
'''
USER = None


class MainAPP(wx.App):

    manager = None
    frame = None

    def OnInit(self):
        self.manager = FrameManager.GuiManager(self.UpdateUI)
        self.frame = self.manager.GetFrame(0)
        self.frame.Show()
        return True

    def UpdateUI(self, type):
        self.frame.Show(False)
        self.frame = self.manager.GetFrame(type)
        self.frame.Show(True)


def main():
    app = MainAPP()
    app.MainLoop()


if __name__ == '__main__':
    main()
