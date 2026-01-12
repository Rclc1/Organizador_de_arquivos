import os
import shutil

#Muda para a pasta que irei organizar
os.chdir("/storage/emulated/0/Download")

#Define os formatos que serão organizados
formatos = {
	"imagens": [".jpeg", ".png"],
	"documentos": [".docx", ".pdf"],
	"planilhas": [".xlsx", ".csv"],
	"textos": [".txt", ".json"]
}

#Verifica se as pastas existem, se não existirem, cria elas
if os.path.exists("Imagens"):
	print("O arquivo já existe!")
else:
	os.mkdir("Imagens")

if os.path.exists("Documentos"):
	print("O arquivo já existe!")
else:
	os.mkdir("Documentos")

if os.path.exists("Planilhas"):
	print("O arquivo já existe!")
else:
	os.mkdir("Planilhas")

if os.path.exists("Textos"):
	print("O arquivo já existe!")
else:
	os.mkdir("Textos")

#Listando todos os arquivos e pastas dentro da pasta principal
lista = os.listdir()

#Loop que lê os itens da lista, separa o nome do arquivo da extensão e guarda os arquivos nas pastas
for item in lista:
	nome, extensao = os.path.splitext(item)
	if extensao in formatos["imagens"]:
		shutil.move(item, "Imagens")
	elif extensao in formatos["documentos"]:
		shutil.move(item, "Documentos")
	elif extensao in formatos["planilhas"]:
		shutil.move(item, "Planilhas")
	elif extensao in formatos["textos"]:
		shutil.move(item, "Textos")