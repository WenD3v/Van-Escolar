DELIMITER //

CREATE TRIGGER atualiza_status_pagar
BEFORE INSERT ON CONTAS_PAGAR
FOR EACH ROW
BEGIN
    IF NEW.VALOR_PAGO IS NOT NULL AND NEW.VALOR_PAGO = NEW.VALOR_TITULO THEN
        SET NEW.STATUS_TITULO = 'quitado';
    ELSE
        SET NEW.STATUS_TITULO = 'em aberto';
    END IF;
END;
//

CREATE TRIGGER atualiza_status_pagar_update
BEFORE UPDATE ON CONTAS_PAGAR
FOR EACH ROW
BEGIN
    IF NEW.VALOR_PAGO IS NOT NULL AND NEW.VALOR_PAGO = NEW.VALOR_TITULO THEN
        SET NEW.STATUS_TITULO = 'quitado';
    ELSE
        SET NEW.STATUS_TITULO = 'em aberto';
    END IF;
END;
//

CREATE TRIGGER atualiza_status_receber
BEFORE INSERT ON CONTAS_RECEBER
FOR EACH ROW
BEGIN
    IF NEW.VALOR_PAGO IS NOT NULL AND NEW.VALOR_PAGO = NEW.VALOR_TITULO THEN
        SET NEW.STATUS_TITULO = 'quitado';
    ELSE
        SET NEW.STATUS_TITULO = 'em aberto';
    END IF;
END;
//

CREATE TRIGGER atualiza_status_receber_update
BEFORE UPDATE ON CONTAS_RECEBER
FOR EACH ROW
BEGIN
    IF NEW.VALOR_PAGO IS NOT NULL AND NEW.VALOR_PAGO = NEW.VALOR_TITULO THEN
        SET NEW.STATUS_TITULO = 'quitado';
    ELSE
        SET NEW.STATUS_TITULO = 'em aberto';
    END IF;
END;
//
DELIMITER ;
