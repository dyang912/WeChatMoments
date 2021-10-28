# coding=utf-8


class GuiManager():
    def __init__(self, UpdateUI):
        self.UpdateUI = UpdateUI
        self.frameDict = {}  # 用来装载已经创建的Frame对象
        self.account = None

    def GetFrame(self, type):
        #frame = self.frameDict.get(type)

        #if frame is None:
            #frame = self.CreateFrame(type)
            #self.frameDict[type] = frame

        return self.CreateFrame(type)

    def CreateFrame(self, type):
        if type == 0:
            import loginFrame
            return loginFrame.LoginFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
        if type == 1:
            import PYQFrame
            return PYQFrame.PYQFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
