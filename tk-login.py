import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

contas = [
    ("admin", "123"),
    ("kallak", "hub")
]

janela = ctk.CTk()
janela.title("Login")
janela.state("zoomed")

bg_image = ctk.CTkImage(
    light_image=Image.open("imagens_desafio/matrix.jpg"),
    dark_image=Image.open("imagens_desafio/matrix.jpg"),
    size=(1920, 1080)
)

bg_label = ctk.CTkLabel(janela, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

pagina_login = ctk.CTkFrame(
    janela,
    width=400,
    height=400,
    corner_radius=20
)
pagina_login.place(relx=0.5, rely=0.5, anchor="center")

ctk.CTkLabel(
    pagina_login,
    text="Login",
    font=ctk.CTkFont(size=24, weight="bold")
).pack(pady=(20, 10))

usuario_entry = ctk.CTkEntry(
    pagina_login,
    placeholder_text="Usuário",
    width=300,
    height=40
)
usuario_entry.pack(pady=10)

senha_entry = ctk.CTkEntry(
    pagina_login,
    placeholder_text="Senha",
    show="*",
    width=300,
    height=40
)
senha_entry.pack(pady=10)

mostrar = False

def mostra_senha():
    global mostrar
    mostrar = not mostrar
    senha_entry.configure(show="" if mostrar else "*")
    botao_mostrar.configure(text="Ocultar" if mostrar else "Mostrar")

botao_mostrar = ctk.CTkButton(
    pagina_login,
    text="Mostrar",
    command=mostra_senha,
    width=120,
    height=30,
    fg_color="transparent",
    hover_color="#2a2a2a"
)
botao_mostrar.pack(pady=5)

mensagem_label = ctk.CTkLabel(pagina_login, text="", text_color="red")
mensagem_label.pack()

def login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    if (usuario, senha) in contas:
        pagina_login.place_forget()
        pagina_sistema.place(relwidth=1, relheight=1)
    else:
        mensagem_label.configure(text="Credenciais inválidas")

botao_login = ctk.CTkButton(
    pagina_login,
    text="Entrar",
    command=login,
    width=300,
    height=40
)
botao_login.pack(pady=20)

pagina_sistema = ctk.CTkFrame(janela)

bg_label2 = ctk.CTkLabel(pagina_sistema, image=bg_image, text="")
bg_label2.place(x=0, y=0, relwidth=1, relheight=1)

ctk.CTkLabel(
    pagina_sistema,
    text="Bem-vindo ao sistema!",
    font=ctk.CTkFont(size=28, weight="bold")
).pack(pady=40)

img = ctk.CTkImage(
    light_image=Image.open("imagens_desafio/pyt.jpg"),
    dark_image=Image.open("imagens_desafio/pyt.jpg"),
    size=(500, 500)
)

ctk.CTkLabel(pagina_sistema, image=img, text="").pack()

janela.mainloop()