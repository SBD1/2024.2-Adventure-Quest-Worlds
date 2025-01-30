# ME-R (Modelo Entidade-Relacionamento)

## Entidades

* Usuario
* Monstro
* InstanciaMonstro
* Minion
* Boss
* Save
* Classe
* Personagem
* Habilidade
* Inventario
* ItemPersonagem
* Sala
* ItemSala
* Item
* Consumivel
* Equipavel
* Missao
* ObjetivoMissao
* ProgressoMissao
* RecompensaMissao

## Atributos

- **Usuario:** idUsuario, login, senha, qtdPersonagem  
- **Monstro:** idMonstro, tipoMonstro  
- **InstanciaMonstro:** idInstanciaMonstro, idMonstro, vidaAtual, idSala  
- **Minion:** idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, quantidadeOuro  
- **Boss:** idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, mulBoss, idItem  
- **Save:** idUsuario, idPersonagem  
- **Classe:** idClasse, nomeClasse, mulFisico, mulMagico  
- **Personagem:** idPersonagem, nomePersonagem, staminaAtualPersonagem, vidaAtualPersonagem, staminaBasePersonagem, vidaBasePersonagem, defensePersonagem, ataqueFisico, ataqueMagico, idSala, xp, nivel  
- **Habilidade:** idHabilidade, nomeHabilidade, danoFisico, danoMagico, custoStamina, custoCooldown, idClasse  
- **Inventario:** idInventario, espacoDisponivel, capacidade, quantidadeOuro, idPersonagem  
- **ItemPersonagem:** idItem, idItemPersonagem, idInventario, quantidadeItem  
- **Sala:** idSala, nomeSala, salaNorte, salaSul, salaLeste, salaOeste  
- **ItemSala:** idItem, idItemSala, idSala, quantidadeItem  
- **Item:** idItem, tipoItem, raridade  
- **Consumivel:** idItem, nomeItem, valorItem, incrementoVidaAtual, incrementoStaminaAtual  
- **Equipavel:** idItem, nomeItem, valorItem, incrementoVidaBase, incrementoDefesa, mulFisico, mulMagico, equipado ('s' ou 'n')  
- **Missao:** idMissao, nomeMissao, descricao, idMissaoAnterior  
- **ObjetivoMissao:** idObjetivo, descricaoObjetivo, tipoObjetivo, quantidadeRequerida, idMissao  
- **ProgressoMissao:** idPersonagem, idMissao, idObjetivo, quantidadeAtual, status  
- **RecompensaMissao:** idRecompensa, idMissao, tipoRecompensa, valorRecompensa, idItem 

## Relacionamentos

**Usuario possui save:**  
- Um Usuário pode ter de 0 a 3 saves.
- Um Save deve pertencer a um único Usuário.
- Cardinalidade: (0:3) (1:1)   

**Personagem corresponde ao save:**  
- Um Personagem corresponde a um único Save.
- Um Save corresponde a um único Personagem.
- Cardinalidade: (1:1) (1:1)  

**Personagem escolhe classe:**  
- Um Personagem deve ter uma única Classe.
- Uma Classe pode ter vários Personagens.
- Cardinalidade: (1:1) (1:N)  

**Classe tem Habilidade:**  
- Uma Classe pode ter várias Habilidades.
- Uma Habilidade pertence a uma única Classe.
- Cardinalidade: (1:N) (1:1)  

**Personagem está em uma Sala:**  
- Um Personagem deve estar em uma única Sala.
- Uma Sala pode conter nenhum ou um Personagem.
- Cardinalidade: (1:1) (0:1)  

**Sala possui ItemSala:**  
- Uma Sala pode ter nenhum ou vários ItemSala.
- Um ItemSala deve estar em uma única Sala.
- Cardinalidade: (0:N) (1:1)  

