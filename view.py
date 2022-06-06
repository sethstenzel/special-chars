import queue
import wx
import sys

class BorderlessUI(wx.Frame):
    
    def __init__(self, view_msg_queue, termination_flag):
        wx.Frame.__init__(self, None, -1, "SpecialChars", style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER)

        self.view_msg_queue = view_msg_queue
        self.termination_flag = termination_flag

        self.window_width = 520
        self.window_height = 167
        self.SetClientSize((self.window_width, self.window_height))
        
        _, client_res_height = wx.DisplaySize()
        self.x_position = 75
        self.y_position = client_res_height - self.window_height - 100     
        self.SetPosition(wx.Point((self.x_position, self.y_position)))

        self.images_directory = ".\\graphics\\"
        self.initial_bg_image = f"{self.images_directory}initial.bmp"

        self.bmp = wx.Image(self.initial_bg_image, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmp = self.scale_bitmap(self.bmp, self.window_width, self.window_height)
        self.transparentColour = wx.Colour(119, 119, 119, alpha=wx.ALPHA_OPAQUE)

        self.ico = wx.Icon(f"{self.images_directory}special_chars_icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.ico)  
        
        self.dc = wx.ClientDC(self)
        self.dc.DrawBitmap(self.bmp, 0,0, True)
        self.set_window_shape()
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_WINDOW_CREATE, self.set_window_shape)

        self.update_timer = wx.Timer(self)
        self.update_timer.Start(milliseconds=int(25))
        self.Bind(wx.EVT_TIMER, self.check_queues)

    def check_queues(self, *args):
        try:
            if not self.termination_flag.empty():
                self.exit_view()
            msg = ""
            if not self.view_msg_queue.empty():
                msg = self.view_msg_queue.get()
            if msg == "show":
                self.Show()
            elif msg == "hide":
                self.Hide()
            elif ".bmp" in msg:
                self.update_bg(msg)
        except Exception as e:
            self.termination_flag.put(True)
            self.exit_view()
            

    def update_bg(self, bg):
        bg = f"{self.images_directory}{bg}"
        new_bmp = wx.Image(bg, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmp = self.scale_bitmap(new_bmp, self.window_width, self.window_height)
        self.dc.DrawBitmap(self.bmp, 0,0, True)

    def set_window_shape(self, *args):
        r = wx.Region(self.bmp , self.transparentColour)
        self.hasShape = self.SetShape(r)

    def on_paint(self, *args):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0, True)

    def exit_view(self):
        self.Destroy()
        self.Close()
        sys.exit()

    @staticmethod
    def scale_bitmap(bmp, width, height):
        image = wx.Bitmap.ConvertToImage(bmp)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        return wx.Bitmap(image)

def view(view_msg_queue, termination_flag):
    try:
        app_view = wx.App()
        view_window = BorderlessUI(view_msg_queue, termination_flag)
        view_window.Show()
        app_view.MainLoop()
    except:
        termination_flag.put(True)
        sys.exit()