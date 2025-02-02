-- SQLBook: Code
-- Listar todas as classes disponíveis com seus multiplicadores
SELECT * FROM Classe;

-- Exibir todas as salas com seus caminhos conectados (Norte, Sul, Leste, Oeste)
SELECT idSala, nomeSala, salaNorte, salaSul, salaLeste, salaOeste
FROM Sala;

-- Listar os monstros com seus tipos e detalhes básicos
SELECT Monstro.idMonstro, Monstro.tipoMonstro, Minion.nomeMonstro, Minion.vidaMonstro, Minion.danoMonstro, Minion.defMonstro, Minion.quantidadeOuro
FROM Monstro
LEFT JOIN Minion ON Monstro.idMonstro = Minion.idMonstro
UNION
SELECT Monstro.idMonstro, Monstro.tipoMonstro, Boss.nomeMonstro, Boss.vidaMonstro, Boss.danoMonstro, Boss.defMonstro, NULL AS quantidadeOuro
FROM Monstro
LEFT JOIN Boss ON Monstro.idMonstro = Boss.idMonstro;

-- Consultar monstros que estão atualmente em instâncias nas salas
SELECT instanciaMonstro.idInstanciaMonstro, instanciaMonstro.idMonstro, Monstro.tipoMonstro, instanciaMonstro.vidaAtual, Sala.nomeSala
FROM instanciaMonstro
JOIN Monstro ON instanciaMonstro.idMonstro = Monstro.idMonstro
LEFT JOIN Sala ON instanciaMonstro.idSala = Sala.idSala;

-- Listar as habilidades disponíveis para cada classe
SELECT Habilidade.nomeHabilidade, Habilidade.danoFisico, Habilidade.danoMagico, Habilidade.custoStamina, Habilidade.custoCooldown, Classe.nomeClasse
FROM Habilidade
JOIN Classe ON Habilidade.idClasse = Classe.idClasse;
-- Listar itens consumíveis com seus efeitos
SELECT Consumivel.nomeItem, Consumivel.valorItem, Consumivel.incrementoVidaAtual, Consumivel.incrementoStaminaAtual
FROM Consumivel;

-- Listar itens equipáveis com suas características
SELECT Equipavel.nomeItem, Equipavel.valorItem, Equipavel.incrementoVidaBase, Equipavel.incrementoDefesa, Equipavel.mulFisico, Equipavel.mulMagico, Equipavel.equipado
FROM Equipavel;

--Consultar o inventário de cada personagem com seus itens e quantidades
SELECT Inventario.idInventario, Inventario.idPersonagem, Inventario.espacoDisponivel, Inventario.capacidade, Inventario.quantidadeOuro, itemPersonagem.idItem, Item.tipoItem, itemPersonagem.quantidadeItem
FROM Inventario
LEFT JOIN itemPersonagem ON Inventario.idInventario = itemPersonagem.idInventario
LEFT JOIN Item ON itemPersonagem.idItem = Item.idItem;

-- Consultar personagens com seus atributos e classe 
SELECT Personagem.idPersonagem, Personagem.nomePersonagem, Personagem.staminaAtualPersonagem, Personagem.vidaAtualPersonagem, Classe.nomeClasse 
FROM Personagem
LEFT JOIN Classe ON Personagem.idClasse = Classe.idClasse


-- Consultar informações de todas as salas e os itens disponíveis nelas
SELECT Sala.idSala, Sala.nomeSala, itemSala.idItem, Item.tipoItem, itemSala.quantidadeItem
FROM Sala
LEFT JOIN itemSala ON Sala.idSala = itemSala.idSala
LEFT JOIN Item ON itemSala.idItem = Item.idItem;