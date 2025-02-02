-- SQLBook: Code
CREATE TABLE IF NOT EXISTS Item (
    idItem INT PRIMARY KEY,
    tipoItem VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Usuario (
    idUsuario SERIAL PRIMARY KEY,
    login VARCHAR(20) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    qtdPersonagem INT CHECK (qtdPersonagem BETWEEN 0 AND 3)
);

CREATE TABLE IF NOT EXISTS Monstro (
    idMonstro SERIAL PRIMARY KEY,
    tipoMonstro VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Regiao (
    idRegiao INT PRIMARY KEY,
    nomeRegiao VARCHAR(50) NOT NULL,
    descricaoRegiao TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Sala (
    idSala INT PRIMARY KEY,
    idRegiao INT REFERENCES Regiao(idRegiao) ON DELETE CASCADE,
    nomeSala VARCHAR(50) NOT NULL,
    salaNorte INT,
    salaSul INT,
    salaLeste INT,
    salaOeste INT
);
CREATE TABLE IF NOT EXISTS instanciaMonstro (
    idInstanciaMonstro INT PRIMARY KEY,
    idMonstro INT REFERENCES Monstro(idMonstro) ON DELETE CASCADE,
    vidaAtual INT NOT NULL,
    idSala INT REFERENCES Sala(idSala) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Minion (
    idMonstro INT PRIMARY KEY REFERENCES Monstro(idMonstro) ON DELETE CASCADE,
    idRegiaoOrigem INT REFERENCES Regiao(idRegiao) ON DELETE CASCADE,
    nomeMonstro VARCHAR(50) NOT NULL,
    vidaMonstro INT NOT NULL,
    danoMonstro INT NOT NULL,
    defMonstro INT NOT NULL,
    quantidadeOuro INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Boss (
    idMonstro INT PRIMARY KEY REFERENCES Monstro(idMonstro) ON DELETE CASCADE,
    nomeMonstro VARCHAR(50) NOT NULL,
    vidaMonstro INT NOT NULL,
    danoMonstro INT NOT NULL,
    defMonstro INT NOT NULL,
    mulBoss DECIMAL(5, 2) NOT NULL,
    idItem INT REFERENCES Item(idItem) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Classe (
    idClasse INT PRIMARY KEY,
    nomeClasse VARCHAR(50) NOT NULL,
    mulFisico DECIMAL(5, 2) NOT NULL,
    mulMagico DECIMAL(5, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Personagem (
    idPersonagem SERIAL PRIMARY KEY,
    nomePersonagem VARCHAR(50) NOT NULL,
    staminaAtualPersonagem INT NOT NULL,
    vidaAtualPersonagem INT NOT NULL,
    staminaBasePersonagem INT NOT NULL,
    vidaBasePersonagem INT NOT NULL,
    defensePersonagem INT NOT NULL,
    ataqueFisico INT NOT NULL,
    ataqueMagico INT NOT NULL,
    idClasse INT REFERENCES Classe(idClasse) ON DELETE SET NULL,
    idSala INT REFERENCES Sala(idSala) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Save (
    idUsuario INT REFERENCES Usuario(idUsuario) ON DELETE CASCADE,
    idPersonagem INT REFERENCES Personagem(idPersonagem) ON DELETE CASCADE,
    PRIMARY KEY (idUsuario, idPersonagem)
);

CREATE TABLE IF NOT EXISTS Habilidade (
    idHabilidade SERIAL PRIMARY KEY,
    nomeHabilidade VARCHAR(50) NOT NULL,
    danoFisico INT NOT NULL,
    danoMagico INT NOT NULL,
    custoStamina INT NOT NULL,
    custoCooldown INT NOT NULL,
    idClasse INT REFERENCES Classe(idClasse) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Inventario (
    idInventario SERIAL PRIMARY KEY,
    espacoDisponivel INT NOT NULL,
    capacidade INT NOT NULL,
    quantidadeOuro INT NOT NULL,
    idPersonagem INT REFERENCES Personagem(idPersonagem) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS itemPersonagem (
    idItemPersonagem SERIAL PRIMARY KEY,
    idInventario INT REFERENCES Inventario(idInventario) ON DELETE CASCADE,
    quantidadeItem INT NOT NULL,
    idItem INT REFERENCES Item(idItem) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS itemSala (
    idItemSala SERIAL PRIMARY KEY,
    idSala INT REFERENCES Sala(idSala) ON DELETE CASCADE,
    quantidadeItem INT NOT NULL,
    idItem INT REFERENCES Item(idItem) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Consumivel (
    idItem INT PRIMARY KEY REFERENCES Item(idItem) ON DELETE CASCADE,
    nomeItem VARCHAR(50) NOT NULL,
    valorItem DECIMAL(5, 2) NOT NULL,
    incrementoVidaAtual INT NOT NULL,
    incrementoStaminaAtual INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Equipavel (
    idItem INT PRIMARY KEY REFERENCES Item(idItem) ON DELETE CASCADE,
    nomeItem VARCHAR(50) NOT NULL,
    valorItem DECIMAL(5, 2) NOT NULL,
    incrementoVidaBase INT NOT NULL,
    incrementoDefesa INT NOT NULL,
    mulFisico DECIMAL(5, 2) NOT NULL,
    mulMagico DECIMAL(5, 2) NOT NULL,
    equipado CHAR(1) CHECK (equipado IN ('s', 'n'))
);
