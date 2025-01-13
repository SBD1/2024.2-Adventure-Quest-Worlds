CREATE TABLE IF NOT EXISTS Classes (
    id_classe SERIAL PRIMARY KEY,
    nome_classe VARCHAR(10) NOT NULL,
    mul_fisico FLOAT NOT NULL,
    mul_magico FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS Sala (
    id_sala SERIAL PRIMARY KEY,
    nome_sala VARCHAR(10) NOT NULL,
    sala_norte INT,
    sala_sul INT,
    sala_leste INT,
    sala_oeste INT
);

CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario SERIAL PRIMARY KEY,
    login VARCHAR(20) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    qtd_personagens INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Item (
    id_item SERIAL PRIMARY KEY,
    nome_item VARCHAR(30) NOT NULL,
    valor_item INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Monstro (
    id_monstro SERIAL PRIMARY KEY,
    nome_monstro VARCHAR(30) NOT NULL,
    vida_monstro INT NOT NULL,
    dano_monstro INT NOT NULL,
    def_monstro INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Personagem (
    id_personagem SERIAL PRIMARY KEY,
    nome_personagem VARCHAR(30) NOT NULL,
    def_personagem INT NOT NULL,
    vida_atual INT NOT NULL,
    vida_base INT NOT NULL,
    stamina_atual INT NOT NULL,
    stamina_base INT NOT NULL,
    ataque_fisico INT NOT NULL,
    ataque_magico INT NOT NULL,
    id_classe INT NOT NULL,
    id_sala INT NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_classe) REFERENCES Classes(id_classe),
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);