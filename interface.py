import tkinter as tk
from tkinter import ttk, font as tk_font
from convert import convert_temp


UNITS = ['°C', '°F', 'K', '°R']


def switch_unit(unit):
    match unit:
        case '°C':
            return 'celsius'
        case '°F':
            return 'fahrenheit'
        case 'K':
            return 'kelvin'
        case '°R':
            return 'rankine'


class TemperatureConverter(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        tk_font.nametofont('TkDefaultFont').configure(size=14)
        default_font = tk_font.nametofont('TkDefaultFont').actual()

        # define widgets
        # row 0
        self.original_temp_label = tk.Label(self, text='Original temp:')
        self.temp_input = tk.Entry(self, width=10, font=default_font)
        self.original_unit_input = ttk.Combobox(self, values=UNITS, width=5, font=default_font, state='readonly')
        self.original_unit_input.current(0)  # set to C by default
        # row 1
        self.convert_to_label = tk.Label(self, text='Convert to:')
        self.destination_unit_input = ttk.Combobox(self, values=UNITS, width=5, font=default_font, state='readonly')
        self.destination_unit_input.current(1)  # set to F by default
        # row 2
        self.result_label = tk.Label(self, text='')

        # place widgets in frame
        self.place_widgets()

        # update when inputs change
        self.temp_input.bind('<KeyRelease>', lambda _: self.run_convert_temp())
        self.original_unit_input.bind('<<ComboboxSelected>>', lambda _: self.run_convert_temp())
        self.destination_unit_input.bind('<<ComboboxSelected>>', lambda _: self.run_convert_temp())


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
        self.result_label.grid(row=2, column=0, columnspan=2, sticky=tk.W, **padding)

    def run_convert_temp(self):
        original_temp_str = self.temp_input.get()
        original_unit = switch_unit(self.original_unit_input.get())
        destination_unit = switch_unit(self.destination_unit_input.get())

        original_temp = 0.0
        result = ''
        success = False
        valid_temp = True

        try:
            original_temp = float(original_temp_str)
        except ValueError:
            result = 'Invalid temperature'
            valid_temp = False

        if original_temp_str == '':
            valid_temp = True
            result = ''

        if valid_temp:
            destination_temp = convert_temp(original_temp, original_unit, destination_unit)
            result = f'Temperature: {destination_temp:.2f} {self.destination_unit_input.get()}'
            success = True

        # set result_label text to result
        self.result_label.config(text=result, fg='black' if success else 'red')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Temperature Converter')
    main_frame = TemperatureConverter(root)
    main_frame.pack()
    root.mainloop()
