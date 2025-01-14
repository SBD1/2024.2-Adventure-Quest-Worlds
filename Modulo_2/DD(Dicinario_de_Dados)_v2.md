## Dicionário de Dados

---

### **Usuário**
#### Descrição: Entidade que armazena os dados de login dos jogadores.
#### Observações: Um usuário pode até 3 saves.
| Nome Variável |     Tipo     |             Descrição           | Restrição | Chave |
| :-----------: | :----------: | :-----------------------------: | :-------: | :---: |
|   idUsuario   |     int      | Identificador único do usuário |  NOT NULL |   PK  |
|      login    | varchar[20]   |  Nome de usuário para login      |  NOT NULL |   -   |
|     senha     | varchar[20]   | Senha do usuário             |  NOT NULL |   -   |
| qtdPersonagem |     int     | Número de personagens do usuário |  NOT NULL |   -   |

---

### **Save**
#### Descrição: Entidade que armazena os dados dos saves dos jogadores.
#### Observações: Um save pertence a um usuário, e um usuario pode ter até 3 saves.
| Nome Variável |     Tipo     |             Descrição           | Restrição | Chave |
| :-----------: | :----------: | :-----------------------------: | :-------: | :---: |
|   idUsuario  |     int      | Identificador do usuário dono do save |  NOT NULL |   FK  |
|   idPersonagem |     int     | Identificador do personagem do save |  NOT NULL |   FK  |

---

### **Personagem**
#### Descrição: Entidade que armazena os dados dos personagens dos jogadores.
#### Observações: Um personagem pertence a uma classe e está em uma sala.

| Nome Variável       |     Tipo     |                Descrição             | Restrição | Chave |
| :------------------: | :----------: | :---------------------------------: | :-------: | :---: |
|    idPersonagem     |     int      |    Identificador único do personagem  |  NOT NULL |   PK  |
|      nomePersonagem   | varchar[20]   | Nome do personagem                  |  NOT NULL |   -   |
| staminaAtualPersonagem|     int     |   Stamina atual do personagem     |  NOT NULL |   -   |
|   vidaAtualPersonagem|     int     |   Vida atual do personagem     |  NOT NULL |   -   |
|staminaBasePersonagem |     int     |   Stamina base do personagem     |  NOT NULL |   -   |
|   vidaBasePersonagem|     int     |     Vida base do personagem     |  NOT NULL |   -   |
|  defesaPersonagem   |     int      |    Defesa do personagem             |  NOT NULL |   -   |
|   ataqueFisico      |     int      |   Ataque físico do personagem        |  NOT NULL |   -   |
|   ataqueMagico      |     int      | Ataque mágico do personagem         |  NOT NULL |   -   |

---
### **Classe**
#### Descrição: Entidade que armazena os dados das classes dos personagens.
#### Observações: Uma classe pode ter várias habilidades.

| Nome Variável |     Tipo     |          Descrição         | Restrição | Chave |
| :-----------: | :----------: | :------------------------: | :-------: | :---: |
|   idClasse    |     int      | Identificador único da classe |  NOT NULL |  PK   |
|  nomeClasse   | varchar[30]   |        Nome da classe        |  NOT NULL |  -   |
|    mulFisico  |    float    | Multiplicador de ataque físico |  NOT NULL |  -   |
|   mulMagico   |    float    |  Multiplicador de ataque mágico |  NOT NULL |  -   |
---
### **Habilidade**
#### Descrição: Entidade que armazena os dados das habilidades dos personagens.
#### Observações: Uma habilidade pertence a uma classe.

| Nome Variável   |     Tipo     |             Descrição            | Restrição | Chave |
| :--------------: | :----------: | :-----------------------------: | :-------: | :---: |
|   idHabilidade  |     int      |  Identificador único da habilidade |  NOT NULL |   PK  |
|  nomeHabilidade | varchar[30]   |       Nome da habilidade         |  NOT NULL |  -   |
|     danoFisico    |     int      |       Dano físico da habilidade     |  NOT NULL |  -   |
|    danoMagico    |     int      |      Dano mágico da habilidade     |  NOT NULL |  -   |
|   custoStamina   |     int      | Custo de stamina da habilidade   |  NOT NULL |  -   |
|  custoCooldown  |     int      |  Cooldown da habilidade         |  NOT NULL |   -  |
---
### **Inventario**
#### Descrição: Entidade que armazena os itens do personagem.
#### Observações: Um inventário pertence a um personagem.

