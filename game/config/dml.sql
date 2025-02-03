INSERT INTO classe (idClasse, nomeClasse, mulFisico, mulMagico) VALUES
    (1,'Guerreiro', 1.5, 0.5),
    (2,'Mago', 0.6, 1.8),
    (3,'Arqueiro', 1.2, 0.8),
    (4,'Assassino', 1.3, 0.9)
ON CONFLICT (idClasse) DO NOTHING;

INSERT INTO Regiao (idRegiao, nomeRegiao, descricaoRegiao) VALUES
    (1,'Arcangrove','A beautiful, thriving forest home to many creatures of magical descent. Ancient magi have studied in the notable Tower of Magic, a place where magic users shall learn, evolve, and be tested.')
ON CONFLICT (idRegiao) DO NOTHING;

INSERT INTO Sala (idSala, idRegiao, nomeSala, salaNorte, salaSul, salaLeste, salaOeste) VALUES
    (0, 1, 'Void', NULL, NULL, NULL, NULL),
    (1, 1, 'Arcangrove', NULL, NULL, NULL, 2),
    (2, 1, 'The Cloister', 3, NULL, 1, NULL),
    (3, 1, 'Mudluk Village', 4, 2, NULL, NULL),
    (4, 1, 'Natatorium', NULL, 3, 5, NULL),
    (5, 1, 'Ruins of Great Gilead', NULL, 6, NULL, 4),
    (6, 1, 'Mount Mafic', 5, 7, NULL, NULL),
    (7, 1, 'Elemental', 6, 8, 9, NULL),
    (8, 1, 'Ledgermayne', 7, NULL, 9, NULL),
    (9, 1, 'Boss', NULL, 8, NULL, 7)
ON CONFLICT (idSala) DO NOTHING;

INSERT INTO Monstro (idMonstro, nomeMonstro, vidaMonstro, danoMonstro, defMonstro, tipoMonstro, qntXP, idRegiao) VALUES
    (1, 'Chaos Sprite', 1640, 49, 15, 'False', 25, 1),
    (2, 'Gorrilaphant', 1640, 61, 15, 'False', 25, 1),
    (3, 'Linix', 400, 25, 4, 'False',25, 1),
    (4, 'Seed Splinter', 400, 25, 4, 'False', 25, 1),
    (5, 'Acornent', 750, 45, 10, 'False', 25, 1),
    (6, 'Karasu', 820, 38, 12, 'False', 25, 1),
    (7, 'Wendigo', 780, 50, 9, 'False', 40, 1),
    (8, 'Moglurker', 1000, 60,20, 'False', 40, 1),
    (9, 'Swamp Frogdrake', 1000, 60, 20, 'False', 50, 1),
    (10, 'Swamp Lurker', 1000, 60, 20, 'False', 50, 1),
    (11, 'Tiger Leech', 1000, 60, 20, 'False', 50, 1),
    (12, 'Ledgermayne', 4000, 150, 50, 'True', 100, 1)
ON CONFLICT (idMonstro) DO NOTHING;

INSERT INTO Minion (idMonstro, quantidadeOuro) VALUES
    (1, 10),
    (2, 10),
    (3, 20),
    (4, 20),
    (5, 20),
    (6, 30),
    (7, 30),
    (8, 40),
    (9, 40),
    (10,50),
    (11,50)
ON CONFLICT (idMonstro) DO NOTHING;

INSERT INTO Habilidade (idHabilidade, nomeHabilidade, danoFisico, danoMagico, custoStamina, custoCooldown, idClasse) VALUES
    (1,'Corte Feroz', 50, 0, 30, 5, 1),
    (2,'Bola de Fogo', 0, 80, 40, 8, 2),
    (3,'Flecha Rápida', 30, 0, 20, 4, 3),
    (4,'Golpe Mortal', 60, 0, 50, 10, 4)
ON CONFLICT (idhabilidade) DO NOTHING;

INSERT INTO Item (idItem, nomeItem, tipoItem, precoItem) VALUES
    (1,'Poção de Vida','False',10),
    (2,'Poção de Stamina','False',15),
    (3,'Espada Longa','True',100),
    (4,'Armadura de Placas','True',200),
    (5,'Arco de Ouro','True',500),
    (6,'Elixir de Cura','False',10)
ON CONFLICT (idItem) DO NOTHING;

INSERT INTO Consumivel (idItem, incrementoVidaAtual, incrementoStaminaAtual) VALUES
    (1, 20, 0),
    (2, 0, 20),
    (6, 30, 30)
ON CONFLICT (idItem) DO NOTHING;

INSERT INTO Equipavel (idItem, incrementoVidaBase, incrementoDefesa, mulFisico, mulMagico) VALUES
    (3, 50, 10, 1.2, 0.8),
    (4, 100, 30, 1.1, 1.0),
    (5, 0, 20, 1.0, 1.5)
ON CONFLICT (idItem) DO NOTHING;

INSERT INTO Boss (idMonstro, idItem, mulBoss,fraseBoss) VALUES
    (12, 1, 1.5, 'Slc n compensa')
ON CONFLICT (idMonstro) DO NOTHING;

INSERT INTO instanciaMonstro (idInstanciaMonstro, idMonstro, vidaAtual, idSala) VALUES
    (1, 1, 1640, 1),
    (2, 2, 1640, 1),  
    (3, 3, 400, 1),  
    (4, 4, 400, 1),
    (5, 5, 750, 2),
    (6, 6, 820, 2),
    (7, 7, 780, 2),
    (8, 8, 1000, 3),
    (9, 9, 1000, 3),
    (10, 10, 1000, 3),
    (11, 11, 1000, 3)
ON CONFLICT (idInstanciaMonstro) DO NOTHING;


INSERT INTO Loja (idLoja, idSala, nomeLoja) VALUES
    (1, 1, 'Loja de Poções'),
    (2, 1, 'Loja de Equipamentos')
ON CONFLICT (idLoja) DO NOTHING;

INSERT INTO Catalogo (idLoja, idItem) VALUES
    (1, 1),
    (1, 2),
    (1, 6),
    (2, 3),
    (2, 4),
    (2, 5)
ON CONFLICT (idLoja, idItem) DO NOTHING;

