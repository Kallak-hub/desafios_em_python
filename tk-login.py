import tkinter as tk
from PIL import Image, ImageTk

contas = [
    ("admin", "123"),
    ("kallak", "hub")
]

janela = tk.Tk()
janela.title("Login")
janela.state("zoomed")
janela.configure(bg="#121212")

bg_img = Image.open("imagens_desafio/matrix.jpg")
bg_img = bg_img.resize((janela.winfo_screenwidth(), janela.winfo_screenheight()))
bg_tk_login = ImageTk.PhotoImage(bg_img)

background_login = tk.Label(janela, image=bg_tk_login)
background_login.place(x=0, y=0, relwidth=1, relheight=1)
background_login.image = bg_tk_login

pagina_login = tk.Frame(janela, bg="#1e1e1e")
pagina_login.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(
    pagina_login,
    text="Usuário",
    bg="#1e1e1e",
    fg="#bbbbbb",
    font=("Segoe UI", 14)
).pack(anchor="w", padx=20, pady=(20, 5))

usuario_entry = tk.Entry(
    pagina_login,
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    bd=0,
    width=40,
    font=("Segoe UI", 14)
)
usuario_entry.pack(pady=8, ipady=10)

tk.Label(
    pagina_login,
    text="Senha",
    bg="#1e1e1e",
    fg="#bbbbbb",
    font=("Segoe UI", 14)
).pack(anchor="w", padx=20)

senha_entry = tk.Entry(
    pagina_login,
    show="*",
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    bd=0,
    width=40,
    font=("Segoe UI", 14)
)
senha_entry.pack(pady=8, ipady=10)

def login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    if (usuario, senha) in contas:
        pagina_login.place_forget()
        pagina_sistema.pack(fill="both", expand=True)
    else:
        mensagem_label["text"] = "As credenciais são inválidas"

mostrar = False
def mostra_senha():
    global mostrar
    mostrar = not mostrar
    senha_entry.config(show="" if mostrar else "*")
    botao_mostrar.config(text="Ocultar" if mostrar else "Mostrar")

botao_mostrar = tk.Button(
    pagina_login, 
    text="Mostrar",
    command=mostra_senha,
    bg="#1e1e1e",
    fg="#4CAF50",
    bd=0,
    activebackground="#1e1e1e",
    activeforeground="#4CAF50",
    cursor="hand2",
    font=("Segoe UI", 12)
)
botao_mostrar.pack(pady=(5, 15))

botao_login = tk.Button(
    pagina_login,
    text="Entrar",
    command=login,
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    bd=0,
    padx=20,
    pady=10,
    cursor="hand2",
    font=("Segoe UI", 14, "bold")
)
botao_login.pack(pady=20)

mensagem_label = tk.Label(
    pagina_login,
    bg="#1e1e1e",
    fg="red",
    font=("Segoe UI", 12)
)
mensagem_label.pack(pady=(0, 15))

pagina_sistema = tk.Frame(janela)

bg_img2 = Image.open("imagens_desafio/matrix.jpg")
bg_img2 = bg_img2.resize((janela.winfo_screenwidth(), janela.winfo_screenheight()))
bg_tk_sistema = ImageTk.PhotoImage(bg_img2)

background_sistema = tk.Label(pagina_sistema, image=bg_tk_sistema)
background_sistema.place(x=0, y=0, relwidth=1, relheight=1)
background_sistema.image = bg_tk_sistema

tk.Label(
    pagina_sistema,
    text="Bem-vindo ao sistema!",
    font=("Segoe UI", 22),
    bg="#121212",
    fg="white"
).pack(pady=50)

img = Image.open("imagens_desafio/pyt.jpg")
img = img.resize((350, 350))
img_tk = ImageTk.PhotoImage(img)

label = tk.Label(pagina_sistema, image=img_tk, bg="#121212")
label.image = img_tk
label.pack()

janela.mainloop()