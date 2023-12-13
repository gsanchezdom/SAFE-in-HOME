import tkinter as tk
import os

def open_file():
    os.system('python "C:\\Users\\Bansa\\Desktop\\safe\\programas\\gestor-contraseñas\\main-gestor.py"')

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title('SAFETY AT HOME')

    # Configurar el color de fondo
    root.configure(bg='#3d5758')

    # Crear un botón con el color especificado
    button1 = tk.Button(root, text='Gestor de contraseñas', bg='#04031B', fg='white', font=('arial', 13), command=open_file)
    button1.grid(row=0, column=0, sticky='nsew')  # Posicionar el botón en la cuadrícula

    button2 = tk.Button(root, text='Esteganografía', bg='#b9d9eb', fg='black', font=('arial', 13))
    button2.grid(row=1, column=0, sticky='nsew')  # Posicionar el botón en la cuadrícula

    button3 = tk.Button(root, text='Encriptación de archivos', bg='#c2e0ed', fg='black', font=('arial', 13))
    button3.grid(row=0, column=1, sticky='nsew')  # Posicionar el botón en la cuadrícula

    button4 = tk.Button(root, text='Verificación de dos factores (2AF)', bg='#04031B', fg='white', font=('arial', 13))
    button4.grid(row=1, column=1, sticky='nsew')  # Posicionar el botón en la cuadrícula

    # Hacer que todas las filas y columnas sean elásticas
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Configurar el tamaño de la ventana para que ocupe el 75% de la pantalla
    width = int(root.winfo_screenwidth() * 0.75)
    height = int(root.winfo_screenheight() * 0.75)

    # Calcular la posición de la ventana para que aparezca en el centro de la pantalla
    position_top = int(root.winfo_screenheight() / 2 - height / 2)
    position_right = int(root.winfo_screenwidth() / 2 - width / 2)

    # Configurar la geometría de la ventana
    root.geometry(f"{width}x{height}+{position_right}+{position_top}")

    # Configurar el tamaño mínimo de la ventana
    root.minsize(width//2, height//2)

    # Configurar Icono del programa
    root.iconbitmap("programas\guide-menu\logo.ico")

    # Ejecutar la ventana
    root.mainloop()

if __name__ == "__main__":
    main()
