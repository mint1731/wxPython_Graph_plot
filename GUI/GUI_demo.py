import wx

class Frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        # 버튼 만드는 코드
        self.btn = wx.Button(self.panel, -1, "Name-a-matic")
        # 버튼 클릭 이벤트에 함수(메쏘드) 연결하는 코드
        self.Bind(wx.EVT_BUTTON, self.GetName, self.btn)
        # 텍스트 박스 만들고, 디폴트 값 넣는 코드
        self.txt = wx.TextCtrl(self.panel, -1, size=(140, -1))
        self.txt.SetValue('name goes here')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.btn)
        sizer.Add(self.txt)

        self.panel.SetSizer(sizer)
        self.Show()

        # 버튼이 눌렸을 때 실행 되는 함수,  사용자의 이름을 얻어 텍스트 박스에 넣어줌

    def GetName(self, e):
        dlg = wx.TextEntryDialog(self.panel, 'Whats yo name?:', "name-o-rama", "",
                                 style=wx.OK)
        dlg.ShowModal()
        self.txt.SetValue(dlg.GetValue())
        dlg.Destroy()

    def OnCloseWindow(self, e):
        self.Destroy()


app = wx.App()
frame = Frame(None, 'My Nameomatic')
app.MainLoop()
