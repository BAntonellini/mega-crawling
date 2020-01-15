INSERT INTO cuits_crawled(empr_id, empr_cuit, empr_tel)
SELECT "index", empr_cuit, empr_tel from cuits_existent