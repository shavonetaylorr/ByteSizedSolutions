INSERT INTO Ambassadors (StuID, name, phone_number, experienced) VALUES
(1467518, 'Alasia Villanella', '(870) 513-3932', 1),
(6131633, 'Alexis Balkissoon', '(336) 806-3457', 0),
(8548415, 'Alexisse Hyppolite', '(306) 764-0607', 1),
(9307739, 'Cailyn Everitt', '(903) 346-7955', 0),
(4773408, 'Cesarina Perez Encarnacion', '(728) 367-8302', 1),
(7620391, 'Chi Chi Okoroji', '(542) 541-6750', 1),
(4724615, 'Delaia Baez', '(487) 801-5483', 1),
(6267592, 'Elary Rasmy', '(978) 608-5434', 1),
(9800389, 'Eric Soares', '(773) 684-0650', 1),
(7402867, 'Gianna Rodriguez', '(958) 770-3530', 0),
(8476432, 'Janai Campbell', '(495) 816-8037', 0),
(8453736, 'Jason Penk', '(794) 909-1805', 0),
(2620448, 'John Gold', '(996) 889-4861', 0),
(3834460, 'Jordan Frazier', '(411) 577-3123', 0),
(6126538, 'Joseph Abramson', '(246) 934-5587', 0),
(8374575, 'Joylyn Perez', '(481) 324-3515', 1),
(4621238, 'Juliana Ross', '(789) 825-3556', 0),
(4331092, 'Kendra Smith', '(325) 231-5658', 1),
(3267791, 'Kiera Redfern', '(540) 534-0176', 1),
(9672189, 'Melia Marte', '(794) 260-5905', 1),
(7740985, 'Natalie Stannard', '(523) 794-6227', 1),
(5823875, 'Salma Abdallah', '(679) 901-2544', 0),
(6990981, 'Samaya Harris', '(253) 207-1744', 0),
(2748495, 'Sara Ngoy', '(649) 666-6300', 1),
(2439229, 'Savannah Diaz', '(321) 237-6838', 0),
(7450123, 'Shanice Marlow', '(624) 957-3076', 0),
(4496930, 'Suzy Ndandji', '(435) 932-0289', 1);

SELECT * FROM Ambassadors;
use 2024F_oparak;
SHOW TABLES;

SELECT * FROM Availability;
LOAD DATA LOCAL INFILE 'Availability.csv'
INTO TABLE Availability
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
