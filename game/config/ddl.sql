CREATE TABLE IF NOT EXISTS Item (
    idItem INT PRIMARY KEY,
    nomeItem VARCHAR(50) NOT NULL,
    tipoItem BOOLEAN NOT NULL,
    precoItem INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Usuario (
    idUsuario SERIAL PRIMARY KEY,
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    qtdPersonagem INT CHECK (qtdPersonagem BETWEEN 0 AND 3)
);

CREATE TABLE IF NOT EXISTS Monstro (
    idMonstro INT PRIMARY KEY,
    nomeMonstro VARCHAR(50) NOT NULL,
    vidaMonstro INT NOT NULL,
    danoMonstro INT NOT NULL,
    defMonstro INT NOT NULL,
    tipoMonstro BOOLEAN NOT NULL,
    qntXP INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Regiao (
    idRegiao INT PRIMARY KEY,
    nomeRegiao VARCHAR(50) NOT NULL,
    descricaoRegiao VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS Sala (
    idSala INT PRIMARY KEY,
    idRegiao INT REFERENCES Regiao(idRegiao) ON DELETE SET NULL,
    nomeSala VARCHAR(50) NOT NULL,
    salaNorte INT,
    salaSul INT,
    salaLeste INT,
    salaOeste INT
);

CREATE TABLE IF NOT EXISTS instanciaMonstro (
    idInstanciaMonstro INT PRIMARY KEY,
    idMonstro INT REFERENCES Monstro(idMonstro) ON DELETE CASCADE,
    idRegiao INT REFERENCES Regiao(idRegiao) ON DELETE SET NULL,
    vidaAtual INT NOT NULL,
    idSala INT REFERENCES Sala(idSala) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Minion (
    idMonstro INT PRIMARY KEY REFERENCES Monstro(idMonstro) ON DELETE CASCADE,
    quantidadeOuro INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Boss (
    idMonstro INT PRIMARY KEY REFERENCES Monstro(idMonstro) ON DELETE CASCADE,
    idItem INT REFERENCES Item(idItem) ON DELETE SET NULL,
    mulBoss DECIMAL(5, 2) NOT NULL,
    fraseBoss VARCHAR(200) NOT NULL

);

CREATE TABLE IF NOT EXISTS Classe (
    idClasse INT PRIMARY KEY,
    nomeClasse VARCHAR(50) NOT NULL,
    mulFisico DECIMAL(5, 2) NOT NULL,
    mulMagico DECIMAL(5, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS Personagem (
    idPersonagem SERIAL PRIMARY KEY,
    idClasse INT REFERENCES Classe(idClasse) ON DELETE SET NULL,
    idSala INT REFERENCES Sala(idSala) ON DELETE SET NULL,
    nomePersonagem VARCHAR(50) NOT NULL,
    nivel INT NOT NULL,
    xpAtual INT NOT NULL,
    staminaAtualPersonagem INT NOT NULL,
    vidaAtualPersonagem INT NOT NULL,
    staminaBasePersonagem INT NOT NULL,
    vidaBasePersonagem INT NOT NULL,
    defensePersonagem INT NOT NULL,
    ataqueFisico INT NOT NULL,
    ataqueMagico INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Save (
    idUsuario INT REFERENCES Usuario(idUsuario) ON DELETE CASCADE,
    idPersonagem INT REFERENCES Personagem(idPersonagem) ON DELETE CASCADE,
    PRIMARY KEY (idUsuario, idPersonagem)
);

CREATE TABLE IF NOT EXISTS Habilidade (
    idHabilidade INT PRIMARY KEY,
    nomeHabilidade VARCHAR(50) NOT NULL,
    danoFisico INT NOT NULL,
    danoMagico INT NOT NULL,
    custoStamina INT NOT NULL,
    custoCooldown INT NOT NULL,
    idClasse INT REFERENCES Classe(idClasse) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Inventario (
    idPersonagem INT PRIMARY KEY REFERENCES Personagem(idPersonagem) ON DELETE CASCADE,
    espacoDisponivel INT NOT NULL,
    capacidade INT NOT NULL,
    quantidadeOuro INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Consumivel (
    idItem INT PRIMARY KEY REFERENCES Item(idItem) ON DELETE CASCADE,
    incrementoVidaAtual INT NOT NULL,
    incrementoStaminaAtual INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Equipavel (
    idItem INT PRIMARY KEY REFERENCES Item(idItem) ON DELETE CASCADE,
    incrementoVidaBase INT NOT NULL,
    incrementoDefesa INT NOT NULL,
    mulFisico DECIMAL(5, 2) NOT NULL,
    mulMagico DECIMAL(5, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS InstanciaItem (
    idInstanciaItem INT PRIMARY KEY,
    idItem INT REFERENCES Item(idItem) ON DELETE CASCADE,
    quantidadeItem INT NOT NULL,
    equipado BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS Missao (
    idMissao INT PRIMARY KEY,
    nomeMissao VARCHAR(50) NOT NULL,
    descricaoMissao VARCHAR(200) NOT NULL,
    xpRecompensa INT NOT NULL,
    idItem INT REFERENCES Item(idItem) ON DELETE SET NULL,
    idMissaoSeguinte INT REFERENCES Missao(idMissao) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS ObjetivoMissao (
    idObjetivo INT PRIMARY KEY,
    idMissao INT REFERENCES Missao(idMissao) ON DELETE CASCADE,
    descricaoObjetivo VARCHAR(200) NOT NULL,
    quantidadeMeta INT NOT NULL,
    idMonstro INT REFERENCES Monstro(idMonstro) ON DELETE SET NULL,
    idSala INT REFERENCES Sala(idSala) ON DELETE SET NULL,
    idRegiao INT REFERENCES Regiao(idRegiao) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS ProgressoMissao (
    idPersonagem INT REFERENCES Personagem(idPersonagem) ON DELETE CASCADE,
    idObjetivoMissao INT REFERENCES ObjetivoMissao(idObjetivo) ON DELETE CASCADE,
    concluida BOOLEAN NOT NULL,
    progressoObjetivo INT NOT NULL 
);

CREATE TABLE IF NOT EXISTS Loja (
    idLoja INT PRIMARY KEY,
    idSala INT REFERENCES Sala(idSala) ON DELETE SET NULL,
    nomeLoja VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Catalogo (
    idLoja INT REFERENCES Loja(idLoja) ON DELETE CASCADE,
    idItem INT REFERENCES Item(idItem) ON DELETE CASCADE,
    PRIMARY KEY (idLoja, idItem)
);
