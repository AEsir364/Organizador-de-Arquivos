# 📂 Organizador de Arquivos Autônomo

Um script em **Python** projetado para funcionar como um serviço em segundo plano no Windows, organizando e limpando automaticamente sua pasta de Downloads a cada 10 minutos.

Ele classifica os arquivos por tipo de extensão e os move para as pastas correspondentes do sistema (Documentos, Vídeos, Imagens) ou para subpastas personalizadas, mantendo seu ambiente de trabalho sempre limpo, sem a necessidade de execução manual.

---

## ✨ Funcionalidades

* **Execução Autônoma e Discreta:** Roda a cada 10 minutos em segundo plano, sem abrir nenhuma janela de terminal (graças à extensão `.pyw`).
* **Organização Automática:** Classifica arquivos com base em sua extensão.
* **Pastas Padrão do Windows:** Move arquivos para suas respectivas pastas de usuário:
    * `Downloads` -> `Documents` (documentos)
    * `Downloads` -> `Music` (músicas)
    * `Downloads` -> `Pictures` (fotos)
    * `Downloads` -> `Videos` (vídeos)
* **Pastas Personalizadas:** Cria e move arquivos para subpastas dentro da própria pasta de Downloads para melhor organização:
    * `Downloads` -> `Downloads/Instaladores` (`.exe`, `.msi`)
    * `Downloads` -> `Downloads/Compactados` (`.zip`, `.rar`, `.7z`, etc.)
* **Organização de ROMs:** Detecta e move automaticamente arquivos de ROMs para subpastas específicas por console (3DS, PS1, PS2, PSP, etc.).

---

## 🚀 Como Usar (Instalação)

Para fazer o script rodar automaticamente no seu computador, siga estes passos:

1.  **Baixe o Repositório:** Faça o download ou clone este repositório para uma pasta permanente no seu computador (por exemplo, em `C:/MeusScripts/`).

2.  **Crie um Atalho:**
    * Dentro da pasta, encontre o arquivo `organizador.pyw`.
    * Clique com o botão direito sobre ele e selecione **"Criar atalho"**.

3.  **Adicione o Atalho à Inicialização do Windows:**
    * Pressione as teclas **`Win` + `R`** para abrir a caixa de diálogo "Executar".
    * Digite `shell:startup` e pressione Enter. Isso abrirá a pasta de inicialização do Windows.
    * **Mova o atalho** que você criou no passo 2 para dentro desta pasta.

Pronto! Agora, toda vez que você ligar o computador, o script `organizador.pyw` será iniciado automaticamente e começará a organizar sua pasta de Downloads a cada 10 minutos, tudo em segundo plano.

---

## ⚙️ Como Personalizar o Código

Você pode facilmente modificar o script `organizador.pyw` para adicionar ou alterar categorias de arquivos.

### 1. Adicionando uma Nova Categoria

Para organizar arquivos `.iso` na pasta `Instaladores`, por exemplo, basta editar o dicionário `categorias`:

```python
categorias = {
    # ...
    instaladores: [".exe", ".msi", ".iso"], # Adicionei o ".iso" aqui
    # ...
}
```

### 2. Modificando as Pastas de ROMs

Para adicionar suporte a novas plataformas, edite o dicionário `roms_subpastas`:

```python
roms_subpastas = {
    "3DS": [".3ds", ".cia"],
    "NDS": [".nds"],
    # ...
    "GBA": [".gba"], # Exemplo: Adicionando suporte para Game Boy Advance
}
```
