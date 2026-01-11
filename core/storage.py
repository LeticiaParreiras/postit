import json
import os
from datetime import datetime

ARQUIVO_DADOS = "postits.json"

def salvar_postit(conteudo, estado):
    """Salva um novo post-it no arquivo JSON"""
    if estado.get("id"):
        atualizar_postit(estado, conteudo)
        return estado
    dados = carregar_postits()
    novo_postit = {
        "id": len(dados) + 1,
        "conteudo": conteudo,
        "cor": estado["color"],
        "data": datetime.now().isoformat()
    }
    dados.append(novo_postit)
    _escrever_json(dados)
    estado["id"] = novo_postit["id"]
    return estado

def carregar_postits():
    """Carrega todos os post-its do arquivo JSON"""
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def deletar_postit(estado, text_widget):
    """Deleta um post-it pelo ID e limpa a interface"""
    dados = carregar_postits()
    dados = [p for p in dados if p["id"] != estado["id"]]
    _escrever_json(dados)
    text_widget.delete("1.0", "end")
    estado["id"] = None

def atualizar_postit(estado, conteudo ):
    """Atualiza um post-it existente"""
    dados = carregar_postits()
    for postit in dados:
        if postit["id"] == estado["id"]:
            postit["conteudo"] = conteudo
            postit["cor"] = estado["color"]
            postit["data_atualizacao"] = datetime.now().isoformat()
            break
    _escrever_json(dados)
    

def _escrever_json(dados):
    """Escreve dados no arquivo JSON"""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def limpar_todos():
    """Limpa todos os post-its"""
    _escrever_json([])
