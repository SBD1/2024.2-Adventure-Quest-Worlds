# ME-R(Modelo Entidade-Relacionamento)

## Entidades

* Player
* Classe
* Loja
* EstoqueItem
* Habilidade
* Inventário
* Andar
* Sala
* Instancia do Item
* Item
* Consumivel
* Equipavel
* Instancia do Monstro
* Monstro
* Minion
* Boss


## Atributos

**Player:** idJogador, nome, HP, Mana, Def, Atk, Atkmg, Ouro, idSala, armadura, arma, insignia

**Classe:** idClasse, mana, def, atk, atkmg

**Loja:** idLoja, nome, idSala, idAndar

**EstoqueItem:** idItem, idLoja, preço, quantidade

**Habilidade:** idHabilidade, nome, idClasse, custoDeMana, dano, cooldown, tipodedano

**Inventário:** idJogador, espaço, idInstanciaItem, equipavel

**Andar:** idAndar, nome

**Sala:** idSala, idAndar, descrição

**Instancia do Item:** idInstanciaItem, idItem

**Item:** idItem, nomeDoItem, custoDeOuro, equipavel

**Consumivel:** idItem, maisHp, maisMana

**Equipavel:** idItem, tipo, maisDef, maisAtk, maisAtkmg, maisMana

**Instancia do Monstro:** idMonstro, quantidade

**Monstro:** idMonstro, HP, Def, Atk, Atkmg, qntdOuro, tipo

**Minion:** idMonstro

**Boss:** idMonstro, descrição, idItem


## Relacionamentos

**Player ___Compra___ na Loja:**

* Um Player compra 0 ou vários itens na Loja.
* Existem 0 ou várias lojas onde players podem comprar.
* Cardinalidade: (0:n) (0:n)

**Player ___Escolhe___ Classe:**

* Um Player escolhe 1 classe.
* A classe pertence a vários ou nenhum Player.
* Cardinalidade: (1:1) (0:n)


**Classe ___Tem___ Habilidade:**

* A Classe pode possuir somente 4 habilidades.
* A Habilidade tem exatamente uma Classe.
* Cardinalidade: (1:4) (1:1)

**Player ___Tem___ Inventário:**

* Um Player tem exatamente 1 inventário.
* Um inventário pertence a exatamente um Player.
* Cardinalidade: (1:1) (1:1)

**Inventário ___Possui___ Instância do Item:**

* O Inventário possui nenhum ou várias Instâncias dos Itens.
* Instância de Item pode possuir 0 ou 1 inventário.
* Cardinalidade: (0:n) (0:1)

**Loja ___Possui___ EstoqueItem:**

* Uma loja pode possuir vários EstoqueItem.
* EstoqueItem só pode possuir em apenas uma loja.
* Cardinalidade: (0:n) (1:1)

**EstoqueItem ___Contem___ Instância do item:**

* EstoqueItem contém um ou várias Instâncias do item.
* Instância do Item contém nenhuma ou vários EstoqueItem.
* Cardinalidade: (1:n) (0:n)

**Loja ___Esta___ Sala:**

* Uma loja pode estar em somente uma Sala.
* Sala pode possuir 0 ou uma loja.
* Cardinalidade: (1:1) (0:1)

**Sala ___Possui___ Andar:**

* Sala possui somente um Andar.
* Andar possui uma ou mais Salas.
* Cardinalidade: (1:1) (1:n)

**Sala ___Esta___ Instância do Monstro:**

* Sala está com nenhum ou várias Instâncias de Monstros.
* Instância de Monstro está em somente uma sala.
* Cardinalidade: (0:n) (1:1)

**Player ___Luta___ Instancia do Monstro:**

* Um Player Luta contra 0 ou 1 instância do Monstro.
* A Instância do Monstro luta contra 0 ou 1 Player.
* Cardinalidade: (0:1) (0:1)

**Player ___Esta___ Sala:**

* Um Player tem que estar em uma sala.
* A sala pode possuir um ou mais Players.
* Cardinalidade: (1:1) (0:n)

**Instancia de monstro ___Possui___ Monstro:**

* Uma Instancia de monstro possui exatamente 1 monstro.
* Um monstro possui no mínimo 0 e no máximo n instâncias.
* Cardinalidade: (1:1) (0:n)

**Instancia de monstro ___Dropa___ Instancia do item:**

* Uma Instancia de monstro dropa no mínimo 0 e no máximo 1 Instancia de item.
* A Instancia de item é dropada exatamente por 1 instância de monstro.
* Cardinalidade: (0:1) (1:1)
