## Dicionário de Dados

---

### **Usuário**
#### Descrição: Entidade que armazena os dados de login dos jogadores.
#### Observações: Um usuário pode até 3 saves.
| Nome Variável |     Tipo     |             Descrição           | Restrição | Chave |
| :-----------: | :----------: | :-----------------------------: | :-------: | :---: |
|   idUsuario   |     int      | Identificador único do usuário |  NOT NULL |   PK  |
|      login    | varchar[50]   |  Nome de usuário para login      |  NOT NULL |   -   |
|     senha     | varchar[50]   | Senha do usuário             |  NOT NULL |   -   |
| qtdPersonagem |     int     | Número de personagens do usuário entre 0 e 3 |  NOT NULL |   -   |

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
|      nomePersonagem   | varchar[50]   | Nome do personagem                  |  NOT NULL |   -   |
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
|  nomeClasse   | varchar[50]   |        Nome da classe        |  NOT NULL |  -   |
|    mulFisico  |    decimal    | Multiplicador de ataque físico |  NOT NULL |  -   |
|   mulMagico   |    decimal    |  Multiplicador de ataque mágico |  NOT NULL |  -   |
---
### **Habilidade**
#### Descrição: Entidade que armazena os dados das habilidades dos personagens.
#### Observações: Uma habilidade pertence a uma classe.

| Nome Variável   |     Tipo     |             Descrição            | Restrição | Chave |
| :--------------: | :----------: | :-----------------------------: | :-------: | :---: |
|   idHabilidade  |     int      |  Identificador único da habilidade |  NOT NULL |   PK  |
|  nomeHabilidade | varchar[50]   |       Nome da habilidade         |  NOT NULL |  -   |
|     danoFisico    |     int      |       Dano físico da habilidade     |  NOT NULL |  -   |
|    danoMagico    |     int      |      Dano mágico da habilidade     |  NOT NULL |  -   |
|   custoStamina   |     int      | Custo de stamina da habilidade   |  NOT NULL |  -   |
|  custoCooldown  |     int      |  Cooldown da habilidade         |  NOT NULL |   -  |
|   idClasse      |     int      |  Identificador da classe da habilidade |  NOT NULL |  FK  |

---
### **Inventario**
#### Descrição: Entidade que armazena os itens do personagem.
#### Observações: Um inventário pertence a um personagem.

| Nome Variável  |     Tipo     |         Descrição        | Restrição | Chave |
| :-------------: | :----------: | :---------------------: | :-------: | :---: |
|   idPersonagem |     int      | Identificador do personagem dono do inventário | NOT NULL|   FK |
|espacoDisponivel |     int      | Espaço disponível no inventário |  NOT NULL |   -   |
|   capacidade   |     int      |  Capacidade do inventário   |  NOT NULL |   -   |
| quantidadeOuro      |     int      | Quantidade de ouro do personagem     |  NOT NULL |   -   |
---
### **Sala**
#### Descrição: Entidade que armazena os dados das salas do jogo.
#### Observações: Uma sala pode conter monstros, itens e o personagem.
| Nome Variável |     Tipo     |         Descrição         | Restrição | Chave |
| :-----------: | :----------: | :-----------------------: | :-------: | :---: |
|    idSala     |     int      | Identificador único da sala |  NOT NULL |  PK   |
|    idRegiao   |     int      | Identificador da região da sala |  NOT NULL |  FK   |
|     nomeSala   | varchar[50]   |        Nome da sala         |  NOT NULL |  -   |
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
|  nomeRegiao   | varchar[50]   |        Nome da região       |  NOT NULL |  -   |
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
|  idSala       |     int      |    Identificador da sala onde o item está |  NOT NULL |  FK  |
|  idPersonagem |     int      |    Identificador do personagem dono do item |  NOT NULL |  FK  |

---
### **Item**
#### Descrição: Entidade que armazena os dados dos itens do jogo.
#### Observações: Um item pode ser consumível ou equipável.

