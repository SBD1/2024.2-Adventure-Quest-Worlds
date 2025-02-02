-- Função de gatilho que define NEW.vidaAtual com base no vidaMonstro do monstro
CREATE OR REPLACE FUNCTION update_vida_atual()
RETURNS TRIGGER AS $update_vida_atual$
DECLARE
    vida_instancia INT;
BEGIN
    SELECT COALESCE(
        (SELECT vidaMonstro FROM Minion WHERE idMonstro = NEW.idMonstro),
        (SELECT vidaMonstro FROM Boss   WHERE idMonstro = NEW.idMonstro)
    )
    INTO vida_instancia;

    IF NEW.vidaAtual IS NULL THEN
        NEW.vidaAtual := vida_instancia;
    END IF;

    RETURN NEW;
END;
$update_vida_atual$ LANGUAGE plpgsql;

CREATE TRIGGER instancia_atualizada
BEFORE INSERT ON instanciaMonstro
FOR EACH ROW
EXECUTE FUNCTION update_vida_atual();
