import sqlite3

class sudokuData():
    def __init__(self):
        self.con = sqlite3.connect('Sudokuboards.db')
        self.cur = self.con.cursor()

    def createTable(self, tableName, vars):
        """Supply the name of the table in tableName and a list of strings representing the columns and their types in vars
        Example: createTable(Customer,['ID integer PRIMARY KEY','Age integer','Name text NOT NULL'])"""

        table = "CREATE TABLE IF NOT EXISTS "+tableName+'('
        for i in vars:
            table += i
            table += ','

        table[table.len()-1] = ')'
        table += ';'
        
        self.cur.execute(table)
        

    def addRow(self,board):
        sql=''' INSERT INTO Boards(Board,Solved)
              VALUES(?,?) '''

        self.cur.execute(sql,(board,0))
        self.con.commit()

        return self.cur.lastrowid

    def solvedPuzzle(self,puzzleID):
        sql = ''' UPDATE Boards
              SET Solved = 1
              WHERE ID = ?'''

        self.cur.execute(sql,puzzleID)
        self.con.commit()
