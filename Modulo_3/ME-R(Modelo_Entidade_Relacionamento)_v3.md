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
* Sala
* Regiao
* Item
* Consumivel
* Equipavel
* Missao
* ObjetivoMissao
* ProgressoMissao
* Loja
* InstanciaItem
* Catalogo

## Atributos

- **Usuario:** idUsuario, login, senha, qtdPersonagem 
- **Monstro:** idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, tipoMonstro, qntXp, idRegiao
- **InstanciaMonstro:** idInstanciaMonstro, idMonstro, vidaAtual, idSala
- **Minion:** idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, quantidadeOuro, qntXp, idRegiao 
- **Boss:** idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, mulBoss, idItem, fraseBoss, qntXp,id Regiao  
- **Save:** idUsuario, idPersonagem  
- **Classe:** idClasse, nomeClasse, mulFisico, mulMagico  
- **Personagem:** idPersonagem, nomePersonagem, staminaAtualPersonagem, vidaAtualPersonagem, staminaBasePersonagem, vidaBasePersonagem, defensePersonagem, ataqueFisico, ataqueMagico, idSala, xp, nivel, idClasse
- **Habilidade:** idHabilidade, nomeHabilidade, danoFisico, danoMagico, custoStamina, custoCooldown, idClasse  
- **Inventario:** idPersonagem, espacoDisponivel, capacidade, quantidadeOuro
- **IntanciaItem:** idInstaciaItem, idItem, idItemSala, quantidadeItem, equipado
- **Sala:** idSala, nomeSala, salaNorte, salaSul, salaLeste, salaOeste, idRegiao
- **Regiao:** idRegiao, nomeRegiao, descricaoRegiao
- **Item:** idItem, nomeItem, precoItem, tipoItem, raridade
- **Consumivel:** idItem, nomeItem, precoItem, raridade, incrementoVidaAtual, incrementoStaminaAtual  
- **Equipavel:** idItem, nomeItem, precoItem, raridade,  incrementoVidaBase, incrementoDefesa, mulFisico, mulMagico 
- **Missao:** idMissao, nomeMissao, descricaoMissao, idMissaoSeguinte, xpRecompensa, idItemRecompensa, quatidadeOuro
- **ObjetivoMissao:** idObjetivo, descricaoObjetivo, quantidadeMeta, idMissao, idMonstro, idSala 
- **ProgressoMissao:** idPersonagem, idObjetivoMissao, progressoOjetivo, concluida  
- **Loja:** idLoja, nomeLoja, idSala
- **Catalogo:** idLoja, idItem

## Relacionamentos

**Usuario possui save:**  
- Um Usuário pode ter de 0 a 3 saves.
- Um Save deve pertencer a um único Usuário.
- Cardinalidade: (0:3) (1:1)   

**Save contem Personagem:**  
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
- Uma Sala pode conter nenhum ou varios Personagem.
- Cardinalidade: (1:1) (0:n)  

**Sala possui InstaciaItem:**    
- Uma Sala pode ter nenhum ou vários InstaciaItem.
- Um InstaciaItem deve estar em uma única Sala.
- Cardinalidade: (0:N) (1:1)  

**InstaciaItem contem Item:**  
- Um InstaciaItem deve possuir exatamente um Item.
- Um Item pode estar em nenhum ou vários InstaciaItem.
- Cardinalidade: (1:1) (0:N)  

**Personagem tem Inventário:**  
- Um Personagem tem um único Inventário.
- Um Inventário pertence a um único Personagem.
- Cardinalidade: (1:1) (1:1)  

**Inventário guarda InstaciaItem:**  
- Um Inventário pode ter nenhum ou vários InstaciaItem.
- Um InstaciaItem deve estar em um único Inventário.
- Cardinalidade: (0:N) (1:1)  

**Personagem mata InstanciaMonstro:**  
- Um Personagem pode matar nenhum ou várias InstanciaMonstro.
- Uma InstanciaMonstro é morta por apenas um Personagem.
- Cardinalidade: (0:N) (1:1)  

