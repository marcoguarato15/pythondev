import xml.etree.ElementTree as ET

dados = """<?xml version='1.0' encoding='utf-8'?>
<clientes>
    <cliente>
        <id>1</id>
        <nome>Rodrigo</nome>
        <idade>30</idade>
        <cidade>Belo Horizonte</cidade>
    </cliente>
    <cliente>
        <id>2</id>
        <nome>Carlos</nome>
        <idade>22</idade>
        <cidade>São Paulo</cidade>
    </cliente>
</clientes>
"""

caminho_arquivo = "dados/clientes.xml"

# 1 - exportando dados para xml
with open(caminho_arquivo, "w", encoding="utf-8") as file:
    file.write(dados)

# 2 - Lendo dados do xml
tree = ET.parse(caminho_arquivo)
root = tree.getroot() # Pega a raiz <clientes>

for cliente in root.findall("cliente"):
    id = cliente.find("id").text
    nome = cliente.find("nome").text
    idade = cliente.find("idade").text
    cidade = cliente.find("cidade").text

    print(f"Id: {id} | Nome: {nome} | Idade: {idade} | Cidade: {cidade}")

# 3 - Adicionando novo cliente
novo_cliente = ET.Element("cliente")
id_novo = ET.SubElement(novo_cliente, "id")
id_novo.text = "5"
nome_novo = ET.SubElement(novo_cliente, "nome")
nome_novo.text = "Marco"
idade_novo = ET.SubElement(novo_cliente, "idade")
idade_novo.text = "24"
cidade_novo = ET.SubElement(novo_cliente, "cidade")
cidade_novo.text = "Uberaba"

root.append(novo_cliente)

# Salvando no XML
tree.write(caminho_arquivo, encoding="utf-8", xml_declaration=True)