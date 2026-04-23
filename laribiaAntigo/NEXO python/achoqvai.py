import tkinter as tk
from tkinter import font

# Janela principal
root = tk.Tk()
root.title("Cadastro PC")
root.geometry("1920x1080")
root.configure(bg="#E1F5FF")

# Container principal (Rectangle 7)
main_frame = tk.Frame(root, width=1150, height=800, bg="#DFFFE4")
main_frame.place(x=100, y=140)  # Ajuste a posição conforme necessário

# Lado esquerdo (Rectangle 8)
left_panel = tk.Frame(main_frame, width=760, height=800, bg="#6FA576")
left_panel.place(x=0, y=0)

# Lado direito (Rectangle 9)
right_panel = tk.Frame(main_frame, width=327, height=800, bg="#DFFFE4")
right_panel.place(x=760, y=0)

# Título "Bem vindo(a)!"
welcome_label = tk.Label(left_panel, text="Bem vindo(a)!", font=("Arial", 60), fg="white", bg="#6FA576")
welcome_label.place(x=100, y=50)

# Subtítulo
subtitle = tk.Label(left_panel, text="Já possuí uma conta?\nFaça seu login abaixo.", font=("Arial", 30), fg="white", bg="#6FA576", justify="center")
subtitle.place(x=100, y=150)

# Botão "Logar-se"
login_button = tk.Button(left_panel, text="Logar-se", font=("Arial", 25), fg="white", bg="#6FA576", bd=2, relief="ridge", highlightbackground="white", highlightthickness=1)
login_button.place(x=250, y=300, width=267, height=64)

# Título "Faça seu cadastro"
cadastro_label = tk.Label(right_panel, text="Faça seu cadastro", font=("Arial", 30), fg="#6FA576", bg="#DFFFE4")
cadastro_label.place(x=20, y=30)

# Campos de entrada
def create_entry(parent, label_text, y):
    label = tk.Label(parent, text=label_text, font=("Arial", 20), fg="#DFFFE4", bg="#6FA576")
    label.place(x=20, y=y)
    entry_bg = tk.Frame(parent, bg="#ABD8B1", width=767, height=78)
    entry_bg.place(x=20, y=y+40)

create_entry(left_panel, "Nome", 400)
create_entry(left_panel, "Email", 500)
create_entry(left_panel, "Telefone", 600)
create_entry(left_panel, "Senha", 700)
create_entry(left_panel, "Confirmar senha", 800)

# Botão "Fazer cadastro"
cadastro_btn = tk.Button(right_panel, text="Fazer cadastro", font=("Arial", 25), fg="#DFFFE4", bg="#6FA576", bd=0)
cadastro_btn.place(x=20, y=700, width=302, height=54)

# Janela principal

# Função para criar rótulos estilizados
def create_label(parent, text, x, y, width, height, font_size, color="#FFFFFF", bg="#E1F5FF"):
    label = tk.Label(parent, text=text, font=("Arial", font_size), fg=color, bg=bg, wraplength=width, justify="center")
    label.place(x=x, y=y, width=width, height=height)

# Textos principais
create_label(root, "Se você é monitor(a):", 100, 50, 623, 84, 70)
create_label(root, "Se você é leitor(a):", 800, 50, 546, 84, 70)
create_label(root, "Insira o email do(a) coordenador(a) da biblioteca aqui para a validação do seu cadastro.", 100, 200, 565, 144, 35)
create_label(root, "Clique aqui para seguir em frente e continuar seu acesso normalmente.", 800, 200, 565, 144, 35)

# Menu inferior
create_label(root, "Início", 100, 400, 153, 84, 70, color="#1E1E1E")
create_label(root, "Retirada", 300, 400, 247, 84, 70, color="#1E1E1E")

# Janela principal
root = tk.Tk()
root.title("Cadastro M / CB")
root.geometry("1920x1080")
root.configure(bg="#E1F5FF")

# Função para criar rótulos estilizados
def create_label(parent, text, x, y, width, height, font_size, color="#FFFFFF", bg="#E1F5FF"):
    label = tk.Label(parent, text=text, font=("Arial", font_size), fg=color, bg=bg, wraplength=width, justify="center")
    label.place(x=x, y=y, width=width, height=height)

# Textos principais
create_label(root, "Se você é monitor(a):", 100, 50, 623, 84, 70)
create_label(root, "Se você é leitor(a):", 800, 50, 546, 84, 70)
create_label(root, "Insira o email do(a) coordenador(a) da biblioteca aqui para a validação do seu cadastro.", 100, 200, 565, 144, 35)
create_label(root, "Clique aqui para seguir em frente e continuar seu acesso normalmente.", 800, 200, 565, 144, 35)

# Menu inferior
create_label(root, "Início", 100, 400, 153, 84, 70, color="#1E1E1E")
create_label(root, "Retirada", 300, 400, 247, 84, 70, color="#1E1E1E")

# Função para criar rótulos estilizados
def create_label(parent, text, x, y, width, height, font_size, color="#1E1E1E", bg="#E1F5FF"):
    label = tk.Label(parent, text=text, font=("Arial", font_size), fg=color, bg=bg, wraplength=width, justify="center")
    label.place(x=x, y=y, width=width, height=height)

# Navegação
create_label(root, "Início", 50, 50, 153, 84, 70)
create_label(root, "Retirada", 250, 50, 247, 84, 70)
create_label(root, "Devoluções", 550, 50, 334, 84, 70)
create_label(root, "Comunidade", 900, 50, 360, 84, 70)

# Linha decorativa (Line 3)
line = tk.Frame(root, bg="#1E1E1E", height=5, width=265)
line.place(x=250, y=140)

# Campo de pesquisa
search_frame = tk.Frame(root, bg="#508699", width=844, height=79)
search_frame.place(x=100, y=200)
search_frame.configure(bg="#508699", highlightbackground="#508699")

search_entry = tk.Entry(search_frame, font=("Arial", 20), bg="#C0D9E0", fg="#1E1E1E", relief="flat")
search_entry.place(x=20, y=20, width=600, height=40)

search_label = tk.Label(search_frame, text="Pesquisar...", font=("Arial", 30), fg="#1E1E1E", bg="#C0D9E0")
search_label.place(x=640, y=15)

# Campos de entrada
create_label(root, "Nome do(s) livro(s):", 100, 320, 548, 82, 68, color="#508699")
create_label(root, "Quantidade de livro(s) que deseja:", 100, 420, 955, 82, 68, color="#508699")

# Ícones decorativos (simulados como botões)
def create_icon(x, y, size=40):
    icon = tk.Frame(root, bg="#A0A0A0", width=size, height=size)
    icon.place(x=x, y=y)

# Simulando ícones question/menu
for i in range(10):
    create_icon(100 + i * 70, 550, 40)  # question icons
    create_icon(100 + i * 70, 600, 64)  # menu icons

root.mainloop()
