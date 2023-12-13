import tkinter as tk
import sqlite3
import hashlib
import random
import string

def create_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title('Gestor de contraseñas')

    # Crear la base de datos
    conn = sqlite3.connect('C:\\Users\\Bansa\\Desktop\\safe\\programas\\gestor-contraseñas\\passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (app text, password text)''')

    # Crear la función para añadir una contraseña
    def add_password():
        app = app_entry.get()
        password = password_entry.get()
        if not app or not password:
            return
        c.execute("INSERT INTO passwords VALUES (?, ?)", (app, hash_password(password)))
        conn.commit()
        app_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    # Crear la función para mostrar las contraseñas
    def show_passwords():
        c.execute("SELECT * FROM passwords")
        for row in c.fetchall():
            print(f"App: {row[0]}, Password: {row[1]}")

    # Crear los campos de entrada
    app_entry = tk.Entry(root)
    app_entry.grid(row=0, column=0)
    password_entry = tk.Entry(root)
    password_entry.grid(row=0, column=1)

    # Crear los botones
    add_button = tk.Button(root, text='Añadir contraseña', command=add_password)
    add_button.grid(row=1, column=0)
    show_button = tk.Button(root, text='Mostrar contraseñas', command=show_passwords)
    show_button.grid(row=1, column=1)
    generate_button = tk.Button(root, text='Generar contraseña', command=lambda: password_entry.insert(0, create_password()))
    generate_button.grid(row=2, column=0)

    # Ejecutar la ventana
    root.mainloop()

if __name__ == "__main__":
    main()
