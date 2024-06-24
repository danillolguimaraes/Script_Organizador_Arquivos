# organizador de arquivos pasta downlaod windows

import os

os.getcwd();

os.chdir(r"c:\\Users\\Dan_n\\Downloads\\");
lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path.isfile(arquivo)];
lista_tipo = {tipo.split(".")[-1] for tipo in lista_arquivos};

for tipo in lista_tipo:
  if os.path.exists(tipo):
    pass
  else:
    os.mkdir(tipo);

for arquivo in lista_arquivos:
  pasta_destino = arquivo.split(".")[-1]
  print(pasta_destino)
  de = os.path.join(os.getcwd(), arquivo)
  para = os.path.join(os.getcwd(), pasta_destino, arquivo)
  if os.path.exists(de):
    os.replace(de, para)