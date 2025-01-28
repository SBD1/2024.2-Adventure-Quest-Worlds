INSERT INTO Classe (idClasse, nomeClasse, mulFisico, mulMagico) VALUES
(1,'Guerreiro', 1.5, 0.5),
(2,'Mago', 0.6, 1.8),
(3,'Arqueiro', 1.2, 0.8),
(4,'Assassino', 1.3, 0.9);

INSERT INTO Sala (idSala, idRegiao, nomeSala, salaNorte, salaSul, salaLeste, salaOeste) VALUES
(1, 1, 'Arcangrove', NULL, NULL, NULL, 2),
(2, 1, 'The Cloister', 3, NULL, 1, NULL),
(3, 1, 'Mudluk Village', 4, 2, NULL, NULL),
(4, 1, 'Natatorium', NULL, 3, 5, NULL),
(5, 1, 'Ruins of Great Gilead', NULL, 6, NULL, 4),
(6, 1, 'Mount Mafic', 5, 7, NULL, NULL),
(7, 1, 'Elemental', 6, 8, 9, NULL),
(8, 2, 'Ledgermayne', 7, NULL, 9, NULL),
(9, 2, 'Boss', NULL, 8, NULL, 7);


INSERT INTO Monstro (idMonstro,tipoMonstro) VALUES
(1,'Minion'),
(2,'Boss'),
(3,'Minion'),
(4,'Minion'),
(5,'Minion'),
(6,'Minion'),
(7,'Minion'),
(8,'Minion'),
(9,'Minion'),
(10,'Minion'),
(11, 'Minion');

INSERT INTO Regiao (idRegiao, nomeRegiao, descricaoRegiao) VALUES
(1,'Arcangrove','A beautiful, thriving forest home to many creatures of magical descent. Ancient magi have studied in the notable Tower of Magic, a place where magic users shall learn, evolve, and be tested.');

INSERT INTO Minion (idMonstro, idRegiaoOrigem, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, quantidadeOuro) VALUES
(1, 1, 'Chaos Sprite', 1640, 49, 15, 25),
(2, 1, 'Gorrilaphant', 1640, 61, 15, 25),
(3, 1, 'Linix', 400, 25, 4, 20),
(4, 1, 'Seed Splinter', 400, 25, 4, 20),
(5, 1, 'Acornent', 750, 45, 10, 35),
(6, 1, 'Karasu', 820, 38, 12, 42),
(7, 1, 'Wendigo', 780, 50, 9, 37),
(8, 1, 'Moglurker', 1000, 60, 20, 50),
(9, 1, 'Swamp Frogdrake', 1000, 60, 20, 50),
(10, 1, 'Swamp Lurker', 1000, 60, 20, 50),
(11, 1, 'Tiger Leech', 1000, 60, 20, 50);

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
(1, 1640, 1),
(2, 1640, 1),  
(3, 400, 1),  
(4, 400, 1),
(5, 750, 2),
(6, 820, 2),
(7, 780, 2),
(8, 1000, 3),
(9, 1000, 3),
(10, 1000, 3),
(11, 1000, 3);

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
