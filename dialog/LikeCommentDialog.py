import wx


class LikeCommentDialog(wx.Dialog):
    def __init__(self, func_callback, theme_color, index, account, sql_server):
        wx.Dialog.__init__(self, None, -1, title='Like&Comment', size=(300, 400))
        self.themeColor = theme_color
        self.func_callBack = func_callback
        self.index = index
        self.account = account
        self.sql_server = sql_server

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        title1 = wx.StaticText(panel, -1, 'Likes:', pos=(10, 5), size=(20, -1))
        title1.SetForegroundColour('#32CD32')

        like_list = self.get_like_list(self.index)
        name_list = wx.StaticText(panel, -1, label=like_list, pos=(10, 25), size=(-1, -1))
        name_list.SetForegroundColour('black')

        title2 = wx.StaticText(panel, -1, 'Comments:', pos=(10, 45), size=(40, -1))
        title2.SetForegroundColour('#32CD32')

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((100, 55))
        result = self.generate_comment(panel, self.index, self.account)
        vbox.Add(result, flag=wx.ALL, border=10)
        panel.SetSizer(vbox)

        self.content_input = wx.TextCtrl(panel, -1, '(Enter Your Comment)', pos=(10, 235), size=(260, 65),
                                         style=wx.TE_MULTILINE)
        self.content_input.SetForegroundColour('black')

        sureButton = wx.Button(panel, -1, 'Confirm', pos=(10, 315), size=(125, 40), style=wx.BORDER_NONE)
        sureButton.SetForegroundColour('white')
        sureButton.SetBackgroundColour(self.themeColor)
        self.Bind(wx.EVT_BUTTON, self.sureEvent, sureButton)

        cancleButton = wx.Button(panel, -1, 'Cancel', pos=(145, 315), size=(125, 40), style=wx.BORDER_NONE)
        cancleButton.SetBackgroundColour('#CDCDB4')
        cancleButton.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)

    def generate_comment(self, panel, index, account):
        result = self.sql_server.get_all_comments(index, account)
        result.reverse()
        if not result:
            return wx.StaticText(panel, -1, '(Empty)')

        vbox = wx.BoxSizer(wx.VERTICAL)

        for index in result:
            mSizer = wx.GridBagSizer(3, 2)

            writer = wx.StaticText(panel, -1, '%s:' % index[1].rstrip())
            writer.SetForegroundColour('#32CD32')
            mSizer.Add(writer, span=(1, 2), pos=(0, 0), flag=wx.LEFT)

            content = wx.StaticText(panel, -1, '%s' % index[3].rstrip())
            mSizer.Add(content, span=(1, 2), pos=(1, 0), flag=wx.LEFT)

            ti = wx.StaticText(panel, -1, '%s' % index[2])
            mSizer.Add(ti, pos=(2, 0), flag=wx.LEFT)

            if index[1].rstrip() == account:
                delete_button = wx.Button(panel, label="Delete", size=(60, 30), name=str(index[2]))
                mSizer.Add(delete_button, pos=(2, 2), flag=wx.LEFT, border=70)
                self.Bind(wx.EVT_BUTTON,
                          lambda evt, i=delete_button.GetName(): self.delete_confirm(evt, self.account, i),
                          delete_button)

            vbox.Add(mSizer)
        return vbox

    def sureEvent(self, event):
        content = self.content_input.GetValue()
        self.sql_server.add_comment(self.index, content)
        self.Destroy()

    def cancleEvent(self, event):
        self.Destroy()

    def delete_confirm(self, event, account, create_time):
        self.sql_server.delete_confirm(account, create_time)
        self.ShowMessageSucess()
        self.Destroy()

    def ShowMessageSucess(self):
        dial = wx.MessageDialog(None, 'Delete Success!', 'info', wx.OK)
        dial.ShowModal()

    def get_like_list(self, index):
        like_list = self.sql_server.get_all_likes(index, self.account)

        if not like_list:
            return "No Likes"
        else:
            result = ""
            for i in like_list:
                result += i[0].rstrip() + ', '
            return result[:-2]


