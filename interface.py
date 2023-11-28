import tkinter as tk
from tkinter import ttk, font as tk_font


UNITS = ['°C', '°F', 'K', '°R']


class TemperatureConverter(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        tk_font.nametofont('TkDefaultFont').configure(size=14)
        default_font = tk_font.nametofont('TkDefaultFont').actual()

        # define widgets
        # row 0
        self.original_temp_label = tk.Label(self, text='Original temp:')
        self.temp_input = tk.Entry(self, width=10, font=default_font)
        self.original_unit_input = ttk.Combobox(self, values=UNITS, width=5, font=default_font)
        self.original_unit_input.current(0)  # set to C by default
        # row 1
        self.convert_to_label = tk.Label(self, text='Convert to:')
        self.destination_unit_input = ttk.Combobox(self, values=UNITS, width=5, font=default_font)
        self.destination_unit_input.current(1)  # set to F by default
        # row 2
        self.convert_btn = tk.Button(self, text='Convert')
        self.result_label = tk.Label(self, text='')

        # place widgets in frame
        self.place_widgets()

    def place_widgets(self):
        padding = {
            'padx': 5,
            'pady': 10,
        }
        self.original_temp_label.grid(row=0, column=0, sticky=tk.E, **padding)
        self.temp_input.grid(row=0, column=1, **padding)
        self.original_unit_input.grid(row=0, column=2, sticky=tk.W, **padding)
        self.convert_to_label.grid(row=1, column=0, sticky=tk.E, **padding)
        self.destination_unit_input.grid(row=1, column=1, sticky=tk.W, **padding)
        self.convert_btn.grid(row=2, column=0, **padding)
        self.result_label.grid(row=2, column=1, columnspan=2, sticky=tk.W)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Temperature Converter')
    main_frame = TemperatureConverter(root)
    main_frame.pack()
    root.mainloop()
