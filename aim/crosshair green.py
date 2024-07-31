import tkinter as tk
import win32gui
import win32con

class CrosshairApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.geometry("+0+0")
        self.root.lift()
        self.root.wm_attributes("-transparentcolor", "black")
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.canvas = tk.Canvas(self.root, width=screen_width, height=screen_height, highlightthickness=0, bg='black')
        self.canvas.pack()

        crosshair_color = 'green'
        segment_length = 20
        gap = 10
        circle_radius = 50
        line_width = 4  # Αυξημένο πάχος γραμμών
        dot_radius = 5  # Ακτίνα για την τελεία στο κέντρο

        # Draw crosshair segments
        self.canvas.create_line(screen_width//2 - gap - segment_length, screen_height//2, screen_width//2 - gap, screen_height//2, fill=crosshair_color, width=line_width)
        self.canvas.create_line(screen_width//2 + gap, screen_height//2, screen_width//2 + gap + segment_length, screen_height//2, fill=crosshair_color, width=line_width)
        self.canvas.create_line(screen_width//2, screen_height//2 - gap - segment_length, screen_width//2, screen_height//2 - gap, fill=crosshair_color, width=line_width)
        self.canvas.create_line(screen_width//2, screen_height//2 + gap, screen_width//2, screen_height//2 + gap + segment_length, fill=crosshair_color, width=line_width)

        # Draw circle
        self.canvas.create_oval(screen_width//2 - circle_radius, screen_height//2 - circle_radius,
                                screen_width//2 + circle_radius, screen_height//2 + circle_radius,
                                outline=crosshair_color, width=line_width)

        # Draw center dot
        self.canvas.create_oval(screen_width//2 - dot_radius, screen_height//2 - dot_radius,
                                screen_width//2 + dot_radius, screen_height//2 + dot_radius,
                                fill=crosshair_color, outline=crosshair_color)

        self.root.bind('<Escape>', self.close_app)
        
        # Make the window click-through
        hwnd = win32gui.FindWindow(None, str(self.root))
        ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)

    def close_app(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CrosshairApp(root)
    root.mainloop()