| Nome Variável  |     Tipo     |         Descrição        | Restrição | Chave |
| :-------------: | :----------: | :---------------------: | :-------: | :---: |
|   idPersonagem |     int      | Identificador do personagem dono do inventário | NOT NULL|   FK |
|espacoDisponivel |     int      | Espaço disponível no inventário |  NOT NULL |   -   |
|   capacidade   |     int      |  Capacidade do inventário   |  NOT NULL |   -   |
| quantidadeOuro   |    int     | Quantidade de ouro do personagem   |  NOT NULL |   -   |
---
### **Sala**
#### Descrição: Entidade que armazena os dados das salas do jogo.
#### Observações: Uma sala pode conter monstros e itens.
| Nome Variável |     Tipo     |         Descrição         | Restrição | Chave |
| :-----------: | :----------: | :-----------------------: | :-------: | :---: |
|    idSala     |     int      | Identificador único da sala |  NOT NULL |  PK   |
|     nomeSala   | varchar[20]   |        Nome da sala         |  NOT NULL |  -   |
|    salaNorte  |     int      | Identificador da sala ao norte  |   NULL  |   -   |
|     salaSul    |     int      | Identificador da sala ao sul   |   NULL   |   -   |
|    salaLeste    |     int      |  Identificador da sala ao leste  |   NULL   |   -   |
|    salaOeste    |     int      |  Identificador da sala ao oeste  |   NULL   |   -   |

---
### **ItemSala**
#### Descrição: Entidade que armazena os itens da sala.
#### Observações: Uma sala pode ter vários itens.
| Nome Variável    |     Tipo     |               Descrição             | Restrição | Chave |
| :--------------: | :----------: | :---------------------------------: | :-------: | :---: |
| idInstanciaSala  |      int      |     Identificador único da instância do item na sala      |  NOT NULL |   PK |
|   quantidadeItem |     int      |    Quantidade de itens na sala     |  NOT NULL |   -   |

---
### **ItemPersonagem**
#### Descrição: Entidade que armazena os itens do personagem.
#### Observações: Um personagem pode ter vários itens.
| Nome Variável     |     Tipo     |               Descrição             | Restrição | Chave |
| :---------------: | :----------: | :---------------------------------: | :-------: | :---: |
| idInstanciaItemPersonagem    |     int      |    Identificador único da instância do item do personagem        |  NOT NULL |  PK   |
|  quantidadeItem    |     int      |    Quantidade de itens do personagem     |  NOT NULL |   -   |

---
### **Item**
#### Descrição: Entidade que armazena os dados dos itens do jogo.
#### Observações: Um item pode ser consumível ou equipável.

| Nome Variável |     Tipo     |          Descrição          | Restrição | Chave |
| :-----------: | :----------: | :-------------------------: | :-------: | :---: |
|    idItem     |     int      |   Identificador único do item  |  NOT NULL |   PK  |
|    nomeItem   | varchar[20]   |         Nome do item           |  NOT NULL |  -   |
|   valorItem    |     int      |         Valor do item         |  NOT NULL |  -   |
|    tipoItem   |     int      | Tipo do item (consumivel = 0, equipavel = 1) |  NOT NULL |  -   |
---
### **Consumivel**
#### Descrição: Entidade que armazena os dados dos itens consumíveis.
#### Observações: Um item consumível é um tipo de item.

| Nome Variável     |     Tipo     |           Descrição           | Restrição | Chave |
| :---------------: | :----------: | :--------------------------: | :-------: | :---: |
|      idItem       |     int      |   Identificador único do item  |  NOT NULL |   FK  |
| incrementoVidaAtual   |     int      |      Incremento de vida atual    |  NOT NULL |  -   |
|incrementoStaminaAtual|     int      |     Incremento de stamina atual   |  NOT NULL |  -   |
---
### **Equipavel**
#### Descrição: Entidade que armazena os dados dos itens equipáveis.
#### Observações: Um item equipável é um tipo de item.

