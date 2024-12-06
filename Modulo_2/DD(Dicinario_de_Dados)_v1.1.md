# Dicionário de Dados

---

### **Player**
#### Descrição: Player é a uma entidade que descreve as caracterísitcas de todo o player dentro do jogo
#### Observações: Player possui a chave estrangeira: `idSala`

| Nome Variável |     Tipo     |           Descrição           | Restrição |   Chave   |
| :-----------: | :----------: | :--------------------------: | :-------: | :-----: |
|   idJogador   |     int      | Identificador único do jogador |     NOT NULL     |    PK    |
|    idSala     |     int      | Sala atual onde o jogador está |     NOT NULL     |    FK    |
|     nome      | varchar[30]   |        Nome do jogador         |     NOT NULL     |    -    |
|      hp       |     int      |    Pontos de vida do jogador   |     NOT NULL     |    -    |
|     mana      |     int      |    Pontos de mana do jogador   |     NOT NULL     |    -    |
|      def      |     int      |       Defesa do jogador        |     NOT NULL     |    -    |
|      atk      |     int      |  Ataque físico do jogador      |     NOT NULL     |    -    |
|     atkmg     |     int      |  Ataque mágico do jogador      |     NOT NULL     |    -    |
|     ouro      |     int      | Quantidade de ouro do jogador  |     NOT NULL     |    -    |
|   armadura    |     int      | Equipamento de defesa do jogador |   NULL     |    -    |
|     arma      |     int      | Equipamento de ataque do jogador |   NULL     |    -    |
|   insignia    |     int      |     Item especial do jogador   |     NULL     |    -    |



---

### **Classe**
#### Descrição: Classe é uma entidade que descreve as características base das diferentes classes disponíveis no jogo.

| Nome Variável |     Tipo     |           Descrição           | Restrição | Chave |
| :-----------: | :----------: | :--------------------------: | :-------: | :---: |
|   idClasse    |     int      | Identificador único da classe |     NOT NULL     |   PK   |
|     mana      |     int      |    Pontos de mana base da classe |   NOT NULL     |   -   |
|      def      |     int      |     Defesa base da classe     |     NOT NULL     |   -   |
|      atk      |     int      |  Ataque físico base da classe |     NOT NULL     |   -   |
|     atkmg     |     int      |  Ataque mágico base da classe |     NOT NULL     |   -   |


---

### **Loja**
#### Descrição: Loja é uma entidade que descreve as características das lojas disponíveis no jogo, incluindo sua localização e identificação única.

#### Observações: Loja possui as chaves estrangeiras: `idSala` e `idAndar`.

| Nome Variável |     Tipo     |               Descrição              | Restrição | Chave |
| :-----------: | :----------: | :---------------------------------: | :-------: | :---: |
|    idLoja     |     int      |   Identificador único da loja        |     NOT NULL     |   PK   |
|    idSala     |     int      | Sala onde a loja está localizada     |     NOT NULL     |   FK   |
|   idAndar     |     int      | Andar onde a loja está localizada    |     NOT NULL     |   FK   |
|     nome      | varchar[30]   |            Nome da loja              |     NOT NULL     |   -   |


---

### **EstoqueItem**
#### Descrição: EstoqueItem é uma entidade que descreve os itens disponíveis em estoque nas lojas, incluindo o preço e a quantidade disponível.

#### Observações: EstoqueItem possui as chaves estrangeiras: `idItem` e `idLoja`.

| Nome Variável |     Tipo     |             Descrição            | Restrição | Chave |
| :-----------: | :----------: | :-----------------------------: | :-------: | :---: |
|    idItem     |     int      |   Identificador único do item    |     NOT NULL     |   FK   |
|    idLoja     |     int      | Loja onde o item está disponível |     NOT NULL     |   FK   |
|     preço     |     int      |          Preço do item           |     NOT NULL     |   -   |
|  quantidade   |     int      | Quantidade disponível no estoque |     NOT NULL     |   -   |

---

### **Habilidade**
#### Descrição: Habilidade é uma entidade que descreve as características das habilidades disponíveis no jogo, incluindo seu custo de mana, dano, tempo de recarga e tipo de dano.

#### Observações: Habilidade possui a chave estrangeira: `idClasse`.

