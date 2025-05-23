import tkinter as tk
from tkinter import messagebox

from tables import StateTable, ImplicationTable


class ImplicationTableReducerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)

        self.table_entries = []
        self.title('Implication Table Reducer')

        self._input_frame = tk.Frame(self, borderwidth=0)
        self._input_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=10)

        self._states_count_entry = self.create_input(self._input_frame,
                                                    'Enter number of states:', width=5, row=0, col=0)

        self._inputs_count_entry = self.create_input(self._input_frame,
                                                    'Enter number of inputs:', width=5, row=1, col=0,)

        self._circuit_type_var = tk.StringVar(value='Mealy')
        self._circuit_type_entry = self.create_option_menu(self._input_frame,
                                                          'Choose circuit type:', self._circuit_type_var,
                                                           ['Mealy', 'Moore'], row=2, col=0)

        self._update_button = tk.Button(self._input_frame, text='Update Table', command=self.update_table)
        self._update_button.grid(row=3, column=0, sticky='nsew')

        self._calculate_button = tk.Button(self._input_frame, text='Calculate', command=self.calculate_table_data)
        self._calculate_button.grid(row=4, column=0, sticky='nsew')

        self._table_frame = tk.Frame(self, borderwidth=0)
        self._table_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=10)

    def get_input_count(self):
        return int(self._inputs_count_entry.get())

    def get_states_count(self):
        return int(self._states_count_entry.get())

    def get_circuit_type(self):
        return self._circuit_type_var.get()

    def create_input(self, parent, label_text, row, col, **entry_options):
        frame = tk.Frame(parent, borderwidth=0)
        frame.grid(row=row, column=col, sticky='nsew', pady=5)

        label = tk.Label(frame, text=label_text)
        label.grid(row=0, column=0, sticky='nsew')

        entry = tk.Entry(frame, **entry_options)
        entry.grid(row=0, column=1, sticky='nsew')

        return entry

    def create_option_menu(self, parent, label_text, variable, options, row, col):
        frame = tk.Frame(parent, borderwidth=0)
        frame.grid(row=row, column=col, sticky='nsew', pady=5)

        label = tk.Label(frame, text=label_text)
        label.grid(row=0, column=0, sticky='nsew')

        option_menu = tk.OptionMenu(frame, variable, *options)
        option_menu.grid(row=0, column=1, sticky='nsew')

        return option_menu

    def calculate_table_data(self):
        try:
            table_data = [[entry.get() for entry in row] for row in self.table_entries]

            input_count = self.get_input_count()

            s_table = StateTable()

            for row in table_data:
                next_states = row[:input_count]
                for next_state in next_states:
                    if next_state == '' or ord(next_state) - ord('a') >= self.get_states_count():
                        raise ValueError

                outputs = row[input_count:]
                for output in outputs:
                    if output == '' or output not in ['0', '1']:
                        raise ValueError

                s_table.add([ord(x.lower()) - ord('a') for x in next_states], [ord(x) - ord('0') for x in outputs])

            s_table.row_match()

            print("AFTER ROW MATCHING:")
            s_table.print_table()

            i_table = ImplicationTable(s_table)

            print("\nIMPLICATION TABLE:")
            i_table.print_table()

            i_table.imply()

            print("IMPLICATION TABLE AFTER REDUCTION:")
            i_table.print_table()

            print("REMAINING STATES:")

            remaining_states = i_table.get_remaining_states()
            for state in remaining_states:
                print("{", end=" ")
                for x in state:
                    print(chr(ord('a') + x), end=" ")
                print("}", end=" ")
            print()

            print("\nCLASSIFICATION:")
            classes = i_table.classify()

            for c in classes:
                print("{", end=" ")

                for x in c:
                    print(chr(ord('a') + x), end=" ")

                print("}", end=" ")

            print()

            reduced_table = i_table.get_reduced_table(classes)

            # reduced_table.print_table()

            self.display_table(reduced_table.get_table_as_list())
        except ValueError:
            messagebox.showerror('Error', 'Recheck the provided state table.')

    def display_table(self, data_array):
        table_window = tk.Toplevel(self, padx=10, pady=10)
        table_window.title('Reduced Table')

        inputs = self.get_input_count()
        outputs = inputs if self.get_circuit_type() == 'Mealy' else 1

        header_font = ('Arial', 14, 'bold')

        ps_label = tk.Label(table_window, text='P.S', borderwidth=1)
        ps_label.config(font=header_font)
        ps_label.grid(row=0, column=0, sticky='nsew', padx=1, pady=2)

        ns_label = tk.Label(table_window, text='N.S', borderwidth=1)
        ns_label.config(font=header_font)
        ns_label.grid(row=0, column=1, columnspan=inputs, sticky='nsew', padx=1, pady=2)

        op_label = tk.Label(table_window, text='Output', borderwidth=1)
        op_label.config(font=header_font)
        op_label.grid(row=0, column=inputs + 1, columnspan=outputs, sticky='nsew', padx=1, pady=2)

        if inputs != 1:
            for j in range(len(data_array[0]) + 1):
                if j == 0:
                    label_text = ''
                elif 0 < j <= inputs:
                    label_text = f'x = {j - 1}'
                elif outputs > 1:
                    label_text = f'x = {j - (inputs + 1)}'
                else:
                    continue

                field = tk.Label(table_window, text=label_text, borderwidth=1, width=5)
                field.config(font=('Arial', 12, 'italic'))
                field.grid(row=1, column=j, sticky='nsew', padx=1, pady=1)

        for i, row in enumerate(data_array):
            label_text = chr(ord('A') + i)

            field = tk.Label(table_window, text=label_text, borderwidth=1, width=5)
            field.grid(row=i + (2 if inputs != 1 else 1), column=0, sticky='nsew', padx=1, pady=1)

            for j, value in enumerate(row):
                if j < inputs:
                    label_text = chr(ord('A') + value)
                else:
                    label_text = str(value)

                field = tk.Label(table_window, text=label_text, borderwidth=1, width=5)
                field.grid(row=i + (2 if inputs != 1 else 1), column=j+1, sticky='nsew', padx=1, pady=1)

        # Adjust the size of the columns to fit the contents
        for j in range(len(data_array[0])):
            table_window.grid_columnconfigure(j)

        # Adjust the size of the rows to fit the contents
        for i in range(len(data_array)):
            table_window.grid_rowconfigure(i)

    def update_table(self):
        try:
            states_entry = self._states_count_entry.get()
            inputs_entry = self._inputs_count_entry.get()

            if states_entry == '' or inputs_entry == '' or not states_entry.isdigit() or not inputs_entry.isdigit():
                raise TypeError

            states = int(states_entry)
            inputs = int(inputs_entry)

            if states <= 0 or inputs <= 0:
                raise ValueError

            self._clear_table()
            self._build_table()

        except ValueError:
            messagebox.showerror('Error', 'Please provide positive integer values for the number of states and inputs.')

        except TypeError:
            messagebox.showerror('Error', 'Illegal format for number of states and inputs.')

    def _clear_table(self):
        for widgets in self._table_frame.winfo_children():
            widgets.destroy()
        self.table_entries.clear()

    def _build_table(self):
        states = self.get_states_count()
        inputs = self.get_input_count()
        outputs = inputs if self.get_circuit_type() == 'Mealy' else 1

        header_font = ('Arial', 14, 'bold')

        ps_label = tk.Label(self._table_frame, text='P.S', borderwidth=1)
        ps_label.config(font=header_font)
        ps_label.grid(row=0, column=0, sticky='nsew', padx=1, pady=2)

        ns_label = tk.Label(self._table_frame, text='N.S', borderwidth=1)
        ns_label.config(font=header_font)
        ns_label.grid(row=0, column=1, columnspan=inputs, sticky='nsew', padx=1, pady=2)

        op_label = tk.Label(self._table_frame, text='Output', borderwidth=1)
        op_label.config(font=header_font)
        op_label.grid(row=0, column=inputs + 1, columnspan=outputs, sticky='nsew', padx=1, pady=2)

        for i in range(states + 1):
            row_entries = []
            for j in range(inputs + outputs + 1):
                if inputs != 1 and i == 0:
                    if j == 0:
                        label_text = ''
                    elif 0 < j <= inputs:
                        label_text = f'x = {j - 1}'
                    elif outputs > 1:
                        label_text = f'x = {j - (inputs + 1)}'
                    else:
                        continue

                    label = tk.Label(self._table_frame, text=label_text, borderwidth=1, font=('Arial', 12, 'italic'))
                    label.grid(row=i + 1, column=j, sticky='nsew', padx=1, pady=1)
                else:
                    if j == 0:
                        field_text = chr(ord('a') + i - (1 if inputs != 1 else 0))
                        field = tk.Label(self._table_frame, text=field_text, borderwidth=1, width=5)
                    else:
                        field = tk.Entry(self._table_frame, borderwidth=1, width=5, validate='key')
                        row_entries.append(field)

                    field.grid(row=i + 1, column=j, sticky='nsew', padx=1, pady=1)

            if len(row_entries) != 0:
                self.table_entries.append(row_entries)


if __name__ == "__main__":
    app = ImplicationTableReducerGUI()
    app.mainloop()
