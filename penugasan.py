import tkinter as tk
from tkinter import ttk

# Initialize an empty list to store inventory items
inventory_list = []

# Initialize "tree" and "inventory_window" variable as none (no value assigned yet)
tree = None
inventory_window = None

# function for submit inventory
def submit_inventory():
    item = {
        "tanggal_inventaris": tanggal_inventaris.get(),
        "kode_barang": kode_barang.get(),
        "nama_barang": nama_barang.get(),
        "kuantitas": kuantitas.get(),
        "tanggal_beli": tanggal_beli.get(),
        "kondisi_barang": kondisi_barang.get()
    }
    inventory_list.append(item)
    clear_inventory_fields()

# function for inventory list
def check_inventory():
    global inventory_window
    global tree

    if inventory_window is None or not inventory_window.winfo_exists():
        inventory_window = tk.Toplevel(window)
        inventory_window.title("Inventory List")
        inventory_window.geometry("1200x400")

        refresh_button = ttk.Button(
            inventory_window, text="Refresh", command=refresh_inventory
        )
        refresh_button.pack()

        tree = ttk.Treeview(inventory_window, show="headings")

        columns = (
            "No", "Tanggal Inventaris", "Kode Barang", "Nama Barang", "Kuantitas",
            "Tanggal Beli", "Kondisi Barang"
        )

        tree["columns"] = columns

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        for idx, item in enumerate(inventory_list, start=1):
            values = (
                idx, item["tanggal_inventaris"], item["kode_barang"],
                item["nama_barang"], item["kuantitas"],
                item["tanggal_beli"], item["kondisi_barang"]
            )
            tree.insert("", "end", values=values)

        tree.column("No", width=30)

        tree.pack(fill="both", expand=True)
    else:
        inventory_window.lift()

# fuction for refresh inventory
def refresh_inventory():
    global tree

    for item in tree.get_children():
        tree.delete(item)

    for idx, item in enumerate(inventory_list, start=1):
        values = (
            idx, item["tanggal_inventaris"], item["kode_barang"],
            item["nama_barang"], item["kuantitas"],
            item["tanggal_beli"], item["kondisi_barang"]
        )
        tree.insert("", "end", values=values)

# function for clear inventory 
def clear_inventory_fields():
    tanggal_inventaris.set("")
    kode_barang.set("")
    nama_barang.set("")
    kuantitas.set("")
    tanggal_beli.set("")
    kondisi_barang.set("")

# function for login 
def login():
    if username.get() == "admin" and password.get() == "admin":
        frame1.pack_forget()
        create_frame2()

# function for quit window
def quit_window():
    window.destroy()

# function for frame 1
def create_frame1():
    global frame1

    frame1 = ttk.Frame(window)
    frame1.pack(padx=50, pady=0, fill="both", expand=True)

    ttk.Label(frame1, text="Inventaris Barang", font=(0, 30)).pack(
        padx=(90, 0), pady=(40, 40), fill="both")

    ttk.Label(frame1, text="Admin Login", font=(0, 20)).pack(
        padx=(145, 0), pady=(0, 15), fill="x")

    ttk.Label(frame1, text="Username").pack(
        padx=80, pady=(0, 5), fill="x")
    ttk.Entry(frame1, textvariable=username).pack(
        padx=80, pady=(0, 0), fill="both")
    ttk.Label(frame1, text="Password").pack(
        padx=80, pady=(0, 5), fill="x")
    ttk.Entry(frame1, textvariable=password,
              show='*').pack(padx=80, pady=(0, 0), fill="both")

    ttk.Button(frame1, text="Login", command=login).pack(pady=(20, 0))
    ttk.Button(frame1, text="Quit", command=quit_window).pack()

    ttk.Label(frame1, text="Hint = Username -> admin, password -> admin").pack(
        padx=(55, 0), pady=(25, 0), fill="x", expand=True)

# function for frame 2
def create_frame2():
    global frame2
    window.geometry("300x500")
    frame2 = ttk.Frame(window)
    frame2.pack(padx=50, pady=0, fill="both", expand=True)

    ttk.Label(frame2, text="Inventaris Barang", font=(0, 20)).pack(
        padx=(25, 0), pady=(30, 30),  anchor="w")
    ttk.Label(frame2, text="Tanggal Inventaris").pack(
        padx=0, pady=0, fill="x")
    ttk.Entry(frame2, textvariable=tanggal_inventaris).pack(
        padx=0, pady=0, fill="x")
    ttk.Label(frame2, text="Kode Barang").pack(
        padx=0, pady=0, fill="x")
    ttk.Entry(frame2, textvariable=kode_barang).pack(
        padx=0, pady=0, fill="x")
    ttk.Label(frame2, text="Nama Barang").pack(
        padx=0, pady=0, fill="x")
    ttk.Entry(frame2, textvariable=nama_barang).pack(
        padx=0, pady=0, fill="x")
    ttk.Label(frame2, text="Kuantitas Barang").pack(
        padx=0, pady=0, fill="x")
    ttk.Entry(frame2, textvariable=kuantitas).pack(
        padx=0, pady=0, fill="x")
    ttk.Label(frame2, text="Tanggal Pembelian").pack(
        padx=0, pady=0, fill="x")
    ttk.Entry(frame2, textvariable=tanggal_beli).pack(
        padx=0, pady=0, fill="x")
    ttk.Label(frame2, text="Kondisi Barang").pack(
        padx=0, pady=0, fill="x")
    ttk.Entry(frame2, textvariable=kondisi_barang).pack(
        padx=0, pady=0, fill="x")

    ttk.Button(frame2, text="Submit",
               command=submit_inventory).pack(pady=(20, 0))
    ttk.Button(frame2, text="Check Inventory",
               command=check_inventory).pack(pady=(20, 0))

# create default window tkinter GUI
window = tk.Tk()
window.title("Database App")
window.geometry("500x400")
window.resizable(False, False)

# define variable
username = tk.StringVar()
password = tk.StringVar()
tanggal_inventaris = tk.StringVar()
kode_barang = tk.StringVar()
nama_barang = tk.StringVar()
kuantitas = tk.StringVar()
tanggal_beli = tk.StringVar()
kondisi_barang = tk.StringVar()

# show frame 1
create_frame1()

# make GUI window always open
window.mainloop()
