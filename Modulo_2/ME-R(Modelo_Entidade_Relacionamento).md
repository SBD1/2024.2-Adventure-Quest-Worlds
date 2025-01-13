# ME-R (Modelo Entidade-Relacionamento)

## Entidades

* Usuário  
* Monstro  
* Instância do Monstro  
* Minion  
* Boss  
* Save  
* Classe  
* Personagem  
* Habilidade  
* Inventário  
* ItemPersonagem  
* Sala  
* ItemSala  
* Item  
* Consumível  
* Equipável  

## Atributos

- **Usuário:** idUsuario, login, senha, qtdPersonagem
  
- **Monstro:** idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro
  
- **Instância do Monstro:** idInstanciaMonstro, idMonstro, vidaAtual, idSala
  
- **Minion:** ???

- **Boss:** mulBoss, idItem

- **Save:** idPersonagem, bonecos *(?)*

- **Classe:** idClasse, nomeClasse, mulFisico, mulMagico

- **Personagem:** idPersonagem, nomePersonagem, staminaAtualPersonagem *(?)*, vidaAtualPersonagem, staminaBasePersonagem, vidaBasePersonagem, defensePersonagem, ataqueFisico, ataqueMagico

- **Habilidade:** idHabilidade, nomeHabilidade, danoFisico, danoMagico, custoStamina, custoCooldown

- **Inventário:** idInventario, espacoDisponivel, capacidade, quantidadeOuro, idPersonagem *(Verificar)*

- **ItemPersonagem:** 

- **Sala:** idSala, nomeSala, salaNorte, salaSul, salaLeste, salaOeste

- **ItemSala:** 

- **Item:** idItem, nomeItem, valorItem

- **Consumível:** incrementoDeVidaAtual, incrementoDeStaminaAtual

- **Equipável:** incrementoDeVidaBase, incrementoDefesa, mulFisico, mulMagico, equipado ('s' ou 'n')

## Relacionamentos

**Usuário possui save:**

- Um usuário pode ter de 0 a 3 saves, mas um save pertence a um único usuário.
- Um save corresponde a um personagem e um personagem corresponde a um save.
- Cardinalidade: (1:3) (1:1)

**Personagem escolhe classe:**

- Um personagem pode ter uma única classe.  
- A classe pode corresponder a 0 ou vários personagens.  
- Cardinalidade: (1:1) (0:N)

**Classe possui habilidade:**

- Uma classe pode ter 1 ou várias habilidades.  
- Uma habilidade pode corresponder a 1 classe.  
- Cardinalidade: (1:N) (1:1)

**Personagem está em uma sala:**

- Um personagem pode estar em exatamente 1 sala.  
- Uma sala pode ter 0 até 1 personagem.  
- Cardinalidade: (1:1) (0:1)

**Sala possui itemSala:**

- Uma sala pode ter 0 até vários itemSala.  
- Um itemSala pode estar em 0 até 1 sala.  
- Cardinalidade: (0:N) (0:1)

**ItemSala possui item:**

- Um itemSala possui exatamente 1 item.  
- Um item pode estar em 0 até vários itemSala.  
- Cardinalidade: (1:1) (0:N) *(Cardinalidade no DER?)*

**Personagem possui inventário:**

- Um personagem tem somente um único inventário.  
- Um inventário pode corresponder a 1 ou 1 personagem.  
- Cardinalidade: (1:1) (1:1)

**Inventário guarda o itemPersonagem:**

- Um inventário pode ter 0 até vários itemPersonagem.  
- Um itemPersonagem somente pode estar em 1 inventário.  
- Cardinalidade: (0:N) (1:1)

**Um itemPersonagem possui item:**

- Um itemPersonagem possui exatamente 1 item.  
- Um item pode ter 0 até vários itemPersonagem.  
- Cardinalidade: (1:1) (0:N)

**Personagem mata instância do monstro:**

- Um personagem pode matar 0 até vários monstros.  
- Um personagem pode ser morto por apenas 1 monstro.  
- Cardinalidade: (0:N) (1:1)

**InstânciaMonstro possui monstro:**

- Uma instânciaMonstro possui exatamente 1 monstro.  
- Um monstro pode ter 0 até várias instâncias.  

**Instância monstro cria itemPersonagem:** *(?)*

- Uma instânciaMonstro pode criar 0 até 1 itemPersonagem.  
- Um itemPersonagem pode ser criado por 0 até 1 instânciaMonstro.  
- Cardinalidade: (0:1) (0:1)
