import tkinter as tk


class TemperatureConverter(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        # define widgets
        ...

        # place widgets in frame
        self.place_widgets()

    def place_widgets(self):
        ...


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Temperature Converter')
    main_frame = TemperatureConverter(root)
    main_frame.pack()
    root.mainloop()
