#wxPython 모듈을 불러옴
import wx

#TestFrame 클래스 선언, wx.Frame 값을 받음
class TestFrame(wx.Frame): #창의 틀이라 할 수 있음. 보통 그대로 사용하지 않고 파생 클래스를 하나 만들어 그 안에 여러 위젯으로 GUI 구성.
    #함수를 부르는 객체가 해당 클래스의 인스턴스인지 확인하기 위해 self를 첫 번째로 기입
    #set_info를 통해 값을 할당하지 않으면 get_info를 호출할 수 없는 오류를 줄이기 위해 인스턴스 생성시 변수값을 지정
    def __init__(self,parent,id,title):
        #Frame 앞에 wx는 모듈을 import 한 후 모듈 내부의 함수를 사용하는 방법이다.
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(400,500))
        #wx.Frame.__init__(self,parent=None, title="Close Event") -> 위와 동일한 내용으로 겹칠 필요가 없음
        self.Bind(wx.EVT_CLOSE, self.OnClose) #닫기 이벤트에 대한 이벤트 처리기
        # panel 생성
        panel = wx.Panel(self,-1,(0,0),(300,400), style=wx.SUNKEN_BORDER)
        # self.picture = 을 이용해 객체 내의 정보를 저장, 위에서 설정한 panel에 대한 정보가 wx 모듈 안의 StaticBitmap 함수로 들어간다.
        self.picture=wx.StaticBitmap(panel)
        panel.SetBackgroundColour(wx.WHITE)
        self.picture.SetFocus()
        self.picture.SetBitmap(wx.Bitmap('image/TEST1.bmp'))

    def OnClose(self, event):
        if wx.MessageBox("창을 닫을까요?", "확인", wx.YES_NO) != wx.YES:
            event.Skip(False)
        else:
            self.Destroy()

'''
    def closeWindow(self, event):
        self.Close()

    def OnSelect(self,event):
        self.picture.SetFocus()
        self.picture.SetBitmap(wx.Bitmap('image/TEST1.bmp'))        
'''

#새로운 MyApp 클래스 선언, wx.App 값을 받음
class MyApp(wx.App):
    #wx.App 의 인스턴스가 만들어지면 wxPython 시스템이 초기화되고 초기화 이후 OnInit() 메소드가 자동 호출된다.
    #OnInit을 재정의해서 윈도우와 위젯 생성을 해도 되지만 wx.App의 인스턴스 생성 코드 이후에도 위젯을 생성할 수 있다.
    # * wxPython 이 wxWidget에 파이썬 코드를 입힌 것이고 OnInit은 wxWidget에서 받았다. __init()__ (초기화 메서드, 생성자라고도 함) 호출 후 OnInit이 호출된다. *
    def OnInit(self): # OnInit() 메소드 오버라이딩
        #frame을 통해 창을 띄우며 Parent = None 이므로 이것이 Main frame 이 된다.
        frame = TestFrame(None, -1, "TEST")
        frame.CenterOnScreen()

        StatusBar = frame.CreateStatusBar()
        StatusBar.SetStatusText('StatusBar')

        MenuBar = wx.MenuBar()
        menu = wx.Menu()
        menu.Append(wx.ID_EXIT, 'E&xit\tAlt-X', '종료')
        MenuBar.Append(menu, '&파일')

        menu1 = wx.Menu()
        menu1.Append(200, 'Test', '테스트메뉴')
        menu1.Append(201, 'Copy', '복사')
        menu1.Append(202, 'Paste', '붙여넣기')
        MenuBar.Append(menu1, '&편집')
        frame.SetMenuBar(MenuBar)

        frame.Show(True)
        return True



app = MyApp(0)
#애플리케이션은 시스템이 보내는 이벤트를 감시하다가 해당 이벤트와 연결된 처리기를 호출한다.
app.MainLoop()
