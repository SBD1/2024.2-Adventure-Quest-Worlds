# Dicionário de Dados

---

### **Player**
| Atributo     | Tipo     | Descrição                           |
|--------------|----------|-------------------------------------|
| idJogador    | Inteiro  | Identificador único do jogador.     |
| nome         | Texto    | Nome do jogador.                   |
| HP           | Inteiro  | Pontos de vida do jogador.          |
| Mana         | Inteiro  | Pontos de mana do jogador.          |
| Def          | Inteiro  | Defesa do jogador.                 |
| Atk          | Inteiro  | Ataque físico do jogador.           |
| Atkmg        | Inteiro  | Ataque mágico do jogador.           |
| Ouro         | Inteiro  | Quantidade de ouro do jogador.      |
| idSala       | Inteiro  | Sala atual onde o jogador está.     |
| armadura     | Inteiro  | Equipamento de defesa do jogador.   |
| arma         | Inteiro  | Equipamento de ataque do jogador.   |
| insignia     | Inteiro  | Item especial do jogador.           |

---

### **Classe**
| Atributo  | Tipo     | Descrição                         |
|-----------|----------|-----------------------------------|
| idClasse  | Inteiro  | Identificador único da classe.     |
| mana      | Inteiro  | Pontos de mana base da classe.     |
| def       | Inteiro  | Defesa base da classe.             |
| atk       | Inteiro  | Ataque físico base da classe.      |
| atkmg     | Inteiro  | Ataque mágico base da classe.      |

---

### **Loja**
| Atributo  | Tipo     | Descrição                         |
|-----------|----------|-----------------------------------|
| idLoja    | Inteiro  | Identificador único da loja.       |
| nome      | Texto    | Nome da loja.                     |
| idSala    | Inteiro  | Sala onde a loja está localizada.  |
| idAndar   | Inteiro  | Andar onde a loja está localizada. |

---

### **EstoqueItem**
| Atributo   | Tipo     | Descrição                           |
|------------|----------|-------------------------------------|
| idItem     | Inteiro  | Identificador único do item.        |
| idLoja     | Inteiro  | Loja onde o item está disponível.   |
| preço      | Inteiro  | Preço do item.                     |
| quantidade | Inteiro  | Quantidade disponível no estoque.   |

---

### **Habilidade**
| Atributo     | Tipo     | Descrição                              |
|--------------|----------|----------------------------------------|
| idHabilidade | Inteiro  | Identificador único da habilidade.      |
| nome         | Texto    | Nome da habilidade.                   |
| idClasse     | Inteiro  | Classe que possui essa habilidade.     |
| custoDeMana  | Inteiro  | Custo de mana para usar a habilidade.   |
| dano         | Inteiro  | Dano causado pela habilidade.          |
| cooldown     | Inteiro  | Tempo de recarga da habilidade.        |
| tipodedano   | Texto    | Tipo de dano da habilidade (físico/mágico). |

---

### **Inventário**
| Atributo         | Tipo     | Descrição                          |
|------------------|----------|------------------------------------|
| idJogador        | Inteiro  | Jogador dono do inventário.         |
| espaço           | Inteiro  | Espaço disponível no inventário.   |
| idInstanciaItem  | Inteiro  | Item associado ao inventário.      |
| equipavel        | Booleano | Indica se o item é equipável.      |

---

### **Andar**
| Atributo  | Tipo     | Descrição                |
|-----------|----------|--------------------------|
| idAndar   | Inteiro  | Identificador único do andar. |
| nome      | Texto    | Nome do andar.           |

---

### **Sala**
| Atributo  | Tipo     | Descrição                |
|-----------|----------|--------------------------|
| idSala    | Inteiro  | Identificador único da sala. |
| idAndar   | Inteiro  | Andar onde a sala está.  |
| descrição | Texto    | Descrição da sala.       |

---

### **Instância do Item**
| Atributo        | Tipo     | Descrição                    |
|-----------------|----------|------------------------------|
| idInstanciaItem | Inteiro  | Identificador único da instância do item. |
| idItem          | Inteiro  | Item associado à instância.   |

---

### **Item**
| Atributo      | Tipo     | Descrição                          |
|---------------|----------|------------------------------------|
| idItem        | Inteiro  | Identificador único do item.       |
| nomeDoItem    | Texto    | Nome do item.                     |
| custoDeOuro   | Inteiro  | Custo do item em ouro.            |
| equipavel     | Booleano | Indica se o item é equipável.     |

---

### **Consumível**
| Atributo  | Tipo     | Descrição                      |
|-----------|----------|--------------------------------|
| idItem    | Inteiro  | Identificador único do item.   |
| maisHp    | Inteiro  | Pontos de HP restaurados.      |
| maisMana  | Inteiro  | Pontos de mana restaurados.    |

---

### **Equipável**
| Atributo  | Tipo     | Descrição                          |
|-----------|----------|------------------------------------|
| idItem    | Inteiro  | Identificador único do item.       |
| tipo      | Texto    | Tipo de equipamento (armadura, arma). |
| maisDef   | Inteiro  | Aumento de defesa.                |
| maisAtk   | Inteiro  | Aumento de ataque físico.         |
| maisAtkmg | Inteiro  | Aumento de ataque mágico.         |
| maisMana  | Inteiro  | Aumento de mana.                 |

---

### **Instância do Monstro**
| Atributo    | Tipo     | Descrição                          |
|-------------|----------|------------------------------------|
| idMonstro   | Inteiro  | Identificador único do monstro.    |
| quantidade  | Inteiro  | Quantidade de instâncias do monstro. |

---

### **Monstro**
| Atributo   | Tipo     | Descrição                          |
|------------|----------|------------------------------------|
| idMonstro  | Inteiro  | Identificador único do monstro.    |
| HP         | Inteiro  | Pontos de vida do monstro.         |
| Def        | Inteiro  | Defesa do monstro.                |
| Atk        | Inteiro  | Ataque físico do monstro.          |
| Atkmg      | Inteiro  | Ataque mágico do monstro.          |
| qntdOuro   | Inteiro  | Quantidade de ouro ao ser derrotado. |
| tipo       | Texto    | Tipo de monstro (Minion/Boss).    |

---

### **Minion**
| Atributo   | Tipo     | Descrição                          |
|------------|----------|------------------------------------|
| idMonstro  | Inteiro  | Identificador único do monstro.    |

---

### **Boss**
| Atributo   | Tipo     | Descrição                          |
|------------|----------|------------------------------------|
| idMonstro  | Inteiro  | Identificador único do monstro.    |
| descrição  | Texto    | Descrição do boss.                |
| idItem     | Inteiro  | Item dropado pelo boss.           |

--- 

## 
| Versão |    Data    | Descrição               | Autor                                                                                                                 |
| :----: | :--------: | ----------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [`1.0`](/Modulo_1/DD(Dicinario_de_Dados).md)  | 26/11/2024 | Criação do documento DD | [Henrique ](https://github.com/henriquecq)                          |