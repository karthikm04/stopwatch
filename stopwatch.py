import tkinter as tk
from datetime import datetime, timedelta

class CircularStopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Circular Stopwatch")
        
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0

        self.bg_color = "#2C3E50"  # Lavender color for background
        self.fg_color = "#ECF0F1"  # Black color for text
        self.button_color = "#E74C3C"  # Cyan color for buttons
        circle_border_color = "#3498DB"  # Peter River Blue for the circle borde

        # Create the canvas
        self.canvas = tk.Canvas(root, width=300, height=300, bg=self.bg_color, highlightthickness=0)
        self.canvas.pack(padx=20, pady=20)

        # Draw the circular background
        self.canvas.create_oval(20, 20, 280, 280, outline=circle_border_color, fill=self.bg_color, width=5)
        # Create the stopwatch label in the center
        self.label = self.canvas.create_text(150, 150, text="00:00:00.000", font=("Arial", 24), fill=self.fg_color)

        # Create buttons
        self.start_button = tk.Button(root, text="Start", command=self.start, bg=self.button_color, font=("Arial", 14))
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop, bg=self.button_color, font=("Arial", 14))
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset, bg=self.button_color, font=("Arial", 14))
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update_clock()

    def start(self):
        if not self.is_running:
            self.start_time = datetime.now() - timedelta(milliseconds=self.elapsed_time)
            self.is_running = True
            self.update_clock()

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.elapsed_time = (datetime.now() - self.start_time).total_seconds() * 1000

    def reset(self):
        self.is_running = False
        self.elapsed_time = 0
        self.canvas.itemconfig(self.label, text="00:00:00.000")

    def update_clock(self):
        if self.is_running:
            current_time = datetime.now() - self.start_time
            time_str = self.format_time(current_time.total_seconds())
            self.canvas.itemconfig(self.label, text=time_str)
        self.root.after(100, self.update_clock)  # Update every 100 milliseconds

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = int((seconds - int(seconds)) * 1000)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{milliseconds:03}"

if __name__ == "__main__":
    root = tk.Tk()
    app = CircularStopwatch(root)
    root.mainloop()