**Monstro possui InstanciaMonstro:**  
- Um Monstro pode ter nenhuma ou várias InstanciaMonstro.
- Uma InstanciaMonstro deve pertencer a um único Monstro.
- Cardinalidade: (0:N) (1:1)  

**InstanciaMonstro dropa InstaciaItem:**  
- Uma InstanciaMonstro pode criar nenhum ou um InstaciaItem.
- Um InstaciaItem criado por uma e so um InstanciaMonstro.
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

**Missão desbloqueia Missão:**
- Uma Missão pode desbloquear uma ou várias Missões.
- Uma Missão pode ser desbloqueada por uma única Missão.
- Cardinalidade: (1:N) (1:1)

**Missão concede InstanciaItem:**
- Uma Missão pode conceder varias InstanciaItem.
- Uma InstanciaItem pode ser concedida por uma Missão.
- Cardinalidade: (1:N) (1:1)

**ObjetivoMissao referencia InstanciaMonstro:**
- Um ObjetivoMissao pode referenciar nenhuma ou varias InstanciaMonstro.
- Um InstanciaMonstro pode ser referenciado por um ObjetivoMissao.
- Cardinalidade: (0:n) (1:1)

**ObjetivoMissao referencia Sala:**
- Um ObjetivoMissao pode referenciar nenhuma ou varias Salas.
- Uma Sala pode ser referenciada por um ObjetivoMissao.
- Cardinalidade: (1:1) (1:1)

**Regiao tem Salas:**
- Uma Regiao pode ter várias Salas.
- Uma Sala pertence a uma única Regiao.
- Cardinalidade: (1:N) (1:1)

**Monstro esta em Regiao:**
- Um Monstro pode estar em uma única Regiao.
- Uma Regiao pode ter vários Monstros.
- Cardinalidade: (1:1) (1:N)

**ObjetivoMissao conclui ProgressoMissao:**
- Um ObjetivoMissao pode concluir um ProgressoMissao.
- Um ProgressoMissao pode ser concluido por um ObjetivoMissao.
- Cardinalidade: (1:1) (1:1)

**Personagem progride ProgressoMissao:**  
- Um Personagem pode ter progresso em várias Missões.
- Um ProgressoMissao pertence a um único Personagem.
- Cardinalidade: (0:N) (1:1)  

**Personagem equipa InstanciaItem:**
- Um Personagem pode equipar nenhum ou uma InstanciaItem.
- Um InstanciaItem pode ser equipado por um Personagem.
- Cardinalidade: (0:1) (1:1)

**Loja possui Catalogo:**
- Uma Loja possui um Catalogo.
- Um Catalogo pertence a uma única Loja.
- Cardinalidade: (1:1) (1:1)

**Catalogo vende Item:**
- Um Catalogo pode vende vários Itens.
- Um Item pode ser vendido em um Catalogo.
- Cardinalidade: (0:N) (1:1)


**Sala possui Loja:**
- Uma Sala pode ter uma Loja.
- Uma Loja pertence a uma única Sala.
- Cardinalidade: (0:1) (1:1)


---

## Histórico de Versões
| Versão |    Data    | Descrição               | Autor                                                                                                                 |
| :----: | :--------: | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [`1.0`](/Modulo_1/ME-R(Modelo_Entidade_Relacionamento).md)  | 26/11/2024 | Criação do documento ME-R | Todos                       |
| [`2.0`](/Modulo_2/ME-R(Modelo_Entidade_Relacionamento)_v2.md)  | 30/11/2024 | Adição de atributos e relacionamentos | Todos                       |
| [`2.1`](/Modulo_2/ME-R(Modelo_Entidade_Relacionamento)_v2.1.md)  | 14/01/2025 | Adição de atributos e relacionamentos | Todos                       |
| [`3.0`](/Modulo_3/ME-R(Modelo_Entidade_Relacionamento)_v3.md)  | 27/01/2025 | Correção baseada nas novas features | [Henrique ](https://github.com/henriquecq)                         |
| [`3.1`](/Modulo_3/ME-R(Modelo_Entidade_Relacionamento)_v3.md)  | 01/02/2025 | Novas features | [Henrique ](https://github.com/henriquecq)                         |

