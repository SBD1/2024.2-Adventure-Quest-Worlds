# 2024.2-Adventure-Quest-World
Repositório para desenvolvimento do jogo Adventure Quest World da disciplina de SBD1 - 2024.2

![aqw](./aqw.jpg)

## Integrantes da equipe

| Nome         | Perfil do github                                 | Matrícula|
|--------------|--------------------------------------------------|----------|
| Arthur Ribeiro | [artrsousa1](https://github.com/artrsousa1)        | 221007850 |
| Bruno Bragança | [brunobreis](https://github.com/brunobreis)      | 221007902 |
| Caio Habibe Falcão| [caiohabibe](https://github.com/caiohabibe)| 221021868 |
| Henrique Quenino  | [henriquecq](https://github.com/henriquecq)            | 221008098 |

## Como executar o projeto

Na raiz do projeto, execute o seguinte comando para criar as variáveis de ambiente:

```bash
make config
```

Na raiz do projeto, execute o seguinte comando para subir o banco de dados e o pgAdmin 4:

```bash
make build
```

O pgAdmin estará disponível para acesso em `http://localhost:8000`. As credenciais padrão para acesso são:

- Email: `admin@admin.com`
- Senha: `admin`

Certifique-se de que o banco de dados está rodando corretamente e então execute o seguinte comando na diretório `game`:

```bash
# Criação do ambiente virtual
python3 -m venv env

# Ativação do ambiente virtual
source env/bin/activate

# Instalação das dependências
pip install -r requirements.txt
```

## Videos de apresentação

| Módulo         | Link da gravação       | Data |
|:--------------:|------------------------|------|
| 1              | [Apresentação Módulo 1](https://youtu.be/rttzNn9oLz4) | 25/11/2024 |
| 2              | [Apresentação Módulo 2](https://youtu.be/mHI9vepULyg) | 13/01/2025 |

## Entregas

- Módulo 1
  - [DER(Diagrama Entidade Relacionamento)_V1](./Modulo_1/DER(Diagrama_Entidade_Relacionamento).png)
  - [ME-R(Modelo Entidade Relacionamento)_V1](./Modulo_1/ME-R(Modelo_Entidade_Relacionamento).md)
  - [DD(Dicinario de Dados)_V1](./Modulo_1/DD(Dicinario_de_Dados).md)
- Módulo 2
  - [DER(Diagrama Entidade Relacionamento)_V2](./Modulo_2/DER(Diagrama_Entidade_Relacionamento)_v2.png)
  - [ME-R(Modelo Entidade Relacionamento)_V2](./Modulo_2/ME-R(Modelo_Entidade_Relacionamento)_v2.1.md)
  - [DD(Dicinario de Dados)_V2](./Modulo_2/DD(Dicinario_de_Dados)_v2.1.md)
- Módulo 3
  - [DER(Diagrama Entidade Relacionamento)_V3](./Modulo_3/DER(Diagrama_Entidade_Relacionamento)_v3.jpg)
  - [ME-R(Modelo Entidade Relacionamento)_V3](./Modulo_3/ME-R(Modelo_Entidade_Relacionamento)_v3.md)
  - [DD(Dicinario de Dados)_V3](./Modulo_3/DD(Dicinario_de_Dados)_v3.md)