**ItemSala possui Item:**  
- Um ItemSala deve possuir exatamente um Item.
- Um Item pode estar em nenhum ou vários ItemSala.
- Cardinalidade: (1:1) (0:N)  

**Personagem possui Inventário:**  
- Um Personagem tem um único Inventário.
- Um Inventário pertence a um único Personagem.
- Cardinalidade: (1:1) (1:1)  

**Inventário guarda o ItemPersonagem:**  
- Um Inventário pode ter nenhum ou vários ItemPersonagem.
- Um ItemPersonagem deve estar em um único Inventário.
- Cardinalidade: (0:N) (1:1)  

**ItemPersonagem possui Item:**  
- Um ItemPersonagem deve possuir exatamente um Item.
- Um Item pode conter nenhum ou vários ItemPersonagem.
- Cardinalidade: (1:1) (0:N)  

**Personagem mata InstanciaMonstro:**  
- Um Personagem pode matar nenhum ou várias InstanciaMonstro.
- Uma InstanciaMonstro é morta por apenas um Personagem.
- Cardinalidade: (0:N) (1:1)  

**Monstro possui InstanciaMonstro:**  
- Um Monstro pode ter nenhuma ou várias InstanciaMonstro.
- Uma InstanciaMonstro deve pertencer a um único Monstro.
- Cardinalidade: (0:N) (1:1)  

**InstanciaMonstro cria ItemPersonagem:**  
- Uma InstanciaMonstro pode criar nenhum ou um ItemPersonagem.
- Um ItemPersonagem pode ser criado por nenhuma ou uma InstanciaMonstro.
- Cardinalidade: (0:1) (0:1)  

**InstanciaMonstro está em uma Sala:**  
- Uma InstanciaMonstro deve estar em uma única Sala.
- Uma Sala pode conter nenhuma ou várias InstanciaMonstro.
- Cardinalidade: (1:1) (0:N)  

**Item possui exclusivamente tipos:**  
- Um Item pode ser classificado apenas como Consumível ou Equipável.  

**Monstro possui exclusivamente tipos:**  
- Um Monstro pode ser classificado apenas como Minion ou Boss.  

**Missão possui ObjetivoMissao:**  
- Uma Missão pode ter um ou vários ObjetivoMissao.
- Um ObjetivoMissao pertence a uma única Missão.
- Cardinalidade: (1:N) (1:1)  

**Personagem tem ProgressoMissao:**  
- Um Personagem pode ter progresso em várias Missões.
- Um ProgressoMissao pertence a um único Personagem.
- Cardinalidade: (0:N) (1:1)  

**Missão concede RecompensaMissao:**  
- Uma Missão pode conceder uma ou várias RecompensaMissao.
- Uma RecompensaMissao pertence a uma única Missão.
- Cardinalidade: (1:N) (1:1)  

**RecompensaMissao pode incluir Item:**  
- Uma RecompensaMissao pode conceder nenhum ou um Item.
- Um Item pode ser concedido por nenhuma ou uma RecompensaMissao.
- Cardinalidade: (0:1) (0:1)

---

## Histórico de Versões
| Versão |    Data    | Descrição               | Autor                                                                                                                 |
| :----: | :--------: | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [`1.0`](/Modulo_1/ME-R(Modelo_Entidade_Relacionamento).md)  | 26/11/2024 | Criação do documento ME-R | Todos                       |
| [`2.0`](/Modulo_2/ME-R(Modelo_Entidade_Relacionamento)_v2.md)  | 30/11/2024 | Adição de atributos e relacionamentos | Todos                       |
| [`2.1`](/Modulo_2/ME-R(Modelo_Entidade_Relacionamento)_v2.1.md)  | 14/01/2025 | Adição de atributos e relacionamentos | Todos                       |
| [`3.0`](/Modulo_3/ME-R(Modelo_Entidade_Relacionamento)_v3.md)  | 27/01/2025 | Correção baseada nas novas features | [Henrique ](https://github.com/henriquecq)                         |

