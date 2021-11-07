var user = {
  user: "admin",
  pwd: "adminasfiweefw",
  roles: [
    {
      role: "dbOwner",
      db: "nosql",
    },
  ],
};
db.createUser(user);
db.createCollection("users");
