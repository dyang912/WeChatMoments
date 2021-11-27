import getopt
import sys

import wx

from model import SqlServer
import guiManager as FrameManager

USER = None


class MainAPP(wx.App):
    sql_server = None
    manager = None
    frame = None

    def __init__(self, sql_server):
        self.sql_server = sql_server
        wx.App.__init__(self)

    def OnInit(self):
        self.manager = FrameManager.GuiManager(self.UpdateUI, self.sql_server)
        self.frame = self.manager.CreateFrame(0)
        self.frame.Show()
        return True

    def UpdateUI(self, frame_type):
        self.frame.Show(False)
        self.frame = self.manager.CreateFrame(frame_type)
        self.frame.Show(True)


def main(argv):
    user, pw = parse_arg(argv)
    sql_server = SqlServer.SqlServer(user, pw)
    app = MainAPP(sql_server)
    app.MainLoop()


def parse_arg(argv):
    user = ""
    pw = ""
    try:
        opts, args = getopt.getopt(argv, "hu:p:", ["user=", "password="])
    except getopt.GetoptError:
        print("main.py -u <db user> -p <db password>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("main.py -u <db user> -p <db password>")
            sys.exit()
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--password"):
            pw = arg
        else:
            assert False, "unhandled option"
    if user == "":
        print("missing db user")
        sys.exit()
    if pw == "":
        print("missing db password")
        sys.exit()
    return user, pw


if __name__ == '__main__':
    main(sys.argv[1:])
