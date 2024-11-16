import json
from tkinter import *
from tkinter import messagebox, ttk
import mail
import mysql.connector
import data_management as dm
from tkcalendar import DateEntry 
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from tkinter import Tk, Toplevel, Label, StringVar, OptionMenu, IntVar, Spinbox, Entry, Button, BooleanVar, Checkbutton, messagebox
from datetime import datetime
from tkcalendar import DateEntry
import math

myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    password = os.getenv("SQL_pass"),
    database="Battery_Management"
)

def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit the application?"):
        exit()

glb_user_id, glb_family_name = None, None

func_object=dm.FUNCTIONALITY(myconn)

def add_device(root):
    global glb_family_name


    root.withdraw()
    # Create a new Toplevel window
    add_device_window = Toplevel(root)
    add_device_window.title('Battery Management System')
    add_device_window.configure(background='ghostwhite')
    add_device_window.resizable(False, False)
    add_device_window.protocol("WM_DELETE_WINDOW", on_close)
    # Title Label
    Label(
        add_device_window, text='Add Device', 
        bg='darkorange', font=("Century", 22, "bold"), 
        fg='white'
    ).grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

    # Device Name
    Label(
        add_device_window, text='Device Name', 
        bg='ghostwhite', font=('Century', 16), 
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    name_var = StringVar()
    name_entry = Entry(
        add_device_window, font=('Century', 12), 
        bg='white', fg='black', textvariable=name_var
    )
    name_entry.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    # Battery Size
    Label(
        add_device_window, text='Battery Size', 
        bg='ghostwhite', font=('Century', 16), 
    ).grid(row=3, column=0, sticky="w", padx=10, pady=10)

    battery_size_var = StringVar(value="Select")
    battery_sizes = ['AA', 'AAA', 'D2', 'CR2032', 'CR2025', 'CR2016', 'LR44', 'LR41', '9V', 'Other']
    battery_size_menu = OptionMenu(
        add_device_window, battery_size_var, *battery_sizes
    )
    battery_size_menu.config(font=('Century', 12), bg='white', fg='black', width=10)
    battery_size_menu.grid(row=4, column=0, sticky="w", padx=10, pady=5)

    # Device Type
    Label(
        add_device_window, text='Device Type', 
        bg='ghostwhite', font=('Century', 16), 
    ).grid(row=5, column=0, sticky="w", padx=10, pady=10)

    device_type_var = StringVar(value="Select")
    device_types = ['Remote', 'Camera', 'Toy', 'Flashlight', 'Car key', 'Game Controller', 'Watch/Clock', 'Mouse/CompPeripherals', 'Scale', 'Other']
    device_type_menu = OptionMenu(
        add_device_window, device_type_var, *device_types
    )
    device_type_menu.config(font=('Century', 12), bg='white', fg='black', width=10)
    device_type_menu.grid(row=6, column=0, sticky="w", padx=10, pady=5)

    # Brand
    Label(
        add_device_window, text='Brand', 
        bg='ghostwhite', font=('Century', 16), 
        
    ).grid(row=1, column=1, sticky="w", padx=10, pady=10)

    brand_var = StringVar()
    brand_entry = Entry(
        add_device_window, font=('Century', 12), 
        bg='white', fg='black', textvariable=brand_var
    )
    brand_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    # Number of Cells
    Label(
        add_device_window, text='Number of cells', 
        bg='ghostwhite', font=('Century', 16), 
        
    ).grid(row=3, column=1, sticky="w", padx=10, pady=10)

    num_cells_var = IntVar(value=1)
    num_cells_spinbox = Spinbox(
        add_device_window, from_=1, to=100, increment=1, 
        textvariable=num_cells_var, font=('Century', 12), 
        bg='white', fg='black', width=5
    )
    num_cells_spinbox.grid(row=4, column=1, sticky="w", padx=10, pady=5)

    # Weight Sensitive Checkbox
    Label(
        add_device_window, text='Weight Sensitive?', 
        bg='ghostwhite', font=('Century', 16), 
        
    ).grid(row=5, column=1, sticky="w", padx=10, pady=10)

    weight_sensitive_var = BooleanVar()
    weight_sensitive_checkbox = Checkbutton(
        add_device_window, text="Yes", variable=weight_sensitive_var, 
        bg='ghostwhite', fg='black', font=('Century', 12), 
        onvalue=True, offvalue=False
    )
    weight_sensitive_checkbox.grid(row=6, column=1, sticky="w", padx=10, pady=5)

    # Submit Button
    def submit():
        # Collecting the values
        name = name_var.get()
        battery_size = battery_size_var.get()
        device_type = device_type_var.get()
        brand = brand_var.get()
        num_cells = num_cells_var.get()
        weight_sensitive = weight_sensitive_var.get()

        # Storing the results in a list
        results = [name, battery_size, device_type, brand, num_cells, weight_sensitive]
        print("Submitted Data:", results)
        device_conn = dm.DEVICE_TABLE(myconn)

        try:
            messagebox.showinfo(title='Device Added', message=f'{results[0]} added successfully.')
            device_conn.INSERT_INTO_DEVICE_NEWDEVICE(
                glb_family_name, name, brand, device_type, num_cells, battery_size, weight_sensitive
            )
        except Exception as e:
            messagebox.showerror(title='Device Add Error', message='An error occurred while adding the device: ' + str(e))

        # Clear all inputs
        clear_inputs()

    # Clear all input fields
    def clear_inputs():
        name_var.set("")
        battery_size_var.set("Select")
        device_type_var.set("Select")
        brand_var.set("")
        num_cells_var.set(1)
        weight_sensitive_var.set(False)

    # Positioning the submit button
    submit_button = Button(
        add_device_window, text="Add Device", command=submit, 
    )
    submit_button.grid(row=7, column=1, columnspan=1, pady=20)

    def go_back():
        root.deiconify()
        add_device_window.destroy()

    back_button = Button(add_device_window, text="Back", command=go_back, font=('Century', 12))#, bg='red', fg='white')
    back_button.grid(row=7, column=0, columnspan=1, pady=10)

def add_purchase(root):
    global glb_family_name, glb_user_id

    root.withdraw()

    add_purchase_window = Toplevel(root)
    add_purchase_window.title('Battery Management System')
    add_purchase_window.configure(background='ghostwhite')
    add_purchase_window.resizable(True, True)
    add_purchase_window.protocol("WM_DELETE_WINDOW", on_close)
    # Main Title
    Label(
        add_purchase_window, text='Add Purchase', 
        bg='darkorange', font=("Century", 22, "bold"), 
        fg='white'
    ).grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

    # Brand Selection
    Label(
        add_purchase_window, text='Brand', 
        bg='ghostwhite', font=('Century', 16), 
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    brand_var = StringVar(value="Select")
    brands = ['Duracell Ultra', 'Duracell', 'Eveready', 'AmazonBasics', 'Panasonic', 'Energizer', 'Nippo', 'Sony', 'PowerCell', 'Godrej', 'Amaron', 'Other']
    brand_menu = OptionMenu(add_purchase_window, brand_var, *brands)
    brand_menu.config(font=('Century', 12), bg='white', fg='black', width=10)
    brand_menu.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    # Battery Size Selection
    Label(
        add_purchase_window, text='Battery Size', 
        bg='ghostwhite', font=('Century', 16), 
    ).grid(row=3, column=0, sticky="w", padx=10, pady=10)

    battery_size_var = StringVar(value="Select")
    battery_sizes = ['AA', 'AAA', 'D2', 'CR2032', 'CR2025', 'CR2016', 'LR44', 'LR41', '9V', 'Other']
    battery_size_menu = OptionMenu(add_purchase_window, battery_size_var, *battery_sizes)
    battery_size_menu.config(font=('Century', 12), bg='white', fg='black', width=10)
    battery_size_menu.grid(row=4, column=0, sticky="w", padx=10, pady=5)

    # Price Selection
    Label(
        add_purchase_window, text='Price', 
        bg='ghostwhite', font=('Century', 16), 
        
    ).grid(row=5, column=0, sticky="w", padx=10, pady=10)

    price_var = IntVar(value=100)
    price_spinbox = Spinbox(add_purchase_window, from_=1, to=2000, increment=1, textvariable=price_var, font=('Century', 12), bg='white', fg='black', width=5)
    price_spinbox.grid(row=6, column=0, sticky="w", padx=10, pady=5)

    # Store Entry
    Label(
        add_purchase_window, text='Store', 
        bg='ghostwhite', font=('Century', 16), 
        
    ).grid(row=1, column=1, sticky="w", padx=10, pady=10)

    store_var = StringVar()
    store_entry = Entry(add_purchase_window, font=('Century', 12), bg='white', fg='black', textvariable=store_var)
    store_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    # Number of Cells
    Label(
        add_purchase_window, text='Number of cells', 
        bg='ghostwhite', font=('Century', 16), 
        
    ).grid(row=3, column=1, sticky="w", padx=10, pady=10)

    num_cells_var = IntVar(value=1)
    num_cells_spinbox = Spinbox(add_purchase_window, from_=1, to=100, increment=1, textvariable=num_cells_var, font=('Century', 12), bg='white', fg='black', width=5)
    num_cells_spinbox.grid(row=4, column=1, sticky="w", padx=10, pady=5)

    # Purchase Date
    Label(
        add_purchase_window, text='Purchase Date', 
        bg='ghostwhite', font=('Century', 16), 
    ).grid(row=5, column=1, sticky="w", padx=10, pady=10)

    purchase_date_entry = DateEntry(add_purchase_window, font=('Century', 12), bg='white', fg='black', width=12, date_pattern='yyyy-mm-dd')
    purchase_date_entry.set_date(datetime.now())
    purchase_date_entry.grid(row=6, column=1, sticky="w", padx=10, pady=5)

    # Expiry Date
    Label(
        add_purchase_window, text='Exp Date', 
        bg='ghostwhite', font=('Century', 16), 
    ).grid(row=7, column=0, sticky="w", padx=10, pady=10)

    exp_date_entry = DateEntry(add_purchase_window, font=('Century', 12), bg='white', fg='black', width=12, date_pattern='yyyy-mm-dd')
    exp_date_entry.set_date(datetime.now() + relativedelta(years=10))
    exp_date_entry.grid(row=8, column=0, sticky="w", padx=10, pady=5)

    # Submit Button
    def submit():
        # Collect and process form data
        brand = brand_var.get()
        battery_size = battery_size_var.get()
        price = price_var.get()
        store = store_var.get()
        num_cells = num_cells_var.get()
        purchase_date = purchase_date_entry.get_date()
        exp_date = exp_date_entry.get_date()

        results = [brand, num_cells, battery_size, price, store, purchase_date, exp_date]
        print("Submitted Data:", results)
        try:
            device_conn = dm.PURCHASE_TABLE(myconn)
            device_conn.INSERT_INTO_PURCHASE_NEWPURCHASE(
                brand, num_cells, battery_size, price, store, purchase_date, exp_date, glb_family_name, glb_user_id
            )
            messagebox.showinfo(title='Purchase Added', message='Purchase added successfully.')
        except Exception as e:
            print("Error:", e)

        clear_inputs()

    def clear_inputs():
        brand_var.set("Select")
        battery_size_var.set("Select")
        num_cells_var.set(1)
        price_var.set(100)
        store_var.set("")
        purchase_date_entry.set_date(datetime.now())
        exp_date_entry.set_date(datetime.now() + relativedelta(years=10))

    submit_button = Button(add_purchase_window, text="Add Entry", command=submit, font=('Century', 12))#, bg='green', fg='white')
    submit_button.grid(row=9, column=1, columnspan=1, pady=20)

    # Back Button
    def go_back():
        root.deiconify()
        add_purchase_window.destroy()

    back_button = Button(add_purchase_window, text="Back", command=go_back, font=('Century', 12))#, bg='red', fg='white')
    back_button.grid(row=9, column=0, columnspan=1, pady=10)

def insert_battery(root):
    global glb_family_name, glb_user_id

    device_data =  func_object.SHOW_ALL_DEVICES(glb_family_name)
    if not device_data:
        root.deiconify()
        messagebox.showwarning("No Device Entry","No Entry(s) of the Devices found for the family.")
        return
    # Hide the main window
    root.withdraw()

    # Setup the Add Purchase Window
    insert_battery_window = Toplevel(root)
    insert_battery_window.title('Battery Management System')
    insert_battery_window.configure(background='ghostwhite')
    insert_battery_window.resizable(True, True)
    insert_battery_window.protocol("WM_DELETE_WINDOW", on_close)
    # Main Title
    Label(
        insert_battery_window, text='Insert Batteries', 
        bg='darkorange', font=("Century", 22, "bold"), 
        fg='white'
    ).grid(row=0, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

    # Device Selection Label
    Label(
        insert_battery_window, text='Device:', 
        bg='ghostwhite', font=('Century', 16), 
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    # Device Selection with dictionary for ID and name mapping
    device_var = StringVar(value="Select")
    device_dict = {device[0]: device[1] for device in device_data}
    device_names = list(device_dict.values())

    device_menu = OptionMenu(insert_battery_window, device_var, *device_names)
    device_menu.config(font=('Century', 12), bg='white', fg='black', width=10)
    device_menu.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    # Battery Size and Number of Cells Labels
    battery_size_label = Label(
        insert_battery_window, text='Battery Size:', 
        bg='ghostwhite', font=('Century', 16)
    )
    battery_size_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    no_of_cells_label = Label(
        insert_battery_window, text='Number of cells:', 
        bg='ghostwhite', font=('Century', 16)
    )
    no_of_cells_label.grid(row=2, column=1, sticky="w", padx=10, pady=10)

    selected_device_id = None
    enough_batteries = False
    # Update labels based on selected device
    def update_battery_info(*args):
        nonlocal selected_device_id, enough_batteries
        selected_device_name = device_var.get()
        # print("Selected Device: >>>> ", selected_device_name.strip())
        if selected_device_name != "Select":
            # print(selected_device_name)
            for id, name in device_dict.items():
                if name == selected_device_name:
                    selected_device_id = id
                    break

            # print("Device ID: ",selected_device_id)

            if selected_device_id:
                results, battery_size, no_of_cells = func_object.SUGGEST_BATTERY(glb_family_name, selected_device_id)
                enough_batteries = results
                # Update the labels with battery details
                battery_size_label.config(text=f'Battery Size: {battery_size}')
                no_of_cells_label.config(text=f'Number of cells: {no_of_cells}')
        else:
            # Reset labels if "Select" is chosen
            battery_size_label.config(text='Battery Size:')
            no_of_cells_label.config(text='Number of cells:')

    # Bind device selection to update_battery_info
    device_var.trace('w', update_battery_info)

    # Initial label update
    update_battery_info()

    def submit(device_id, enough_batteries):
        family_name = glb_family_name
        BATTERY_SIZE = battery_size_label.cget('text').split(':')[-1].strip()
        no_of_cells = int(no_of_cells_label.cget('text').split(':')[-1].strip())

        if enough_batteries:
            ans = messagebox.askyesno(title='Insert Batteries', message='Are you sure you want to insert batteries?')
            try:
                if ans:
                    func_object.INSERT_BATTERY(family_name, BATTERY_SIZE, no_of_cells,device_id)
                    messagebox.showinfo(title='Battery Inserted', message='Batteries inserted successfully.')
            except Exception as e:
                messagebox.showerror(title='Battery Insert Error', message='An error occurred while inserting the battery: ' + str(e))
        else:

            ans = messagebox.askyesno(title='Battery Insert Error', message='Not enough batteries available.\nDo you want to purchase batteries?')
            if ans:
                print("Purchase Batteries")
                data=func_object.SUGGEST_PURCHASE(BATTERY_SIZE, device_id)
                if data:
                    buy_pack(insert_battery_window,data,no_of_cells,device_id)
                else:
                    data2=func_object.SUGGEST_PURCHASE_PRICE_ONLY(BATTERY_SIZE)
                    buy_pack2(insert_battery_window,data2,no_of_cells,device_id)
                    


    submit_button = Button(insert_battery_window, text="Insert Battery", command= lambda : submit(selected_device_id,enough_batteries), font=('Century', 12))#, bg='green', fg='white')
    submit_button.grid(row=9, column=1, columnspan=1, pady=20)

    def go_back():
        root.deiconify()
        insert_battery_window.destroy()

    back_button = Button(insert_battery_window, text="Back", command=go_back, font=('Century', 12))#, bg='red', fg='white')
    back_button.grid(row=9, column=0, columnspan=1, pady=10)

def buy_pack(insert_battery_window,data,no_of_cells,device_id):
    insert_battery_window.withdraw()
    buy_pack_window = Toplevel(insert_battery_window)
    buy_pack_window.title('Battery Management System')
    buy_pack_window.configure(background='ghostwhite')
    buy_pack_window.resizable(True, True)
    buy_pack_window.protocol("WM_DELETE_WINDOW", on_close)
    Label(
        buy_pack_window, text='Select Pack to Purchase:', 
            bg='darkorange', font=("Century", 22, "bold"), 
            fg='white'
        ).grid(row=0, column=0, columnspan=9, pady=20, padx=10, sticky="ew")

    headers = ["Battery Size", "Brand", "Store", "Price per cell", "Total Price", "Number of Cells", "Avg days lasting", "Price per day ratio"]
    for col, header in enumerate(headers):
        Label(buy_pack_window, text=header, font=('Century', 16, 'bold'), bg='ghostwhite').grid(row=1, column=col+1, padx=5, pady=5)

    selected_entry = IntVar()
    selected_entry.set(None)

    for index, entry in enumerate(data):
        Radiobutton(buy_pack_window, variable=selected_entry, value=index, bg='ghostwhite').grid(row=index+2, column=0)
        battery_size, brand, store,pack_id, price_per_cell, total_price, avg_days_lasting, price_per_day_ratio = entry
        number_of_cells = total_price // price_per_cell 
        display_values = [battery_size, brand, store, price_per_cell, total_price, number_of_cells, avg_days_lasting, price_per_day_ratio]
        for col, value in enumerate(display_values):
            Label(buy_pack_window, text=str(value), bg='ghostwhite').grid(row=index+2, column=col+1, padx=5, pady=5)

    
    def go_back():
        insert_battery_window.deiconify()
        buy_pack_window.destroy()

    def submit_buy():

        selected_index = selected_entry.get()
        if selected_index is not None:
            pack_id = data[selected_index][3]
            store_name = data[selected_index][2]
            price = data[selected_index][5]
            quan=math.ceil(no_of_cells/(data[selected_index][5]/data[selected_index][4]))
            try:
                for _ in range(quan):
                    func_object.INSERT_PURCHASE(pack_id,store_name,glb_family_name,glb_user_id,price)
                func_object.INSERT_BATTERY(glb_family_name, data[selected_index][0], no_of_cells,device_id)
                messagebox.showinfo(title='Purchase Successful', message=f'{quan} pack{" " if quan == 1 else "s"} purchased and inserted into device.')

                buy_pack_window.destroy()
                root.deiconify()
            except Exception as e:
                messagebox.showerror(title='Purchase Error', message='An error occurred while purchasing and inserting the pack: ' + str(e))
        else:
            messagebox.showerror(title='No Pack Selected', message='Please select a pack to purchase.')
    back_button = Button(buy_pack_window, text="Back", command=go_back, font=('Century', 12))#, bg='red', fg='white')
    back_button.grid(row=len(data)+2, column=1, columnspan=4, pady=10)

    submit_button = Button(buy_pack_window,text="Buy and insert", command=submit_buy, font=('Century', 12))#, bg='red', fg='white')
    submit_button.grid(row=len(data)+2, column=5, columnspan=4, pady=10)
        
def buy_pack2(insert_battery_window,data,no_of_cells,device_id):
    insert_battery_window.withdraw()
    buy_pack2_window = Toplevel(insert_battery_window)
    buy_pack2_window.title('Battery Management System')
    buy_pack2_window.configure(background='ghostwhite')
    buy_pack2_window.resizable(True, True)
    buy_pack2_window.protocol("WM_DELETE_WINDOW", on_close)
    Label(
        buy_pack2_window, text='Select Pack to Purchase:', 
            bg='darkorange', font=("Century", 22, "bold"), 
            fg='white'
        ).grid(row=0, column=0, columnspan=9, pady=20, padx=10, sticky="ew")

    headers = ["Store", "Brand", "Battery Size", "Number of Cells", "Latest Purchase Date", "Total Price", "Price per Cell"]

    for col, header in enumerate(headers):
        Label(buy_pack2_window, text=header, font=('Century', 16, 'bold'), bg='ghostwhite').grid(row=1, column=col + 1, padx=5, pady=5)
    selected_entry = IntVar()
    selected_entry.set(None)

    for index, entry in enumerate(data):
        store_name, brand, battery_size, latest_purchase_date, total_price, price_per_cell = entry[1:]
        num_of_cells = total_price // price_per_cell
        Radiobutton(buy_pack2_window, variable=selected_entry, value=index, bg='ghostwhite').grid(row=index + 2, column=0)
        values_to_display = [store_name, brand, battery_size, num_of_cells, latest_purchase_date, total_price, price_per_cell]
        for col, value in enumerate(values_to_display):
            Label(buy_pack2_window, text=str(value), bg='ghostwhite').grid(row=index + 2, column=col + 1, padx=5, pady=5)

    
    def go_back():
        insert_battery_window.deiconify()
        buy_pack2_window.destroy()

    def submit_buy():

        selected_index = selected_entry.get()
        if selected_index is not None:
            pack_id = data[selected_index][0]
            store_name = data[selected_index][1]
            price = data[selected_index][5]
            quan=math.ceil(no_of_cells/(data[selected_index][5]/data[selected_index][6]))
            try:
                for _ in range(quan):
                    func_object.INSERT_PURCHASE(pack_id,store_name,glb_family_name,glb_user_id,price)
                func_object.INSERT_BATTERY(glb_family_name, data[selected_index][3], no_of_cells,device_id)
                messagebox.showinfo(title='Purchase Successful', message=f'{quan} pack{" " if quan == 1 else "s"} purchased and inserted into device.')
                buy_pack2_window.destroy()
                root.deiconify()
            except Exception as e:
                messagebox.showerror(title='Purchase Error', message='An error occurred while purchasing and inserting the pack: ' + str(e))
        else:
            messagebox.showerror(title='No Pack Selected', message='Please select a pack to purchase.')
    back_button = Button(buy_pack2_window, text="Back", command=go_back, font=('Century', 12))#, bg='red', fg='white')
    back_button.grid(row=len(data)+2, column=1, columnspan=4, pady=10)

    submit_button = Button(buy_pack2_window,text="Buy and insert", command=submit_buy, font=('Century', 12))#, bg='red', fg='white')
    submit_button.grid(row=len(data)+2, column=5, columnspan=4, pady=10)

def show_device(root):
    global glb_family_name
    root.withdraw()

    def go_back():
        root.deiconify()
        try:
            show_device_window.destroy()
        except Exception:
            pass

    data=func_object.SELECT_ALL_DEVICES(glb_family_name)
    if not data:
        messagebox.showwarning("No Device Entry","No Entry(s) of the devices found in the family.")
        go_back()
        return

    show_device_window = Toplevel(root)
    show_device_window.title('Battery Management System')
    show_device_window.configure(background='ghostwhite')
    show_device_window.resizable(False, False)
    show_device_window.protocol("WM_DELETE_WINDOW", on_close)
    Label(
        show_device_window, text=f'Devices in {glb_family_name} Family', 
            bg='darkorange', font=("Century", 22, "bold"), 
            fg='white'
        ).grid(row=0, column=0, columnspan=9, pady=20, padx=10, sticky="ew")
    
    headers = ['Device ID','Name','Brand','Type','Number of cells','Battery size','Weight sensitive']
    for col, header in enumerate(headers):
        Label(show_device_window, text=header, font=('Century', 16, 'bold'),bg='ghostwhite').grid(row=1, column=col, padx=5, pady=5)
    for index, entry in enumerate(data):
        for col, value in enumerate(entry):
            Label(show_device_window, text=str(value),bg='ghostwhite').grid(row=index+1+1, column=col, padx=5, pady=5)

    
    back_button = Button(show_device_window, text="Back", command=go_back, font=('Century', 12))#, bg='red', fg='white')
    back_button.grid(row=len(data)+2, column=0, columnspan=9, pady=10)

def show_batteries(root):
    global glb_family_name
    root.withdraw()
    def go_back():
        root.deiconify()
        try:
            show_battery_window.destroy()
        except Exception:
            pass

    data=func_object.SELECT_ALL_BATTERIES(glb_family_name)
    
    if not data:
        messagebox.showinfo('Error', 'No batteries available in this family')
        go_back()
        return
    
    show_battery_window = Toplevel(root)
    show_battery_window.title('Battery Management System')
    show_battery_window.configure(background='ghostwhite')
    show_battery_window.resizable(False, False)
    show_battery_window.protocol("WM_DELETE_WINDOW", on_close)


    Label(
        show_battery_window, text=f'Batteries available in {glb_family_name} Family', 
            bg='darkorange', font=("Century", 22, "bold"), 
            fg='white'
        ).grid(row=0, column=0, columnspan=9, pady=20, padx=10, sticky="ew")

    headers = ['Brand','Battery size','Number of cells available']
    for col, header in enumerate(headers):
        Label(show_battery_window, text=header, font=('Century', 16, 'bold'),bg='ghostwhite').grid(row=1, column=col, padx=5, pady=5)
    for index, entry in enumerate(data):
        for col, value in enumerate(entry):
            Label(show_battery_window, text=str(value),bg='ghostwhite').grid(row=index+1+1, column=col, padx=5, pady=5)

    back_button = Button(show_battery_window, text="Back", command=go_back, font=('Century', 12))#, bg='red', fg='white')
    back_button.grid(row=len(data)+2, column=0, columnspan=3, pady=10)

def dispose_batteries(root):
    global glb_family_name
    root.withdraw()
    def go_back():
        root.deiconify()
        try:
            dispose_battery_window.destroy()
        except Exception:
            pass

    data=func_object.SELECT_TODISPOSE_BATTERIES(glb_family_name)
    
    if not data:
        messagebox.showinfo('Error', 'No batteries to dispose in this family')
        go_back()
        return
    
    dispose_battery_window = Toplevel(root)
    dispose_battery_window.title('Battery Management System')
    dispose_battery_window.configure(background='ghostwhite')
    dispose_battery_window.resizable(False, False)
    dispose_battery_window.protocol("WM_DELETE_WINDOW", on_close)


    Label(
        dispose_battery_window, text=f'Batteries to dispose in {glb_family_name} Family', 
            bg='darkorange', font=("Century", 22, "bold"), 
            fg='white'
        ).grid(row=0, column=0, columnspan=3, pady=20, padx=10, sticky="ew")

    headers = ['Battery size','Number of cells']
    for col, header in enumerate(headers):
        Label(dispose_battery_window, text=header, font=('Century', 16, 'bold'),bg='ghostwhite').grid(row=1, column=col+1, padx=5, pady=5)
        checkbox_vars = []
    for index, entry in enumerate(data):
        checkbox_var = BooleanVar()
        checkbox_vars.append(checkbox_var)
        Checkbutton(dispose_battery_window, variable=checkbox_var, bg='ghostwhite').grid(row=index+2, column=0, padx=0, pady=5)
        for col, value in enumerate(entry):
            Label(dispose_battery_window, text=str(value),bg='ghostwhite').grid(row=index+1+1, column=col+1, padx=5, pady=5)

    def submit_dispose():
        ans = messagebox.askyesno(title='Dispose Batteries', message='Are you sure you want to dispose the selected batteries?')
        if ans:
            for index, checkbox_var in enumerate(checkbox_vars):
                if checkbox_var.get():
                    battery_size = data[index][0]
                    num_of_cells = data[index][1]
                    try:
                        func_object.DISPOSE_BATTERY(glb_family_name, battery_size)
                        print("Disposed",num_of_cells,battery_size,'batteries')
                        messagebox.showinfo(title='Battery Dispose', message='Batteries disposed successfully.')
                    except Exception as e:
                        messagebox.showerror(title='Battery Dispose Error', message='An error occurred while disposing the battery: ' + str(e))
            dispose_battery_window.destroy()
            root.deiconify()

    back_button = Button(dispose_battery_window, text="Back", command=go_back, font=('Century', 12))#, bg='red', fg='white')
    back_button.grid(row=len(data)+2, column=1, columnspan=1, pady=10)

    submit_button = Button(dispose_battery_window,text="Dispose", command=submit_dispose, font=('Century', 12))#, bg='red', fg='white')
    submit_button.grid(row=len(data)+2, column=2, columnspan=1, pady=10)

def logout(current_window):
    global main_screen, glb_user_id, glb_family_name
    ans = messagebox.askyesno(title='Log out?', message='Are you Sure to Log Out?')
    if not ans:
        return
    
    glb_user_id = None
    glb_family_name = None
    main_screen.deiconify()
    current_window.destroy()
        
def old_User_start():
    global root, name, pass_word, glb_user_id, glb_family_name

    user_name = str(name.get())
    password = str(pass_word.get())
    user_info = dm.USER_TABLE(myconn).SELECT_FROM_USER(user_name)

    if user_info:
        print(type(user_info))
        print(user_info)
        if user_info[-1] == password:
            print("User Found.")
            glb_user_id = user_info[0]
            glb_family_name = user_info[1]
            login_screen.withdraw()
            root = Toplevel(main_screen)
            root.title('Battery Management System')
            root.config(bg='ghostwhite')
            root.protocol("WM_DELETE_WINDOW", on_close)

            # Create a frame that spans the width of the window
            header_frame = Frame(root, bg="darkorange", width=400, height=50)
            header_frame.grid(row=0, column=0, columnspan=10, sticky="ew")  # Spans entire row
            header_frame.grid_propagate(False)  # Prevent frame from resizing to its contents

            # Add the welcome label to the frame
            Label(header_frame, text='Welcome, ' + user_name + ' !', font=("Century", 22, "bold"), fg='white',bg="darkorange").pack(pady=10, expand=True)

            # Define button style
            button_style = {
                "bg": "white",
                "relief": "groove",
                "cursor": "hand2",
                "borderwidth": 1,
                "font": "Century 15",
                "width": 18
            }

            # Arrange buttons in a 2-column grid
            Button(root, text="Add Device", command=lambda: add_device(root), **button_style).grid(row=1, column=0, padx=5, pady=5)
            Button(root, text="Add Battery Purchase", command=lambda: add_purchase(root), **button_style).grid(row=1, column=1, padx=5, pady=5)
            Button(root, text="Insert Battery", command=lambda: insert_battery(root), **button_style).grid(row=2, column=0, padx=5, pady=5)
            Button(root, text="View Devices", command=lambda: show_device(root), **button_style).grid(row=2, column=1, padx=5, pady=5)
            Button(root, text="View Batteries", command=lambda: show_batteries(root), **button_style).grid(row=3, column=0, padx=5, pady=5)
            Button(root, text="Dispose Batteries", command=lambda: dispose_batteries(root), **button_style).grid(row=3, column=1, padx=5, pady=5)
            Button(root, text="Log out", command=lambda: logout(root), **button_style).grid(row=4, column=0, padx=5, pady=5)
            Button(root, text="Quit", command=on_close, **button_style).grid(row=4, column=1, padx=5, pady=5)

            root.resizable(0, 0)  # Disable resizing
            root.mainloop()
        else:
            print("User not found.")
            messagebox.showerror(title='Incorrect Details',
                                 message='Incorrect Username or Password')

def login():
    global name, login_screen, type_game, pass_word

    # Initialize the login screen
    login_screen = Toplevel(main_screen)
    main_screen.withdraw()
    login_screen.title("Login - Existing User")
    login_screen.protocol("WM_DELETE_WINDOW", on_close)
    # login_screen.geometry("400x250")
    login_screen.resizable(0, 0)
    login_screen.config(bg='ghostwhite')

    # Header frame with consistent color
    header_frame = Frame(login_screen, bg="darkorange", width=400, height=50)
    header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
    header_frame.grid_propagate(False)
    
    # Header Label
    Label(header_frame, text="Login", font=("Century", 22, "bold"), bg="darkorange", fg="white").pack(pady=10)

    # Define consistent font and styles
    font_style = ("Century", 13)
    label_style = {"font": font_style, "bg": "ghostwhite"}
    entry_style = {"font": font_style, "width": 20}
    button_style = {
        "bg": "white",
        "relief": "groove",
        "cursor": "hand2",
        "borderwidth": 1,
        "font": font_style,
        "width": 12,
        "pady": 5
    }

    # Input fields with labels
    Label(login_screen, text="Username:", **label_style).grid(row=1, column=0, sticky=W, padx=10, pady=10)
    name = ttk.Entry(login_screen, **entry_style)
    name.grid(row=1, column=1, padx=10)

    Label(login_screen, text="Password:", **label_style).grid(row=2, column=0, sticky=W, padx=10, pady=10)
    pass_word = ttk.Entry(login_screen, **entry_style, show="*")
    pass_word.grid(row=2, column=1, padx=10)

    # Buttons with consistent styling
    play_btn = Button(login_screen, text="Log In", command=old_User_start, **button_style)
    play_btn.grid(row=5, column=1, sticky=E, padx=10, pady=15)

    back_btn = Button(login_screen, text="Back", command=lambda: (main_screen.deiconify(), login_screen.destroy()), **button_style)
    back_btn.grid(row=5, column=0, sticky=W, padx=10, pady=15)

    # Key bindings for keyboard shortcuts
    login_screen.bind('<Return>', lambda _: old_User_start())
    login_screen.bind('<Escape>', lambda _: (main_screen.deiconify(), login_screen.destroy()))

    login_screen.mainloop()

def new_User_add():
    global glb_family_name, glb_user_id, root

    # Retrieve inputs
    new_user = name.get().strip()
    new_pass = pass_word_new.get().strip()
    usr_mail = usr_mail_id.get().strip()
    new_family_name = family_name.get().strip()

    # Check if all fields are filled
    if not new_user or not new_pass or not usr_mail or not new_family_name:
        messagebox.showerror(title='Input Error', message='All fields are required.')
        return

    # Insert family name
    try:
        family_conn = dm.FAMILY_TABLE(myconn)
        family_conn.INSERT_INTO_FAMILY_NEWFAMILY(new_family_name)
    except Exception as e:
        pass

    try:
        # Check if user exists
        user_conn = dm.USER_TABLE(myconn)
        user_exists = user_conn.SELECT_FROM_USER(new_user)

        if user_exists:
            messagebox.showerror(title='User Already Exists', message='The user already exists. Please choose a different username.')
            return

        # Insert new user
        glb_family_name = new_family_name
        glb_user_id = user_conn.INSERT_INTO_USER_NEWUSER(new_family_name, new_user, new_pass, usr_mail)

        # Close registration screen and open menu page
        register_screen.destroy()
        root = Toplevel(main_screen)
        root.title('Battery Management System')
        root.config(bg='ghostwhite')
        root.protocol("WM_DELETE_WINDOW", on_close)

        # Create a frame that spans the width of the window
        header_frame = Frame(root, bg="darkorange", width=400, height=50)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")  # Spans entire row
        header_frame.grid_propagate(False)  # Prevent frame from resizing to its contents

        # Add the welcome label to the frame
        Label(header_frame, text='Welcome, ' + new_user + ' !', font=("Century", 22, "bold"),fg='white',bg="darkorange").pack(pady=10, expand=True)

        # Define button style
        button_style = {
            "bg": "white",
            "relief": "groove",
            "cursor": "hand2",
            "borderwidth": 1,
            "font": "Century 15",
            "width": 18
        }

        # Arrange buttons in a 2-column grid
        Button(root, text="Add Device", command=lambda: add_device(root), **button_style).grid(row=1, column=0, padx=5, pady=5)
        Button(root, text="Add Battery Purchase", command=lambda: add_purchase(root), **button_style).grid(row=1, column=1, padx=5, pady=5)
        Button(root, text="Insert Battery", command=lambda: insert_battery(root), **button_style).grid(row=2, column=0, padx=5, pady=5)
        Button(root, text="View Devices", command=lambda: show_device(root), **button_style).grid(row=2, column=1, padx=5, pady=5)
        Button(root, text="View Batteries", command=lambda: show_batteries(root), **button_style).grid(row=3, column=0, padx=5, pady=5)
        Button(root, text="Dispose Batteries", command=lambda: dispose_batteries(root), **button_style).grid(row=3, column=1, padx=5, pady=5)
        Button(root, text="Log out", command=lambda: logout(root), **button_style).grid(row=4, column=0, padx=5, pady=5)
        Button(root, text="Quit", command=on_close, **button_style).grid(row=4, column=1, padx=5, pady=5)

        root.resizable(0, 0)  # Disable resizing
        root.mainloop()

    except Exception as e:
        messagebox.showerror(title='User Registration Error', message='An error occurred while registering the user: ' + str(e))

def register():
    global name, user_name, current_all_name, register_screen, type_game, pass_word_new, usr_mail_id, family_name

    # Initialize the register screen
    register_screen = Tk()
    main_screen.withdraw()
    register_screen.config(bg='ghostwhite')
    register_screen.title("New User")
    # register_screen.geometry("400x300")
    register_screen.resizable(0, 0)
    register_screen.protocol("WM_DELETE_WINDOW", on_close)

    # Header frame with consistent background color
    header_frame = Frame(register_screen, bg="darkorange", width=400, height=50)
    header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
    header_frame.grid_propagate(False)
    
    # Header Label
    Label(header_frame, text="Create a New Account", font=("Century", 22, "bold"), bg="darkorange", fg="white").pack(pady=10)

    # Define consistent font for labels, entries, and buttons
    font_style = ("Century", 13)
    label_style = {"font": font_style, "bg": "ghostwhite"}
    entry_style = {"font": font_style, "width": 20}
    button_style = {
        "bg": "white",
        "relief": "groove",
        "cursor": "hand2",
        "borderwidth": 1,
        "font": font_style,
        "width": 12,
        "pady": 5
    }

    # Input fields with labels
    Label(register_screen, text="Username:", **label_style).grid(row=1, column=0, sticky=W, padx=10, pady=5)
    name = ttk.Entry(register_screen, **entry_style)
    name.grid(row=1, column=1, padx=10)

    Label(register_screen, text="Password:", **label_style).grid(row=2, column=0, sticky=W, padx=10, pady=5)
    pass_word_new = ttk.Entry(register_screen, **entry_style, show="*")
    pass_word_new.grid(row=2, column=1, padx=10)

    Label(register_screen, text="Email:", **label_style).grid(row=3, column=0, sticky=W, padx=10, pady=5)
    usr_mail_id = ttk.Entry(register_screen, **entry_style)
    usr_mail_id.grid(row=3, column=1, padx=10)

    Label(register_screen, text="Family Name:", **label_style).grid(row=4, column=0, sticky=W, padx=10, pady=5)
    family_name = ttk.Entry(register_screen, **entry_style)
    family_name.grid(row=4, column=1, padx=10)

    # Buttons with updated font style
    ttk.Button(register_screen, text="Sign Up", command=new_User_add, style="TButton").grid(row=6, column=1, padx=10, pady=10, sticky=E)
    ttk.Button(register_screen, text="Back", command=lambda: (main_screen.deiconify(), register_screen.destroy()), style="TButton").grid(row=6, column=0, padx=10, pady=10, sticky=W)

    # Key bindings for keyboard shortcuts
    register_screen.bind('<Return>', lambda _: new_User_add())
    register_screen.bind('<Escape>', lambda _: (main_screen.deiconify(), register_screen.destroy()))
    
    register_screen.mainloop()

def main_screen_fn():
    global main_screen, value_1
    main_screen = Tk()

    # Configure main screen properties
    # main_screen.geometry("400x300")
    main_screen.resizable(0, 0)
    main_screen.title("Welcome to the Battery Management System!")
    main_screen.config(bg='ghostwhite')
    main_screen.protocol("WM_DELETE_WINDOW", on_close)
    value_1 = IntVar(main_screen)

    # Header with a consistent color and font style
    header_frame = Frame(main_screen, bg="darkorange", width=400, height=60)
    header_frame.pack(fill="x")
    header_label = Label(header_frame, text="Battery Management System", font=("Century", 20, "bold"), 
                         bg="darkorange", fg="white")
    header_label.pack(pady=10)

    # Adding empty space between header and buttons
    Label(main_screen, bg='ghostwhite').pack(pady=10)

    # Define consistent button style
    button_style = {
        "height": 2,
        "width": 25,
        "bg": "white",
        "relief": "groove",
        "cursor": "hand2",
        "borderwidth": 1,
        "font": ("Century", 14)
    }

    b1 = Button(main_screen, text="Existing User", command=login, **button_style)
    b1.pack(pady=10)
    b1.bind('<Enter>', lambda _: b1.config(bg='yellowgreen'))
    b1.bind('<Leave>', lambda _: b1.config(bg='white'))

    b2 = Button(main_screen, text="New User", command=register, **button_style)
    b2.pack(pady=10)
    b2.bind('<Enter>', lambda _: b2.config(bg='yellowgreen'))
    b2.bind('<Leave>', lambda _: b2.config(bg='white'))

    main_screen.mainloop()

main_screen_fn()
