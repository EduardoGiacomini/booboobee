# 🤖 Booboobee
Conjunto de bots utilitários para pequenas tarefas rotineiras.

## Bots

#### Weather Bot
O **Weather Bot** é responsável por apresentar informações sobre o clima do dia para uma determinada cidade. O Weather Bot é capaz de lhe apresentar, com precisão, as chances de chuva e temperaturas máxima e mínima.

#### Dollar Bot
O **Dollar Bot** é responsável por apresentar a cotação do dólar comercial do dia.


## Como executar?
Para executar o projeto, confira o tutorial a seguir.

### Requisitos
- [Python 3](https://www.python.org/downloads/);
- [pip3](https://pip.pypa.io/en/stable/installing/) (Normalmente é instalado junto ao Python);
- [virtualenv](https://pypi.org/project/virtualenv/).

### Instalação das dependências

#### Preparação do ambiente virtual (Opcional)
Inicialmente, vamos preparar um ambiente virtual para instalação das dependências. Na pasta raiz do projeto, execute:
```bash
virtualenv venv
```

A partir desse comando, será criado um ambiente virtual para instalação das dependências. Execute o comando a seguir
para fazer uso desse ambiente criado.
```bash
source venv/bin/activate
```

Ótimo. Agora todas as dependências que iremos utilizar ficarão salvas nessa pasta e não em sua máquina.

#### Instalação das dependências
Vamos instalar as dependências do projeto com o seguinte comando:
```bash
pip3 install -r requirements.txt
```

Com as dependências instaladas. Execute o projeto com:
```bash
python3 start.py
```

OBS: Caso você esteja utilizando uma IDE, como o Pycharm, este processo de configuração e instalação das dependências
em um ambiente virtual pode ser automático.
