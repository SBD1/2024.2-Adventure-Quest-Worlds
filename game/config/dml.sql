INSERT INTO Classe (idClasse, nomeClasse, mulFisico, mulMagico) VALUES
(1,'Guerreiro', 1.5, 0.5),
(2,'Mago', 0.6, 1.8),
(3,'Arqueiro', 1.2, 0.8),
(4,'Assassino', 1.3, 0.9);

INSERT INTO Sala (idSala, nomeSala, salaNorte, salaSul, salaLeste, salaOeste) VALUES
(1,'Entrada', NULL, 2, 3, NULL),
(2,'Corredor', 1, 4, NULL, NULL),
(3,'Sala do Boss', 1, NULL, 4, NULL),
(4,'Caverna', 2, NULL, NULL, NULL);

INSERT INTO Monstro (idMonstro,tipoMonstro) VALUES
(1,'Minion'),
(2,'Minion'),
(3,'Minion'),
(4,'Boss'),
(5,'Boss');

INSERT INTO Minion (idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, quantidadeOuro) VALUES
(1, 'Goblin', 50, 10, 5, 20),
(2, 'Esqueleto', 70, 15, 7, 30),
(3, 'Lobo', 40, 12, 4, 25);

INSERT INTO Habilidade (nomeHabilidade, danoFisico, danoMagico, custoStamina, custoCooldown, idClasse) VALUES
('Corte Feroz', 50, 0, 30, 5, 1),
('Bola de Fogo', 0, 80, 40, 8, 2),
('Flecha Rápida', 30, 0, 20, 4, 3),
('Golpe Mortal', 60, 0, 50, 10, 4);

INSERT INTO Item (idItem, tipoItem) VALUES
(1,'Consumível'),
(2,'Consumível'),
(3,'Equipável'),
(4,'Equipável'),
(5,'Equipável'),
(6,'Consumível');

INSERT INTO Consumivel (idItem, nomeItem, valorItem, incrementoVidaAtual, incrementoStaminaAtual) VALUES
(1, 'Poção de Vida', 10.00, 50, 0),
(2, 'Poção de Stamina', 8.00, 0, 30),
(6, 'Elixir de Cura', 15.00, 100, 50);

INSERT INTO Equipavel (idItem, nomeItem, valorItem, incrementoVidaBase, incrementoDefesa, mulFisico, mulMagico, equipado) VALUES
(3, 'Espada Longa', 100.00, 50, 10, 1.2, 0.8, 'n'),
(4, 'Armadura de Placas', 120.00, 100, 30, 1.1, 1.0, 'n'),
(5, 'Arco de Ouro', 150.00, 0, 20, 1.0, 1.5, 'n');

INSERT INTO Boss (idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, mulBoss, idItem) VALUES
(4, 'Dragão', 500, 50, 30, 2.0, 3),
(5, 'Golem de Pedra', 400, 40, 25, 1.8, 4);

INSERT INTO instanciaMonstro (idMonstro, vidaAtual, idSala) VALUES
(1, 50, 1),
(1, 70, 2),  
(2, 500, 3),  
(1, 40, 4);

INSERT INTO Usuario (idUsuario, login, senha, qtdPersonagem) VALUES
(1,'admin', 'admin', 1);

INSERT INTO Personagem (idPersonagem, nomePersonagem, staminaAtualPersonagem, vidaAtualPersonagem, staminaBasePersonagem, vidaBasePersonagem, defensePersonagem, ataqueFisico, ataqueMagico, idClasse, idSala) VALUES
(1,'AdminArqueiro', 90, 150, 90, 150, 40, 50, 30, 2, 1);

INSERT INTO Inventario (idInventario, espacoDisponivel, capacidade, quantidadeOuro, idPersonagem) VALUES
(1,10,10,100,1);

INSERT INTO Save (idUsuario, idPersonagem) VALUES
(1, 1);

INSERT INTO itemSala (idSala, quantidadeItem, idItem) VALUES
(1, 2, 2),
(2, 1, 1);