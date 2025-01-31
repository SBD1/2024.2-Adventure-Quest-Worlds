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
#### Observações: Um personagem escolhe uma classe, está em uma sala, tem um inventário e pode matar nenhuma ou várias Instâncias de Monstros, alem de poder ter um ou nenhum item equipado.

| Nome Variável       |     Tipo     |                Descrição             | Restrição | Chave |
| :------------------: | :----------: | :---------------------------------: | :-------: | :---: |
|    idPersonagem     |     int      |    Identificador único do personagem  |  NOT NULL |   PK  |
|      idSala        |     int      |    Identificador da sala onde o personagem está |  NOT NULL |   FK  |
|       idClasse      |     int      |    Identificador da classe do personagem |  NOT NULL |   FK  |
|      nomePersonagem   | varchar[20]   | Nome do personagem                  |  NOT NULL |   -   |
| nivel                  | int         | Nível atual do personagem                    | NOT NULL  | -     |
| xpAtual                | int         | XP atual do personagem                       | NOT NULL  | -     |
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
#### Observações: Uma classe pode ter uma ou várias habilidades.

| Nome Variável |     Tipo     |          Descrição         | Restrição | Chave |
| :-----------: | :----------: | :------------------------: | :-------: | :---: |
|   idClasse    |     int      | Identificador único da classe |  NOT NULL |  PK   |
|       idHabilidade |     int      | Identificador da habilidade da classe |  NOT NULL |   FK  |
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
#### Observações: Uma sala pode conter monstros, itens e o personagem.
| Nome Variável |     Tipo     |         Descrição         | Restrição | Chave |
| :-----------: | :----------: | :-----------------------: | :-------: | :---: |
|    idSala     |     int      | Identificador único da sala |  NOT NULL |  PK   |
|    idRegiao   |     int      | Identificador da região da sala |  NOT NULL |  FK   |
|     nomeSala   | varchar[20]   |        Nome da sala         |  NOT NULL |  -   |
|    salaNorte  |     int      | Identificador da sala ao norte  |   NULL  |   -   |
|     salaSul    |     int      | Identificador da sala ao sul   |   NULL   |   -   |
|    salaLeste    |     int      |  Identificador da sala ao leste  |   NULL   |   -   |
|    salaOeste    |     int      |  Identificador da sala ao oeste  |   NULL   |   -   |
---

### **Regiao**
#### Descrição: Entidade que armazena os dados das regiões do jogo.
#### Observações: Uma região pode ter uma ou várias salas.
| Nome Variável |     Tipo     |         Descrição         | Restrição | Chave |
| :-----------: | :----------: | :-----------------------: | :-------: | :---: |
|   idRegiao    |     int      | Identificador único da região |  NOT NULL |  PK   |
|  nomeRegiao   | varchar[20]   |        Nome da região       |  NOT NULL |  -   |
|   descricaoRegiao | varchar[200] | Descrição da região         |  NOT NULL |  -   |

---
### **IntanciaItem**
#### Descrição: Entidade que armazena os dados da instância de um item.
#### Observações: Um inventário pode ter vários itens, um item se for equipavel pode estar ou nao equipado.
| Nome Variável     |     Tipo     |               Descrição             | Restrição | Chave |
| :---------------: | :----------: | :---------------------------------: | :-------: | :---: |
| idInstanciaItem    |     int      |    Identificador único da instância do item        |  NOT NULL |  PK   |
|  idItem         |     int      |    Identificador do item da instância |  NOT NULL |  FK  |
|  quantidadeItem    |     int      |    Quantidade de itens do personagem     |  NOT NULL |   -   |
|  equipado    |    bool     |    Se o item está equipado      |  NOT NULL |   -   |

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
| qntXP| int | Quantidade de Xp q o monstro da ao ser morto| NOT NULL| -|

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
| fraseBoss| varchar[200] | Frase do boss ao ser derrotado | NOT NULL | - |

---

### **Missao**
#### Descrição: Entidade que armazena as missões do jogo.
#### Observações: As missões seguem uma ordem sequencial e têm objetivos variados.
| Nome Variável |     Tipo     |            Descrição          | Restrição | Chave |
| :-----------: | :----------: | :--------------------------: | :-------: | :---: |
|   idMissao   |     int      | Identificador único da missão |  NOT NULL |   PK  |
|   nomeMissao  | varchar(50)  | Nome da missão               |  NOT NULL |   -   |
| descricaoMissao | varchar(200) | Descrição da missão         |  NOT NULL |   -   |
| xpRecompensa  |     int      | XP dado ao completar a missão |  NOT NULL |   -   |
| idItemRecompensa | int      | ID do item dado como recompensa (opcional) |   NULL   |   FK  |
| idMissaoAnterior | int      | Identificador da missão anterior (NULL se for a primeira) |   NULL   |   FK  |

---

### **ProgressoMissao**
#### Descrição: Relaciona personagens com as missões que estão realizando.
| Nome Variável |     Tipo     |                Descrição            | Restrição | Chave |
| :-----------: | :----------: | :-------------------------------: | :-------: | :---: |
| idPersonagem |     int      | Identificador do personagem       |  NOT NULL |   FK  |
| idObjetivoMissao     |     int      | Identificador do objetivo da missao           |  NOT NULL |   FK  |
| concluida    |    bool     | Indica se a missão foi concluída  |  NOT NULL |   -   |
| progressoOjetivo | int | Progresso do objetivo | NOT NULL | - |

---

### **ObjetivoMissao**
#### Descrição: Armazena os objetivos das missões.
#### Observações: Uma missão pode ter vários objetivos.
| Nome Variável |     Tipo     |           Descrição           | Restrição | Chave |
| :-----------: | :----------: | :---------------------------: | :-------: | :---: |
|   idObjetivo  |     int      | Identificador único do objetivo |  NOT NULL |   PK  |
|   idMissao   |     int      | Identificador da missão         |  NOT NULL |   FK  |
| descricaoObjetivo | varchar(200) | Descrição do objetivo   |  NOT NULL |   -   |
| tipoObjetivo  | int | Tipo do objetivo (1=derrotar monstros, 2=alcançar região, 3=percorrer salas) |  NOT NULL |   -   |
| quantidadeMeta | int | Quantidade a ser atingida | NOT NULL | - |
| idReferencia | int | ID da entidade a ser referenciada (Monstro, Região, Sala) | NOT NULL | - |
| tipoReferencia | int | Tipo da entidade referenciada (Monstro=1, Região=2, Sala=3) | NOT NULL | - |


## Histórico de Versões

| Versão |    Data    | Descrição               | Autor                                                                                                                 |
| :----: | :--------: | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [`1.0`](/Modulo_1/DD(Dicinario_de_Dados).md)  | 26/11/2024 | Criação do documento DD | [Henrique ](https://github.com/henriquecq)                          |
| [`2`](/Modulo_2/DD(Dicinario_de_Dados)_v2.md)  | 29/11/2024 | Melhorias no DD         | [Bruno ](https://github.com/BrunoBReis)                          |
| [`2.1`](/Modulo_2/DD(Dicinario_de_Dados)_v2.1.md)  | 14/01/2025 | Aplica novas ideias DD         |  [Henrique ](https://github.com/henriquecq)                         |
| [`3`](/Modulo_3/DD(Dicinario_de_Dados)_v3.md)  | 27/01/2025 | Correção baseada nas novas features | [Henrique ](https://github.com/henriquecq)                         |

