import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from services.transaction_service import (
    add_transaction,
    get_transaction_types,
    get_transaction_types_category
)

def open_income_window(parent):
    window = tk.Toplevel(parent)

    window.title("Add Income")
    window.geometry("400x300")
    types = get_transaction_types()
    categoryTypes = get_transaction_types_category()

    print(types)
    print(categoryTypes)
    
    date_lable = tk.Label(
        window , 
        text="Transaction Date"
    )
    date_lable.pack()
    date_entry  = DateEntry(
        window ,
        width = 20,
        date_pattern ="yyyy-mm-dd"
    )
    date_entry.pack()
    category_lable = tk.Label(
        window ,
        text="category"
    )
    category_lable.pack()
    
    category_cambobox = ttk.Combobox(
        window,
        values=[name for id , name in categoryTypes],
        state="readonly"
    )
    category_cambobox.pack()
    type_label = tk.Label(
        window,
        text="Type"
    )
    type_label.pack()

    type_combobox = ttk.Combobox(
        window,
        values=[name for id, name in types],
        state="readonly"
    )
    type_combobox.pack()
    
    def save_income():
        amount = amount_entry.get()
        description = description_entry.get()

        selected_type = type_combobox.get()
        
        selectedCategory = category_cambobox.get()
        transaction_date = date_entry.get_date()

        type_id = None
        typecategory = None

        for id, name in types:
            if name == selected_type:
                type_id = id
                break
        for id , name in categoryTypes : 
            if name == selectedCategory:
                typecategory = id
                break    

        print(selected_type)
        print(type_id)

        add_transaction(
            amount,
            type_id,
            typecategory,
            description,
            transaction_date
        )   

    window = tk.Toplevel(parent)
        

    window.title("Add Income")
    window.geometry("400x300")

    amount_label = tk.Label(window, text="Amount")
    amount_label.pack()

    amount_entry = tk.Entry(window)
    amount_entry.pack()

    description_label = tk.Label(window, text="Description")
    description_label.pack()

    description_entry = tk.Entry(window)
    description_entry.pack()

    save_button = tk.Button(
        window,
        text="Save",
        command=save_income
    )


    save_button.pack(pady=20)