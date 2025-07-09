"""SELECT s.*, i.*
FROM studente AS s
JOIN iscrizione AS i
  ON s.matricola = i.matricola
WHERE i.codins = '01NATPG';
"""
