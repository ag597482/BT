CREATE TABLE IF NOT EXISTS users1
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, 
  name            VARCHAR(150) NOT NULL,               
  email           VARCHAR(150) NOT NULL,                
  gender           VARCHAR(150) NOT NULL,               
  age             INT unsigned NOT NULL,                
  PRIMARY KEY     (id)                                 
);
