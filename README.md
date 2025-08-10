# 📁 Organizador de Arquivos

Este é um script em **Python** simples e utilitário, projetado para organizar e limpar automaticamente sua pasta de Downloads. Ele classifica os arquivos por tipo de extensão e os move para as pastas correspondentes, tanto as pastas padrão do sistema (como Documentos, Vídeos e Imagens) quanto pastas personalizadas.

-----

## ✨ Funcionalidades

  * **Organização Automática:** Classifica arquivos com base em sua extensão.
  * **Pastas Padrão:** Move arquivos para suas respectivas pastas no sistema Windows:
      * `Downloads` -\> `Documents` (documentos)
      * `Downloads` -\> `Music` (músicas)
      * `Downloads` -\> `Pictures` (fotos)
      * `Downloads` -\> `Videos` (vídeos)
  * **Pastas Personalizadas:** Cria e move arquivos para subpastas dentro da própria pasta de Downloads para melhor organização:
      * `Downloads` -\> `Downloads/Instaladores` (`.exe`, `.msi`)
      * `Downloads` -\> `Downloads/Compactados` (`.zip`, `.rar`, `.7z`, etc.)
  * **Organização de ROMs:** Detecta e move automaticamente arquivos de ROMs para subpastas específicas, como:
      * `Downloads` -\> `Downloads/ROMs/3DS`
      * `Downloads` -\> `Downloads/ROMs/NDS`
      * `Downloads` -\> `Downloads/ROMs/SNES`

-----

## 🛠️ Como Usar

1.  Salve o código como um arquivo `.py` (por exemplo, `organizador.py`).
2.  Coloque o arquivo na sua pasta de Downloads ou em qualquer outro diretório.
3.  Execute o script com o Python.

<!-- end list -->

```bash
python organizador.py
```

O script vai rodar, criar as pastas se ainda não existirem e mover os arquivos automaticamente, exibindo no terminal quais arquivos foram movidos e para onde.

-----

## ⚙️ Como Personalizar o Código

Você pode facilmente modificar o script para adicionar ou alterar categorias de arquivos.

### 1\. Adicionando uma Nova Categoria de Arquivo

Para adicionar um novo tipo de arquivo e movê-lo para uma pasta específica, basta editar o dicionário `categorias`.

Por exemplo, para organizar arquivos `.iso` na pasta `Instaladores`, adicione a extensão na lista:

```python
categorias = {
    # ... outras categorias
    instaladores: [".exe", ".msi", ".iso"], # Adicionei o ".iso" aqui
    # ... outras categorias
}
```

### 2\. Adicionando uma Nova Pasta e Categoria

Se você quiser criar uma nova pasta para um tipo de arquivo que ainda não existe no script, siga estes passos:

**a.** Crie uma nova variável para o caminho da pasta:

```python
# No início do arquivo, junto com as outras pastas personalizadas
designs = os.path.join(downloads, "Designs")
```

**b.** Adicione a nova pasta para ser criada no loop `for`:

```python
# No loop de criacao de pastas
for pasta in [instaladores, compactados, designs, documentos, musicas, fotos, videos]:
    os.makedirs(pasta, exist_ok=True)
```

**c.** Adicione a nova pasta e suas extensões ao dicionário `categorias`:

```python
categorias = {
    designs: [".psd", ".ai", ".svg", ".fig"], # Nova categoria para designs
    # ... outras categorias
}
```

### 3\. Modificando as Pastas de ROMs

O processo é o mesmo para as ROMs. Para adicionar suporte a novas plataformas, edite o dicionário `roms_subpastas`:

```python
roms_subpastas = {
    "3DS": [".3ds", ".cia"],
    "NDS": [".nds"],
    "SNES": [".smc", ".sfc"],
    "GBA": [".gba"], # Adicionei suporte para Game Boy Advance
    "PS2": [".iso"], # Adicionei suporte para PlayStation 2
}
```
