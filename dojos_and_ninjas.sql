SELECT * FROM dojos_and_ninjas.dojos;

-- Query: Create 3 new dojos

INSERT into dojos
	(name)
Values
	('dojo_1'),
    ('dojo_2'),
    ('dojo_3');



-- Query: Delete the 3 dojos you just created

DELETE FROM dojos WHERE id = 1;
DELETE FROM dojos WHERE id = 2;
DELETE FROM dojos WHERE id = 3;



-- Query: Create 3 more dojos
INSERT into dojos
	(name)
Values
	('dojo_1'),
    ('dojo_2'),
    ('dojo_3');

   


-- Query: Create 3 ninjas that belong to the first dojo

-- adding ninjas
INSERT into ninjas 
	(first_name, last_name, age, dojo_id)
values
	-- ('Moe', 'Howard', '40', 10),
    -- ('Larry', 'Howard', '43', 10);
     ('Curly', 'Howard', '38', 10);
    SELECT * FROM ninjas WHERE dojo_id = 10;
    SELECT * FROM dojos_and_ninjas.ninjas;




-- Query: Create 3 ninjas that belong to the second dojo
INSERT into ninjas 
	(first_name, last_name, age, dojo_id)
values
	-- ('Alvin', 'Deville', '12', 11);
   -- ('Simon', 'Deville', '12', 11);
     ('Theodore', 'Deville', '12', 11);
    SELECT * FROM ninjas WHERE dojo_id = 11;
    SELECT * FROM dojos_and_ninjas.ninjas;






-- Query: Create 3 ninjas that belong to the third dojo

INSERT into ninjas 
	(first_name, last_name, age, dojo_id)
values
	-- ('Jon', 'Carter', '25', 12);
   -- ('Brandon', 'Carter', '28', 12);
     ('Rob', 'Carter', '30', 12);
    SELECT * FROM ninjas WHERE dojo_id = 12;
    SELECT * FROM dojos_and_ninjas.ninjas;




-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas WHERE dojo_id = 10;





-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id = 12;




-- Query: Retrieve the last ninja's dojo
SELECT * FROM ninjas WHERE id = 9;





-- Query: Use a JOIN to retrieve the ninja with id 6 as well as the data from its dojo. Be sure to do this in one query using a join statement.

SELECT * FROM dojos.id
FROM dojos
INNER JOIN ninjas on dojos.id = ninjas.ninjasid;



-- Query: Use a JOIN to retrieve all the ninjas as well as that ninja's dojo, note, you will see repeated data on dojos as a dojo can have many ninjas!
