# coding=utf-8

import wx
import main


# 登录
class LoginDialog(wx.Dialog):
    def __init__(self, func_callBack, themeColor):
        wx.Dialog.__init__(self, None, -1, title='登录', size=(300, 200))
        self.func_callBack = func_callBack
        self.themeColor = themeColor

        self.InitUI()  # 绘制Dialog的界面

    def InitUI(self):
        panel = wx.Panel(self)

        accountLabel = wx.StaticText(panel, -1, '账号', pos=(20, 25))
        accountLabel.SetForegroundColour('black')

        self.accountInput = wx.TextCtrl(panel, -1, u'', pos=(80, 25), size=(180, -1))
        self.accountInput.SetForegroundColour('black')

        passwordLabel = wx.StaticText(panel, -1, '密码', pos=(20, 65))
        passwordLabel.SetForegroundColour('black')

        self.passwordInput = wx.TextCtrl(panel, -1, u'', pos=(80, 60), size=(180, -1), style=wx.TE_PASSWORD)
        self.passwordInput.SetForegroundColour('black')

        sureButton = wx.Button(panel, -1, u'登录', pos=(15, 105), size=(120, 40), style=wx.BORDER_MASK)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, u'取消', pos=(150, 105), size=(120, 40), style=wx.BORDER_MASK)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        # 为【取消Button】绑定事件
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
            self.Destroy()  # 销毁隐藏Dialog
            self.func_callBack()
        else:
            self.ShowMessageWrong()
            pass

    def cancleEvent(self, event):
        self.Destroy()  # 销毁隐藏Dialog

    def ShowMessageWrong(self):
        dial = wx.MessageDialog(None, '用户名或密码错误', 'Error', wx.OK | wx.ICON_ERROR)
        dial.ShowModal()



# 注册
class RegisterDialog(wx.Dialog):
    def __init__(self, func_callBack, themeColor):
        wx.Dialog.__init__(self, None, -1, title='注册', size=(300, 280))
        self.func_callBack = func_callBack
        self.themeColor = themeColor

        self.InitUI()  # 绘制Dialog的界面

    def InitUI(self):
        panel = wx.Panel(self)

        accountLabel = wx.StaticText(panel, -1, '账号', pos=(20, 25))
        accountLabel.SetForegroundColour('black')
        self.accountInput = wx.TextCtrl(panel, -1, u'', pos=(80, 25), size=(180, -1))
        self.accountInput.SetForegroundColour('black')

        passwordLabel = wx.StaticText(panel, -1, '密码', pos=(20, 65))
        passwordLabel.SetForegroundColour('black')
        self.passwordInput = wx.TextCtrl(panel, -1, u'', pos=(80, 60), size=(180, -1), style=wx.TE_PASSWORD)
        self.passwordInput.SetForegroundColour('black')

        nameLabel = wx.StaticText(panel, -1, '昵称', pos=(20, 105))
        nameLabel.SetForegroundColour('black')
        self.nameInput = wx.TextCtrl(panel, -1, u'', pos=(80, 100), size=(180, -1))
        self.nameInput.SetForegroundColour('black')

        genderLabel = wx.StaticText(panel, -1, '性别', pos=(20, 145))
        genderLabel.SetForegroundColour('black')
        list = ['男', '女']
        self.genderChoice = wx.Choice(panel, -1, pos=(80, 140), choices=list)

        sureButton = wx.Button(panel, -1, u'注册', pos=(15, 185), size=(120, 40), style=wx.BORDER_MASK)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, u'取消', pos=(150, 185), size=(120, 40), style=wx.BORDER_MASK)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        # 为【取消Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def sureEvent(self, event):
        account = self.accountInput.GetValue()
        password = self.passwordInput.GetValue()
        name = self.nameInput.GetValue()
        genderc = self.genderChoice.GetCurrentSelection()

        if genderc == 0:
            gender = '男'
        else:
            gender = '女'

        # register
        import SqlServer
        server = SqlServer.SqlServer()
        server.register(account, name, gender, password)
        self.Destroy()  # 销毁隐藏Dialog

    def cancleEvent(self, event):
        self.Destroy()  # 销毁隐藏Dialog


# 添加朋友
class AddFDialog(wx.Dialog):
    def __init__(self, func_callBack, themeColor):
        wx.Dialog.__init__(self, None, -1, title='添加朋友', size=(300, 150))
        self.themeColor = themeColor
        self.func_callBack = func_callBack

        self.InitUI()  # 绘制Dialog的界面

    def InitUI(self):
        panel = wx.Panel(self)

        self.contentInput = wx.TextCtrl(panel, -1, u'输入ID', pos=(10, 10), size=(260, 40))
        self.contentInput.SetForegroundColour('black')

        sureButton = wx.Button(panel, -1, u'确定', pos=(10, 60), size=(125, 40), style=wx.BORDER_MASK)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, u'取消', pos=(145, 60), size=(125, 40), style=wx.BORDER_MASK)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        # 为【取消Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def sureEvent(self, event):
        content = self.contentInput.GetValue()
        # addPYQ
        import SqlServer
        server = SqlServer.SqlServer()
        result = server.addFriend(content)
        if result:
            self.ShowMessageSucess()
        else:
            self.ShowMessageWrong()
        self.Destroy()  # 销毁隐藏Dialog
        self.func_callBack()

    def cancleEvent(self, event):
        self.Destroy()  # 销毁隐藏Dialog

    def ShowMessageWrong(self):
        dial = wx.MessageDialog(None, '此ID不存在 或 已添加过好友', 'Error', wx.OK | wx.ICON_ERROR)
        dial.ShowModal()

    def ShowMessageSucess(self):
        dial = wx.MessageDialog(None, '添加成功!', 'info', wx.OK)
        dial.ShowModal()


