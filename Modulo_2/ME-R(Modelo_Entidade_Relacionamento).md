# ME-R(Modelo Entidade-Relacionamento)

## Entidades

* Usuario
* Monstro
* Instancia do Monstro
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

## Atributos

- **Usuario:** idUsuario, login, senha, qtdPersonagem
  
- **Monstro:** idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro
  
- **Instancia do Monstro:** idInstanciaMonstro, idMonstro, vidaAtual, idSala
  
- **Minion:** ???

- **Boss:** mulBoss, idItem

- **Save:** idPersonagem, bonecos *(?)*

- **Classe:** idClasse, nomeClasse, mulFisico, mulMagico

- **Personagem:** idPersonagem, nomePersonagem, staminaAtualPersonagem *(?)* , vidaAtualPersonagem, staminaBasePersonagem, vidaBasePersonagem, defensePersonagem, ataqueFisico, AtaqueMagico

- **Habilidade:** idHabilidade, nomeHabilidade, danoFisico, danoMagico, custoStamina, custoCooldown

- **Inventario:** idInventario, espacoDisponivel, capacidade, quantidadeOuro, idPersonagem *(Verificar)*

- **ItemPersonagem:** 

- **Sala:** idSala, nomeSala, salaNorte, salaSul, salaLeste, salaOeste

- **ItemSala:** 

- **Item:** idItem, nomeItem, valorItem

- **Consumivel:** incrementoDeVidaAtual, incrementoDeStaminaAtual

- **Equipavel:** incrementoDeVidaBase, incrementoDefesa, mulFisico, mulMagico, equipado('s' ou 'n')

## Relacionamentos
**Usuario possui save:**

- Um usuário pode ter de 0 a 3 saves, mas um save pertence a um único usuário.
- Um save corresponde a um personagem e um personagem corresponde a um save.
- Cardinalidade: (1:3) (1:1)

**Personagem escolhe classe:**

- Um personagem pode ter uma única classe
- A classe pode corresponder a 0 ou vários personagens
- Cardinalidade: (1:1) (0:N)

**Classe possui habilidade:**

- Uma classe pode ter 1 ou várias habilidades
- Uma habilidade pode corresponder a 1 classe
- Cardinalidade: (1:N) (1:1)

**Personagem esta em uma Sala**

- Um personagem pode estar em exatamente 1 sala
- Uma sala pode ter 0 ate 1 personagem
- Cardinalidade: (1:1) (0:1)

**Sala possui itemSala**

- Uma sala pode ter 0 ate vários itemSala
- Um itemSala pode estar em 0 ate 1 sala
- Cardinalidade: (0:N) (0:1)

**ItemSala possui item**

- Um itemSala possui exatemente 1 item
- Um item pode estar em 0 ate vários itemSala
- Cardinalidade: (1:1) (0:N)  (cardinalidade no DER?)

**Personagem possui inventário:**

- Um personagem tem somente um único inventário
- Um inventário pode corresponder a 1 ou 1 personagem
- Cardinalidade: (1:1) (1:1)

**Inventario guarda o itemPersonagem:**

- Um inventário pode ter 0 ate vários itemPersonagem
- Um itemPersonagem somente pode estar em 1 inventário
- Cardinalidade: (0:N) (1:1)

**Um itemPersonagem possui item**

- Um itemPersonagem possui exatemente 1 item
- Um item pode ter 0 ate vários itemPersonagem
- Cardinalidade: (1:1) (0:N)

**Personagem mata Instacia do monstro**

- Um personagem pode matar 0 ate vários monstros
- Um personagem pode ser morto por apenas 1 monstro
- Cardinalidade: (0:N) (1:1)

**InstanciaMonstro possui monstro**

- Uma instanciaMonstro possui exatemente 1 monstro
- Um monstro pode ter 0 ate vários instancias

**Instancia monstro cria itemPersonagem** (?)

- Uma instanciaMonstro pode criar 0 ate 1 itemPersonagem
- Um itemPersonagem pode ser criado por 0 ate 1 instanciaMonstro
- Cardinalidade: (0:1) (0:1)