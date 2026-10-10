import wx
class main(wx.Frame):
    def __init__(self):
        super().__init__(None,title="calculator")
        panel=wx.Panel(self)
        self.SetSize(wx.GetDisplaySize())
        self.Centre()
        user=wx.StaticText(panel,-1,"inter calculator")
        self.user_input=wx.TextCtrl(panel,-1)
        self.calculation=wx.Button(panel,-1,"calculator")
        result_calculator=wx.StaticText(panel,-1,"result")
        self.result=wx.TextCtrl(panel,-1,style=wx.TE_MULTILINE+wx.TE_READONLY+wx.HSCROLL)
        self.calculation.Bind(wx.EVT_BUTTON,self.calculation_numbers)
    def calculation_numbers(self,event):
        self.result.Clear()
        try:
            get_number=self.user_input.Value
            if get_number:
                x=eval(get_number)
                self.result.write(str(x))
            else:
                self.result.write("inter numbers only")
        except Exception as e:
            self.result.write("Error. You cannot type letters on this calculator.")
        self.result.SetFocus()
        self.user_input.Clear()
app=wx.App()
window=main()
window.Show()
app.MainLoop()