| Nome Variável |     Tipo     |          Descrição          | Restrição | Chave |
| :-----------: | :----------: | :-------------------------: | :-------: | :---: |
|    idItem     |     int      |   Identificador único do item  |  NOT NULL |   PK  |
|    nomeItem   | varchar[50]   |         Nome do item           |  NOT NULL |  -   |
|   precoItem    |     int      |         Valor do item         |  NOT NULL |  -   |
|    tipoItem   |     int      | Tipo do item (consumivel = 0, equipavel = 1) |  NOT NULL |  -   |
|    raridade   |     int      | Raridade do item reflete nivel Personagem |  NOT NULL |  -   |
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
|    nomeMonstro| varchar[50]   |       Nome do monstro        |  NOT NULL |  -   |
|   vidaMonstro |     int      |       Vida do monstro         |  NOT NULL |   -  |
|  danoMonstro  |     int      |       Dano do monstro         |  NOT NULL |   -  |
|  defMonstro  |     int      |       Defesa do monstro        |  NOT NULL |  -   |
| tipoMonstro|     bool      |  Tipo do monstro (minion=0, boss=1) |  NOT NULL |   -  |
| idRegiao| int | Região do monstro | NOT NULL | FK |
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
|   mulBoss    |    decimal    | Multiplicador de stats        |  NOT NULL |   -  |
| fraseBoss| varchar[200] | Frase do boss ao ser derrotado | NOT NULL | - |

---

### **Missao**
#### Descrição: Entidade que armazena as missões do jogo.
#### Observações: As missões seguem uma ordem sequencial e têm objetivos variados.
| Nome Variável |     Tipo     |            Descrição          | Restrição | Chave |
| :-----------: | :----------: | :--------------------------: | :-------: | :---: |
|   idMissao   |     int      | Identificador único da missão |  NOT NULL |   PK  |
|   nomeMissao  | varchar[50]  | Nome da missão               |  NOT NULL |   -   |
| descricaoMissao | varchar[200] | Descrição da missão         |  NOT NULL |   -   |
| xpRecompensa  |     int      | XP dado ao completar a missão |  NOT NULL |   -   |
| idItemRecompensa | int      | ID do item dado como recompensa (opcional) |   NULL   |   FK  |
| idMissaoSeguinte | int      | ID da missão seguinte (opcional) |   NULL   |   FK  |
| quantidadeOuro | int | Quantidade de ouro dada como recompensa | NOT NULL | - |

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
| descricaoObjetivo | varchar[200] | Descrição do objetivo   |  NOT NULL |   -   |
| quantidadeMeta |     int      | Quantidade necessária para completar o objetivo |  NOT NULL |   -   |
| idInstanciaMonstro | int | ID da instância do monstro a ser morto | NOT NULL | FK |
| idSala | int | ID da sala onde o monstro está | NOT NULL | FK |

### **Loja**
#### Descrição: Entidade que armazena os dados das lojas do jogo.
#### Observações: Uma loja está em uma sala e pode ter vários itens.
| Nome Variável |     Tipo     |         Descrição         | Restrição | Chave |
| :-----------: | :----------: | :-----------------------: | :-------: | :---: |
|    idLoja     |     int      | Identificador único da loja |  NOT NULL |  PK   |
|    idSala     |     int      | Identificador da sala onde a loja está |  NOT NULL |  FK   |
|   nomeLoja    | varchar[50]   |        Nome da loja         |  NOT NULL |  -   |

### **Catalogo**
#### Descrição: Entidade que armazena os itens disponíveis nas lojas.
#### Observações: Uma loja pode ter vários itens.
| Nome Variável        |     Tipo     |                Descrição            | Restrição | Chave |
| :-------------------: | :----------: | :--------------------------------: | :-------: | :---: |
|   IdLoja             |     int      | Identificador único da loja         |  NOT NULL |  FK   |
|   IdItem             |     int      | Identificador único do item         |  NOT NULL |  FK   |

## Histórico de Versões

| Versão |    Data    | Descrição               | Autor                                                                                                                 |
| :----: | :--------: | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [`1.0`](/Modulo_1/DD(Dicinario_de_Dados).md)  | 26/11/5024 | Criação do documento DD | [Henrique ](https://github.com/henriquecq)                          |
| [`2`](/Modulo_2/DD(Dicinario_de_Dados)_v2.md)  | 29/11/5024 | Melhorias no DD         | [Bruno ](https://github.com/BrunoBReis)                          |
| [`2.1`](/Modulo_2/DD(Dicinario_de_Dados)_v2.1.md)  | 14/01/5025 | Aplica novas ideias DD         |  [Henrique ](https://github.com/henriquecq)                         |
| [`3`](/Modulo_3/DD(Dicinario_de_Dados)_v3.md)  | 27/01/5025 | Correção baseada nas novas features | [Henrique ](https://github.com/henriquecq)                         |
| [`3.1`](/Modulo_3/DD(Dicinario_de_Dados)_v3.md)  | 01/02/5025 | Novas features | [Henrique ](https://github.com/henriquecq)                         |

