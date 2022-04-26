
-- ******************************************************** --
--                                                          --
--   QUERIES CRIADAS COM O DIAGRAMA, USAR COMO REFERÊNCIA   --
--                                                          -- 
-- ******************************************************** -- 

CREATE TABLE IF NOT EXISTS "Addresses"
(
 "ID"          bigserial NOT NULL,
 "Country"     varchar(50) NOT NULL,
 "State"       varchar(70) NOT NULL,
 "City"        varchar(100) NOT NULL,
 "Street"      varchar(150) NOT NULL,
 "Number"      integer NULL,
 "Complement"  varchar(50) NULL,
 "Postal Code" varchar(10) NOT NULL,
 CONSTRAINT "PK_51" PRIMARY KEY ( "ID" )
);

CREATE TABLE IF NOT EXISTS "Bids"
(
 "ID"       bigserial NOT NULL,
 "Price"    decimal NOT NULL,
 "User ID"  bigserial NOT NULL,
 "Bid time" date NOT NULL,
 CONSTRAINT "PK_33" PRIMARY KEY ( "ID" ),
 CONSTRAINT "FK_111" FOREIGN KEY ( "User ID" ) REFERENCES "Users" ( "ID" )
);

CREATE INDEX "FK_113" ON "Bids"
(
 "User ID"
);


CREATE TABLE IF NOT EXISTS "Categories"
(
 "ID"          bigserial NOT NULL,
 "Name"        varchar(50) NOT NULL,
 "Description" varchar(240) NOT NULL,
 CONSTRAINT "PK_37" PRIMARY KEY ( "ID" )
);


CREATE TABLE IF NOT EXISTS "Partners"
(
 "ID"      bigserial NOT NULL,
 "Name"    varchar(100) NOT NULL,
 "Address" bigserial NOT NULL,
 "CNPJ"    varchar(14) NOT NULL,
 "About"   varchar(240) NOT NULL,
 CONSTRAINT "PK_45" PRIMARY KEY ( "ID" ),
 CONSTRAINT "FK_90" FOREIGN KEY ( "Address" ) REFERENCES "Addresses" ( "ID" )
);

CREATE INDEX "FK_92" ON "Partners"
(
 "Address"
);

CREATE TABLE IF NOT EXISTS "Products"
(
 "ID"             bigserial NOT NULL,
 "Name"           varchar(70) NOT NULL,
 "Highest Bid"    bigserial NOT NULL,
 "Category ID"    bigserial NOT NULL,
 "Partner ID"     bigserial NOT NULL,
 "Description"    varchar(1200) NOT NULL,
 "Starting Price" decimal NOT NULL,
 "Auction Start"  date NOT NULL,
 "Auction End"    date NOT NULL,
 "Active"         boolean NOT NULL,
 CONSTRAINT "PK_18" PRIMARY KEY ( "ID" ),
 CONSTRAINT "FK_99" FOREIGN KEY ( "Partner ID" ) REFERENCES "Partners" ( "ID" ),
 CONSTRAINT "FK_108" FOREIGN KEY ( "Category ID" ) REFERENCES "Categories" ( "ID" ),
 CONSTRAINT "FK_119" FOREIGN KEY ( "Highest Bid" ) REFERENCES "Bids" ( "ID" )
);

CREATE INDEX "FK_101" ON "Products"
(
 "Partner ID"
);

CREATE INDEX "FK_110" ON "Products"
(
 "Category ID"
);

CREATE INDEX "FK_121" ON "Products"
(
 "Highest Bid"
);


CREATE TABLE IF NOT EXISTS "Users"
(
 "ID"            bigserial NOT NULL,
 "Name"          varchar(60) NOT NULL,
 "Address"       bigserial NOT NULL,
 "CPF"           varchar(11) NOT NULL,
 "Date of Birth" date NOT NULL,
 CONSTRAINT "PK_13" PRIMARY KEY ( "ID" ),
 CONSTRAINT "FK_87" FOREIGN KEY ( "Address" ) REFERENCES "Addresses" ( "ID" )
);

CREATE INDEX "FK_89" ON "Users"
(
 "Address"
);