| Nome Variável    |     Tipo     |                Descrição             | Restrição | Chave |
| :--------------: | :----------: | :---------------------------------: | :-------: | :---: |
|     idItem       |     int      | Identificador único do item          |  NOT NULL |   FK  |
| incrementoVidaBase |     int      |     Incremento de vida base        |  NOT NULL |  -   |
| incrementoDefesa  |     int      |      Incremento de defesa           |  NOT NULL |   -  |
|   mulFisico     |   float    | Multiplicador de ataque físico  |  NOT NULL |  -   |
|   mulMagico    |  float   | Multiplicador de ataque mágico  |  NOT NULL |   -  |
|     equipado    |    bool   |   Se o item está equipado      |  NOT NULL |  -   |
---
### **Monstro**
#### Descrição: Entidade que armazena os dados dos monstros.
#### Observações: Um monstro pode ser um minion ou um boss.
| Nome Variável |     Tipo     |            Descrição          | Restrição | Chave |
| :-----------: | :----------: | :---------------------------: | :-------: | :---: |
|   idMonstro   |     int      | Identificador único do monstro|  NOT NULL |   PK  |
|    nomeMonstro| varchar[20]   |       Nome do monstro        |  NOT NULL |  -   |
|   vidaMonstro |     int      |       Vida do monstro         |  NOT NULL |   -  |
|  danoMonstro  |     int      |       Dano do monstro         |  NOT NULL |   -  |
|  defMonstro  |     int      |       Defesa do monstro        |  NOT NULL |  -   |
| tipoMonstro|     bool      |  Tipo do monstro (minion=0, boss=1) |  NOT NULL |   -  |

---
### **InstanciaMonstro**
#### Descrição: Entidade que armazena os dados da instância de um monstro em uma sala.
#### Observações: Uma sala pode ter várias instâncias de monstros.
| Nome Variável        |     Tipo     |                Descrição            | Restrição | Chave |
| :-------------------: | :----------: | :--------------------------------: | :-------: | :---: |
| idInstanciaMonstro  |     int      | Identificador único da instância do monstro|  NOT NULL |  PK   |
|    vidaAtual     |     int      |     Vida atual do monstro         |  NOT NULL |  -   |
|    idSala        |     int      | Identificador da sala onde o monstro está |  NOT NULL |  FK  |
|    idMonstro     |     int      | Identificador do monstro da instância |  NOT NULL |  FK  |


---
### **Minion**
#### Descrição: Entidade que armazena os dados de um monstro do tipo Minion.
#### Observações: Um Minion é um tipo de monstro.
| Nome Variável |     Tipo     |          Descrição         | Restrição | Chave |
| :-----------: | :----------: | :-----------------------: | :-------: | :---: |
|   idMonstro   |     int      |  Identificador único do monstro  |  NOT NULL |  FK   |
| quantidadeOuro |   int      | Quantidade de ouro dropada  |  NOT NULL |   -  |
---
### **Boss**
#### Descrição: Entidade que armazena os dados de um monstro do tipo Boss.
#### Observações: Um Boss é um tipo de monstro.
| Nome Variável |     Tipo     |              Descrição              | Restrição | Chave |
| :-----------: | :----------: | :--------------------------------: | :-------: | :---: |
|   idMonstro   |     int      |  Identificador único do monstro     |  NOT NULL |  FK   |
|   idItem      |     int      | Identificador único do item dropado|  NOT NULL |   FK  |
|   mulBoss    |    int    | Multiplicador de drop de item      |  NOT NULL |   -  |

---
## Histórico de Versões

| Versão |    Data    | Descrição               | Autor                                                                                                                 |
| :----: | :--------: | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [`1.0`](/Modulo_1/DD(Dicinario_de_Dados).md)  | 26/11/2024 | Criação do documento DD | [Henrique ](https://github.com/henriquecq)                          |
| [`1.1`](/Modulo_2/DD(Dicinario_de_Dados)_v1.1.md)  | 29/11/2024 | Melhorias no DD         | [Bruno ](https://github.com/BrunoBReis)                          |
| [`2`](/Modulo_2/DD(Dicinario_de_Dados)_v2.md)  | 14/01/2025 | Aplica novas ideias DD         |  [Henrique ](https://github.com/henriquecq)                         |

