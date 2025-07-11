import mysql from 'mysql2'
mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'yearup24',
    database: 'dealershipworkshop'
}).promise()

pool.query('SELECT * FROM inventory')