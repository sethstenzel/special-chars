import wx
import sys
import time
import sys
import traceback

class BorderlessUI(wx.Frame):
    
    def __init__(self, view_msg_queue, termination_flag, has_focus):
        wx.Frame.__init__(self, None, -1, "SpecialChars", style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER)

        self.view_msg_queue = view_msg_queue
        self.termination_flag = termination_flag
        self.has_focus = has_focus

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
        self.Bind(wx.EVT_SET_FOCUS, self.gained_focus)
        self.Bind(wx.EVT_KILL_FOCUS, self.lost_focus)
        
        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_mouse_up)
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_mouse_down)
        self.Bind(wx.EVT_RIGHT_UP, self.on_mouse_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_dragging)
        self.SetFocus()

    
    def gained_focus(self, *args):
        if self.has_focus.empty():
            self.has_focus.put(True)

    def lost_focus(self, *args):
        if not self.has_focus.empty():
            self.has_focus.get()

    def check_queues(self, *args):
        try:
            if not self.termination_flag.empty():
                self.exit_view()
            msg = ""
            if not self.view_msg_queue.empty():
                msg = self.view_msg_queue.get()
            if msg == "show":
                self.Show()
                self.SetFocus()
            elif msg == "hide":
                self.Hide()
            elif ".bmp" in msg:
                self.update_bg(msg)
        except Exception as e:
            self.termination_flag.put(True)
            traceback.print_exc()
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


    def on_mouse_down(self, event):
        self.CaptureMouse()
        pos = self.ClientToScreen(event.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)

    def on_mouse_dragging(self, event):
        if  event.Dragging() and (event.RightIsDown() or event.LeftIsDown()):
            pos = self.ClientToScreen(event.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)

    def on_mouse_up(self, event):
        if self.HasCapture():
            self.ReleaseMouse()



def view(view_msg_queue, termination_flag, has_focus):
    try:
        app_view = wx.App()
        view_window = BorderlessUI(view_msg_queue, termination_flag, has_focus)
        view_window.Show()
        app_view.MainLoop()
    except Exception:
        traceback.print_exc()
        termination_flag.put(True)
        sys.exit()