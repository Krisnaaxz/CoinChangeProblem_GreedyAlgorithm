import tkinter as tk
from tkinter import messagebox

class KalkulatorKembalian:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Kalkulator Kembalian")

        # Input harga barang
        self.harga_barang_label = tk.Label(root, text="Harga Barang")
        self.harga_barang_label.grid(row=0, column=0)
        self.harga_barang = tk.Entry(root)
        self.harga_barang.grid(row=0, column=1)

        # Input nominal uang yang dibayarkan
        self.nominal_harga_label = tk.Label(root, text="Masukkan jumlah (rupiah)")
        self.nominal_harga_label.grid(row=1, column=0)
        self.nominal_harga = tk.Entry(root)
        self.nominal_harga.grid(row=1, column=1)

        # Tombol untuk menghitung kembalian
        self.calculate_button = tk.Button(root, text="Hitung Kembalian", command=self.calculate_change)
        self.calculate_button.grid(row=2, column=0, columnspan=2)

        # Listbox untuk menampilkan kembalian
        self.result_listbox = tk.Listbox(root, width=50)
        self.result_listbox.grid(row=3, column=0, columnspan=2)

    def calculate_change(self):
        try:
            kembalian = int(self.nominal_harga.get()) - int(self.harga_barang.get())
            if kembalian < 0:
                raise ValueError("Jumlah tidak boleh negatif")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            return

        uang = [5, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
        result = self.coin_change_greedy(kembalian, uang)

        if result is None:
            messagebox.showerror("Change Error", "Tidak bisa memberikan kembalian dengan nominal tersebut")
        else:
            self.result_listbox.delete(0, tk.END)
            self.result_listbox.insert(tk.END, "Kembalian:")
            for coin, count in result.items():
                self.result_listbox.insert(tk.END, f"{count} x {coin} Rupiah")

    def coin_change_greedy(self, kembalian, uang):
        uang.sort(reverse=True)
        pecahan_uang = {}
        for pecahan in uang:
            if kembalian >= pecahan:
                num_uang = kembalian // pecahan
                kembalian -= num_uang * pecahan
                pecahan_uang[pecahan] = num_uang
        if kembalian != 0:
            return None
        return pecahan_uang
    
def center_window(root: tk.Tk):
    # Update the geometry to get the window's actual size
    root.update_idletasks()

    # Get the window's width and height
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position x, y
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the position of the window
    root.geometry(f'+{x}+{y}')

if __name__ == "__main__":
    root = tk.Tk()
    app = KalkulatorKembalian(root)
    center_window(root)
    root.mainloop()