class GuiManager:
    def __init__(self, update_ui, sql_server):
        self.sql_server = sql_server
        self.update_ui = update_ui
        self.frameDict = {}
        self.account = None

    def CreateFrame(self, frame_type):
        if frame_type == 0:
            from frame import LoginFrame
            return LoginFrame.LoginFrame(frame_id=frame_type, update_ui=self.update_ui, sql_server=self.sql_server)
        if frame_type == 1:
            from frame import MomentsFrame
            return MomentsFrame.PYQFrame(id=frame_type, UpdateUI=self.update_ui, sql_server=self.sql_server)
