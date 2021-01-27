DROP TABLE IF EXISTS rounds;
CREATE TABLE IF NOT EXISTS rounds         
(id INTEGER  PRIMARY KEY, 
initialpot INTEGER, 
finalpot INTEGER);

  
DROP TABLE IF EXISTS plays;  
CREATE TABLE IF NOT EXISTS plays         
(id INTEGER PRIMARY KEY, 
round_id INTEGER, 
bet INTEGER, 
result integer, 
FOREIGN KEY (round_id) REFERENCES rounds (id) 
ON DELETE CASCADE ON UPDATE NO ACTION);

    
INSERT INTO rounds (initialpot, finalpot) VALUES 
(100,0),
(100,0),
(100,0),
(100,120),
(100,80),
(100,400);

    
INSERT INTO plays (round_id, bet, result) VALUES 
(1,50,55),
(1,100,44),
(1,400,56),
(2,10,55),
(2,120,56),
(3,1,41),
(3,1,64),
(3,1,51),
(3,1,56),
(3,1,44),
(3,1,44),
(3,1,13),
(3,1,22),
(3,1,46),
(3,1,65),
(3,1,55),
(3,1,23),
(3,1,61),
(3,1,42),
(3,1,55),
(3,1,16),
(3,1,63),
(3,1,34),
(3,1,33),
(3,10,14),
(3,10,56),
(3,10,35),
(3,10,29),
(3,10,14),
(4,10,66),
(5,10,43),
(5,10,61),
(6,50,22),
(6,100,44);
    