| Nome Variável  |     Tipo     |               Descrição               | Restrição | Chave |
| :------------: | :----------: | :----------------------------------: | :-------: | :---: |
|  idHabilidade  |     int      | Identificador único da habilidade     |     NOT NULL     |   PK   |
|    idClasse    |     int      |   Classe que possui essa habilidade   |     NOT NULL     |   FK   |
|      nome      | varchar[30]   |           Nome da habilidade          |    NOT NULL     |   -   |
|  custoDeMana   |     int      | Custo de mana para usar a habilidade  |     NOT NULL     |   -   |
|      dano      |     int      |       Dano causado pela habilidade    |     NOT NULL     |   -   |
|    cooldown    |     int      |     Tempo de recarga da habilidade    |     NOT NULL     |   -   |
|   tipodedano   | bool   | Tipo de dano da habilidade (físico '0'/ mágico '1') |   NOT NULL     |   -   |

---

### **Inventário**
#### Descrição: Inventário é uma entidade que descreve os itens armazenados por um jogador, incluindo espaço disponível e a possibilidade de os itens serem equipáveis.

#### Observações: Inventário possui as chaves estrangeiras: `idJogador` e `idInstanciaItem`.

| Nome Variável     |     Tipo     |             Descrição             | Restrição | Chave |
| :---------------: | :----------: | :-------------------------------: | :-------: | :---: |
|    idJogador      |     int      |       Jogador dono do inventário   |     NOT NULL     |   FK   |
|  idInstanciaItem  |     int      |      Item associado ao inventário  |     NOT NULL     |   FK   |
|      espaço       |     int      |     Espaço disponível no inventário |     NOT NULL     |   -   |
|     equipavel     |     bool     |    Indica se o item é equipável (nao equipavel '0' / equipavel '1')    |     NOT NULL     |   -   |


---

### **Andar**
#### Descrição: Andar é uma entidade que descreve os andares disponíveis no jogo, incluindo sua identificação única e nome.

| Nome Variável |     Tipo     |           Descrição           | Restrição | Chave |
| :-----------: | :----------: | :--------------------------: | :-------: | :---: |
|    idAndar    |     int      | Identificador único do andar  |     NOT NULL     |   PK   |
|     nome      | varchar[30]   |           Nome do andar        |     NOT NULL     |   -   |

---

### **Sala**
#### Descrição: Sala é uma entidade que descreve as salas disponíveis no jogo, incluindo sua identificação única, localização no andar e uma descrição detalhada.

#### Observações: Sala possui a chave estrangeira: `idAndar`.

| Nome Variável |     Tipo     |           Descrição           | Restrição | Chave |
| :-----------: | :----------: | :--------------------------: | :-------: | :---: |
|    idSala     |     int      | Identificador único da sala   |  NOT NULL |   PK   |
|    idAndar    |     int      |     Andar onde a sala está    |  NOT NULL |   FK   |
|   descrição   | varchar[200]   |        Descrição da sala      |  NOT NULL |   -   |


---

### **Item**
#### Descrição: Item é uma entidade que descreve os itens disponíveis no jogo, incluindo suas características básicas como nome, custo em ouro e se são equipáveis.

| Nome Variável  |     Tipo     |             Descrição             | Restrição | Chave |
| :------------: | :----------: | :-------------------------------: | :-------: | :---: |
|     idItem     |     int      |     Identificador único do item    |  NOT NULL |   PK   |
|  nomeDoItem    | varchar[30]   |            Nome do item            |  NOT NULL |   -   |
|  custoDeOuro   |     int      |       Custo do item em ouro        |  NOT NULL |   -   |
|   equipavel    |     bool     |      Indica se o item é equipável (nao equipavel '0' / equipavel '1')   |  NOT NULL |   -   |


---

### **Instância do Item**
#### Descrição: Instância do Item é uma entidade que descreve cada instância única de um item no jogo, associando-a ao item correspondente.

#### Observações: Instância do Item possui a chave estrangeira: `idItem`.

| Nome Variável     |     Tipo     |                  Descrição                  | Restrição | Chave |
| :---------------: | :----------: | :----------------------------------------: | :-------: | :---: |
|  idInstanciaItem  |     int      | Identificador único da instância do item   |  NOT NULL |   PK   |
|      idItem       |     int      |         Item associado à instância         |  NOT NULL |   FK   |



---

### **Consumível**
#### Descrição: Consumível é uma entidade que descreve os itens consumíveis no jogo, detalhando os pontos de HP ou mana que podem ser restaurados ao utilizá-los.

#### Observações: Consumível possui a chave estrangeira: `idItem`.

| Nome Variável |     Tipo     |           Descrição           | Restrição | Chave |
| :-----------: | :----------: | :--------------------------: | :-------: | :---: |
|    idItem     |     int      |   Identificador único do item |  NOT NULL |   FK   |
|    maisHp     |     int      |    Pontos de HP restaurados   |  NULL |   -   |
|   maisMana    |     int      |   Pontos de mana restaurados  |  NULL |   -   |


