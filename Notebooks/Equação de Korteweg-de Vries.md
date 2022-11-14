---

# IMPORTANTE!
A plataforma GitHub na qual são postados todos os `Notebooks` do projeto [PET.py](https://github.com/GabrielWendell/PET.py/blob/main/README.md) possui uma limitação de arquivos de 25 MB, isso quer dizer que qualquer arquivo que você deseje postar no GitHub não deve ultrapassar 25 MB de tamanho.

Este `Notebook` em particular, devido a uma série de gráficos interativos gerados ao longo do mesmo, acabou tendo uma extensão maior do que a permitida pelo GitHub (84MB+). Dessa forma, para não compromenter a qualidade do projeto, optou-se por comprimir o `Notebook` original para que o leitor possa acompanhar o mesmo sem demais problemas em sua própria máquina.

Dessa forma, este arquivo .md visa explicar ao leitor o passo a passo necessário para a descompactação e abertura do `Notebook` *A equação de Korteweg-de Vries*.

## Abrindo o `Notebook` original

Vamos aqui explicar como acessar o `Notebook` original. Para isso, o leitor precisará primeiro realizar a descompactação do arquivo .rar e então abrir o arquivo .ipynb pelo Jupyter. Segue abaixo o detalhamento de cada passo.


### Passo 1: Descompactando o arquivo `.rar` 

O `Notebook` originou foi comprimido na extensão .rar e se encontra dentro da pasta [`Notebooks`](https://github.com/GabrielWendell/PET.py/tree/main/Notebooks) para download. Para acessar o `Notebook` basta baixar o arquivo `Astrodinâmica de satélites artificiais.rar` e abrir o arquivo comprimido com um descompactador de sua escolha (WinRAR, 7z, WinZip, etc) e extrair o `Notebook` intitulado `Astrodinâmica de satélites artificiais.ipynb`. Clique [aqui](https://www.win-rar.com/download.html?&L=0) para baixar o instalador do WinRAR 64.

### Passo 2: Instalando o `Jupyter`

Para acessar o `Notebook` original, você precisará ter instalado em sua máquina o [`Jupyter`](https://jupyter.org) cujo instalação pode ser feita através do seguinte comando:

- Usando o `pip`:
```
$ pip install jupyterlab
```

- Usando o `conda`:
```
$ conda install -c conda-forge jupyterlab
```

### Passo 3: Executando o Jupyter Notebook

Uma vez instalado o `Jupyter`, para executá-lo basta digitar o seguinte comando em um terminal de sua preferência:

```
$ jupyter notebook
```

Para mais informações sobre a instalação do Jupyter, clique [aqui](https://jupyter.org/install) para checar o passo a passo da intalação do mesmo em sua máquina.

Uma vez aberto o `Jupyter`, basta navegar até a pasta onde está salvo o `Notebook` e executá-lo usando o kernel do Python3.


### Links
- `Astrodinâmica de satélites artificiais.rar`: https://github.com/GabrielWendell/PET.py/blob/main/Notebooks/Astrodinâmica%20de%20satélites%20artificiais.rar
- Instalador WinRAR 64: https://www.win-rar.com/download.html?&L=0
- Página oficial do Jupyter: https://jupyter.org
- Guia de instalação do Jupyter: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
- Documentação do Jupyter: https://jupyterlab.readthedocs.io/en/stable/

---
