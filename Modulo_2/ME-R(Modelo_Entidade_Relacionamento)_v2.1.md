# ME-R(Modelo Entidade-Relacionamento)

## Entidades

* Usuario
* Monstro
* instanciaMonstro
* Minion
* Boss
* Save
* Classe
* Personagem
* Habilidade
* Inventario
* itemPersonagem
* Sala
* itemSala
* Item
* Consumivel
* Equipavel

## Atributos

- **Usuario:** idUsuario, login, senha, qtdPersonagem
  
- **Monstro:** idMonstro, tipoMonstro
  
- **Instância do Monstro:** idInstanciaMonstro, idMonstro, vidaAtual, idSala
  
- **Minion:** idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, quantidadeOuro

- **Boss:** idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, mulBoss, idItem

- **Save:** idUsuario, idPersonagem

- **Classe:** idClasse, nomeClasse, mulFisico, mulMagico

- **Personagem:** idPersonagem, nomePersonagem, staminaAtualPersonagem  , vidaAtualPersonagem, staminaBasePersonagem, vidaBasePersonagem, defensePersonagem, ataqueFisico, AtaqueMagico, idSala

- **Habilidade:** idHabilidade, nomeHabilidade, danoFisico, danoMagico, custoStamina, custoCooldown, idClasse

- **Inventario:** idInventario, espacoDisponivel, capacidade, quantidadeOuro, idPersonagem *(Verificar)*

- **ItemPersonagem:** idItem, idItemPersonagem, idInventário, quantidadeItem

- **Sala:** idSala, nomeSala, salaNorte, salaSul, salaLeste, salaOeste

- **ItemSala:** idItem,idItemSala, idSala, quantidadeItem

- **Item:** idItem, tipoItem

- **Consumivel:** idItem, nomeItem, valorItem, incrementoVidaAtual, incrementoStaminaAtual

- **Equipavel:** idItem, nomeItem, valorItem, incrementoVidaBase, incrementoDefesa, mulFisico, mulMagico, equipado('s' ou 'n')

## Relacionamentos
**Usuario possui save:**

- Um Usuário pode ter de 0 a 3 saves.
- Um Save deve pertencer a um único Usuário e somente um Usuário.
- Cardinalidade: (0:3) (1:1)   

**Personagem corresponde ao save:**

- Um Personagem corresponde a um único Save e somente um.
- Um Save corresponde a um único Personagem e somente um.
- Cardinalidade: (1:1) (1:1)

**Personagem escolhe classe:**

- Um Personagem deve ter uma única Classe e somente uma.
- A Classe deve corresponder a pelo menos um Personagem ou vários. 
- Cardinalidade: (1:1) (1:N)

**Classe tem Habilidade:**

- Uma Classe deve ter uma ou várias Habilidades.
- Uma Habilidade deve corresponder a uma classe e somente uma.
- Cardinalidade: (1:N) (1:1)

**Personagem esta em uma Sala**

- Um Personagem deve estar em uma única Sala e somente uma.
- Uma Sala pode ter nenhum ou um Personagem.
- Cardinalidade: (1:1) (0:1)

**Sala possui itemSala**

- Uma Sala pode ter nenhum ou vários itemSala.
- Um itemSala deve estar em somente uma sala.
- Cardinalidade: (0:N) (1:1)

**ItemSala possui item**

- Um itemSala deve possuir exatemente um Item.
- Um Item pode estar em nenhum ou vários itemSala.
- Cardinalidade: (1:1) (0:N)

**Personagem possui inventário:**

- Um Personagem tem somente um único Inventário.
- Um Inventário deve corresponder a um único Personagem
- Cardinalidade: (1:1) (1:1)

**Inventario guarda o itemPersonagem:**

- Um Inventario pode ter nenhum até vários itemPersonagem.
- Um itemPersonagem deve estar somente em um inventário.
- Cardinalidade: (0:N) (1:1)

**itemPersonagem possui Item**

- Um itemPersonagem deve possuir somente um Item.
- Um Item pode conter nenhum ou vários itemPersonagem.
- Cardinalidade: (1:1) (0:N)

**Personagem mata instanciaMonstro**

- Um Personagem pode matar nenhum até várias instanciaMonstro.
- A instanciaMonstro é morta por somente um e apenas um Personagem.
- Cardinalidade: (0:N) (1:1)

**Monstro possui instanciaMonstro**

- Um Monstro pode ter nenhum ate várias instanciaMonstro.
- Uma instanciaMonstro deve pertencer a exatamente um Monstro.
- Cardinalidade: (0:N) (1:1) 

**instanciaMonstro cria itemPersonagem**

- Uma instanciaMonstro cria nenhum ou um itemPersonagem.
- Um itemPersonagem pode ser criado por nenhum ou um instanciaMonstro.
- Cardinalidade: (0:1) (0:1)

**instanciaMonstro contem Sala**

- Uma instanciaMonstro deve estar em uma e somente uma sala.
- Uma Sala pode conter nenhum um várias instanciaMonstro.
- Cardinalidade: (1:1) (0:N)

**Item _possui exclusivamente_ tipos**

- Um item pode ser classificado **apenas com uma única** das seguintes categorias: Consumivel e Equipavel.


**Monstro possui exclusivamente tipos**

- Um monstro pode ser classificado **apenas com uma única** das seguintes categorias: Minion ou Boss

---

## 
| Versão |    Data    | Descrição               | Autor                                                                                                                 |
| :----: | :--------: | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [`1.0`](/Modulo_1/ME-R(Modelo_Entidade_Relacionamento).md)  | 26/11/2024 | Criação do documento ME-R | Todos                       |
| [`2.0`](/Modulo_2/ME-R(Modelo_Entidade_Relacionamento)_v2.md)  | 30/11/2024 | Adição de atributos e relacionamentos | Todos                       |
| [`2.1`](/Modulo_2/ME-R(Modelo_Entidade_Relacionamento)_v2.1.md)  | 14/01/2025 | Adição de atributos e relacionamentos | Todos                       |