---

### **Equipável**
#### Descrição: Equipável é uma entidade que descreve os itens equipáveis no jogo, especificando os atributos que podem ser melhorados, como defesa, ataque físico, ataque mágico e mana, além do tipo de equipamento.

#### Observações: Equipável possui a chave estrangeira: `idItem`.

| Nome Variável |     Tipo     |               Descrição               | Restrição | Chave |
| :-----------: | :----------: | :----------------------------------: | :-------: | :---: |
|    idItem     |     int      |   Identificador único do item         |  NOT NULL |   FK   |
|     tipo      | bool   | Tipo de equipamento (armadura '0' / arma(weapon)'1')  |  NOT NULL |   -   |
|    maisDef    |     int      |         Aumento de defesa             |  NULL |   -   |
|    maisAtk    |     int      |    Aumento de ataque físico           |  NULL |   -   |
|   maisAtkmg   |     int      |    Aumento de ataque mágico           |  NULL |   -   |
|   maisMana    |     int      |          Aumento de mana              |  NULL |   -   |


---

### **Monstro**
#### Descrição: Monstro é uma entidade que descreve as características dos monstros no jogo, incluindo seus atributos como pontos de vida, defesa, ataque físico, ataque mágico, recompensa em ouro e seu tipo (Minion ou Boss).

| Nome Variável |     Tipo     |              Descrição              | Restrição | Chave |
| :-----------: | :----------: | :--------------------------------: | :-------: | :---: |
|   idMonstro   |     int      |  Identificador único do monstro     |  NOT NULL |   PK   |
|      hp       |     int      |      Pontos de vida do monstro      |  NOT NULL |   -   |
|      def      |     int      |           Defesa do monstro         |  NOT NULL |   -   |
|      atk      |     int      |        Ataque físico do monstro     |  NOT NULL |   -   |
|     atkmg     |     int      |        Ataque mágico do monstro     |  NOT NULL |   -   |
|    qntdOuro   |     int      | Quantidade de ouro ao ser derrotado |  NOT NULL |   -   |
|     tipo      | bool   |    Tipo de monstro (Minion '0' / Boss '1')    |  NOT NULL |   -   |



---


### **Instância do Monstro**
#### Descrição: Instância do Monstro é uma entidade que descreve as ocorrências únicas de monstros no jogo, incluindo a quantidade de instâncias presentes.

#### Observações: Instância do Monstro possui a chave estrangeira: `idMonstro`.

| Nome Variável |     Tipo     |                Descrição               | Restrição | Chave |
| :-----------: | :----------: | :-----------------------------------: | :-------: | :---: |
|   idMonstro   |     int      |    Identificador único do monstro      |  NOT NULL |   FK   |
|  quantidade   |     int      | Quantidade de instâncias do monstro    |  NOT NULL |   -   |


---

### **Minion**
#### Descrição: Minion é uma entidade que representa um tipo específico de monstro no jogo, identificado de forma única.

#### Observações: Minion possui a chave estrangeira: `idMonstro`.

| Nome Variável | Tipo |              Descrição              | Restrição | Chave |
| :-----------: | :--: | :--------------------------------: | :-------: | :---: |
|   idMonstro   | int  |  Identificador único do monstro     |  NOT NULL |   FK   |


---

### **Boss**
#### Descrição: Boss é uma entidade que representa os chefes no jogo, detalhando seu item de recompensa (drop) e uma descrição única.

#### Observações: Boss possui as chaves estrangeiras: `idMonstro` e `idItem`.

| Nome Variável |     Tipo     |           Descrição           | Restrição | Chave |
| :-----------: | :----------: | :--------------------------: | :-------: | :---: |
|   idMonstro   |     int      |  Identificador único do monstro |  NOT NULL |   FK   |
|    idItem     |     int      |      Item dropado pelo boss    |  NOT NULL |   FK   |
|   descrição   | varchar[200]   |       Descrição do boss        |  NOT NULL |   -   |


--- 


## 
| Versão |    Data    | Descrição               | Autor                                                                                                                 |
| :----: | :--------: | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [`1.0`](/Modulo_1/DD(Dicinario_de_Dados).md)  | 26/11/2024 | Criação do documento DD | [Henrique ](https://github.com/henriquecq)                          |
| [`1.1`](/Modulo_2/DD(Dicinario_de_Dados)_v1.1.md)  | 29/11/2024 | Melhorias no DD         | [Bruno ](https://github.com/BrunoBReis)                          |