# 添加新朋友圈
class AddDialog(wx.Dialog):
    def __init__(self, func_callBack, themeColor):
        wx.Dialog.__init__(self, None, -1, title='添加新朋友圈', size=(300, 300))
        self.themeColor = themeColor
        self.func_callBack = func_callBack

        self.InitUI()  # 绘制Dialog的界面

    def InitUI(self):
        panel = wx.Panel(self)

        self.contentInput = wx.TextCtrl(panel, -1, u'输入你的内容', pos=(10, 10), size=(260, 195), style=wx.TE_MULTILINE)
        self.contentInput.SetForegroundColour('black')

        sureButton = wx.Button(panel, -1, u'确定', pos=(10, 215), size=(125, 40), style=wx.BORDER_MASK)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, u'取消', pos=(145, 215), size=(125, 40), style=wx.BORDER_MASK)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        # 为【取消Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def sureEvent(self, event):
        content = self.contentInput.GetValue()
        # addPYQ
        import SqlServer
        server = SqlServer.SqlServer()
        server.addPYQ(content)
        self.Destroy()  # 销毁隐藏Dialog
        self.func_callBack()

    def cancleEvent(self, event):
        self.Destroy()  # 销毁隐藏Dialog


# 点赞评论页面
class LikeCommentDialog(wx.Dialog):
    def __init__(self, func_callBack, themeColor, index, account):
        wx.Dialog.__init__(self, None, -1, title='点赞和评论', size=(300, 400))
        self.themeColor = themeColor
        self.func_callBack = func_callBack
        self.index = index
        self.account = account

        self.InitUI()  # 绘制Dialog的界面

    def InitUI(self):
        panel = wx.Panel(self)

        title1 = wx.StaticText(panel, -1, '赞：', pos=(10, 5), size=(20, -1))
        title1.SetForegroundColour('#32CD32')

        likelist = self.getLikeList(self.index)
        nameList = wx.StaticText(panel, -1, label=likelist, pos=(10, 25), size=(-1, -1))
        nameList.SetForegroundColour('black')

        title2 = wx.StaticText(panel, -1, '评论：', pos=(10, 45), size=(40, -1))
        title2.SetForegroundColour('#32CD32')

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((100, 55))
        result = self.generateComment(panel, self.index, main.USER)
        vbox.Add(result, flag=wx.ALL, border=10)
        panel.SetSizer(vbox)

        self.contentInput = wx.TextCtrl(panel, -1, u'输入你评论的内容', pos=(10, 235), size=(260, 65), style=wx.TE_MULTILINE)
        self.contentInput.SetForegroundColour('black')

        sureButton = wx.Button(panel, -1, u'添加评论', pos=(10, 315), size=(125, 40), style=wx.BORDER_MASK)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        # 为【确定Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, u'取消', pos=(145, 315), size=(125, 40), style=wx.BORDER_MASK)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        # 为【取消Button】绑定事件
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def generateComment(self, panel, index, account):
        import SqlServer
        server = SqlServer.SqlServer()
        temp = server.searchComment(index, account)
        temp.reverse()
        # print(temp)
        if not temp:
            return wx.StaticText(panel, -1, '空')

        vbox = wx.BoxSizer(wx.VERTICAL)

        for index in temp:
            mSizer = wx.GridBagSizer(3, 2)

            writer = wx.StaticText(panel, -1, '%s:' % index[1].rstrip())
            writer.SetForegroundColour('#32CD32')
            mSizer.Add(writer, span=(1, 2), pos=(0, 0), flag=wx.LEFT)

            content = wx.StaticText(panel, -1, '%s' % index[3].rstrip())
            mSizer.Add(content, span=(1, 2), pos=(1, 0), flag=wx.LEFT)

            ti = wx.StaticText(panel, -1, '%s' % index[2])
            mSizer.Add(ti, pos=(2, 0), flag=wx.LEFT)

            if index[1].rstrip() == account:
                buttont = wx.Button(panel, label="删除", size=(60, 30), name=str(index[2]))
                mSizer.Add(buttont, pos=(2, 2), flag=wx.LEFT, border=70)
                self.Bind(wx.EVT_BUTTON, lambda evt, i=buttont.GetName(): self.deleteConfirm(evt, self.account, i), buttont)

            vbox.Add(mSizer)
        return vbox

    def sureEvent(self, event):
        content = self.contentInput.GetValue()
        # addPYQ
        import SqlServer
        server = SqlServer.SqlServer()
        server.addComment(self.index, content)
        self.Destroy()  # 销毁隐藏Dialog

    def cancleEvent(self, event):
        self.Destroy()  # 销毁隐藏Dialog

    def deleteConfirm(self, event, acconut, ti):
        import SqlServer
        server = SqlServer.SqlServer()
        server.deleteConfirm(acconut, ti)
        self.ShowMessageSucess()
        self.Destroy()

    def ShowMessageSucess(self):
        dial = wx.MessageDialog(None, '删除成功!', 'info', wx.OK)
        dial.ShowModal()

    def getLikeList(self, index):
        import SqlServer
        server = SqlServer.SqlServer()
        temp = server.searchLike(index, self.account)
        result = ""

        if not temp:
            return "无"
        else:
            for i in temp:
                result += i[0].rstrip() + ', '
            return result[:-2]





