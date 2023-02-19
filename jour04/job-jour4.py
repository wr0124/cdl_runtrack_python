#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 08:24:13 2023

@author: wr0124
"""
#%% demo
def factorielle(n):
    if n>0:
        if n==0:
            f=1
        elif n==1:
            f=1
        else:
            f=n*factorielle(n-1)
    else:
        print("le nombre n doit etre un tntier positif")
        f=None
        
    return f

print(factorielle(2))
#%%

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%´Job 0.1
#Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre
# programme devra calculer x^n, où n est le nombre fourni par l’utilisateur, sans utiliser de
# fonction autre que les vôtres. Attention, vous ne devez utiliser ni while, ni for, ni foreach
# ni … boucle. Seulement de la récursivité


def powercal(x,n):
    if n>=0:
        if n==0:
            resultat =1
        elif n==1:
            resultat = x
        else:
            resultat = x*powercal(x,n-1)
    else:
        print("le nombre n doit etre un tntier positif")
        resultat=None
        
    return resultat


print( powercal(3,2) )


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%´Job 0.1
# # Créer un programme demandant à l’utilisateur de renseigner un nombre entier. Votre programme devra calculer x^n, 
# où n est le nombre fourni par l’utilisateur, sans utiliser de fonction autre que les vôtres. Attention, vous
#  ne devez utiliser ni while, ni for, ni foreach ni ... boucle. Seulement de la récursivité.
 


def check_ready(board, row, col, n):
    # Check row and column
    for i in range(n):
        if board[row][i] == "X" or board[i][col] == "X":
            return False
    
    # Check diagonals
    for i in range(n):
        for j in range(n):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == "X":
                    return False
    
    return True

def find_position(board, col, n):
    # when all queens have been placed
    if col == n:
        return True
    
    # Try placing queen in each row of current column
    for row in range(n):
        if check_ready(board, row, col, n):
            # Place n_th queen
            board[row][col] = "X"
            
            # Recursively solve rest of board
            if find_position(board, col+1, n):
                return True
            
            # no place for next step , so backward
            board[row][col] = "o"
    
    # Could not place queen in any row of current column
    return False

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

def main(n):
    # Initialize board with all zeros
    board = [["o" for i in range(n)] for j in range(n)]
    print("beginning ")
    print_board(board)
    # Solve  recursively
    if find_position(board, 0, n):
        print("end")
        print_board(board)
    else:
        print("No solution exists for n = ", n)

# Example 
main(8)
#%%%%%%%%%%%%%%Job 08 
# Créer un programme qui ouvre le fichier maze.mz et qui relie l'entrée du labyrinthe (en haut à gauche) a sa 
# sortie (en bas à droite). Le programme doit afficher le labyrinthe dans un fichier “maze-out.mz” ou les cases 
# à suivre pour atteindre la sortie sont représentées par des ‘X’. Le chemin doit être le plus court possible.
 

import numpy as np

fin = open('maze.mz.txt','r')
l=[]
for line in fin.readlines():
    l.append( [  x  for x in line.split() ] )
    
matrix_maze = np.empty((101, 151), dtype=object)
 
for i in range(len(l)):
    for j in l[i]:
        for k in range(len(j)):
            if j[k] == "#":
                matrix_maze[i][k]=1
            if j[k]== '.':
                matrix_maze[i][k]=0
   
print("size of maze " + str(matrix_maze.shape)   ) 


def find_shortest_path(matrix_maze, start, end):
    rows = len(matrix_maze)
    cols = len(matrix_maze[0])
    visited = [[False for j in range(cols)] for i in range(rows)]
    parent = [[None for j in range(cols)] for i in range(rows)]

    def dfs(node):
        if node == end:
            return True
        row, col = node
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for neighbor in neighbors:
            nrow, ncol = neighbor
            if nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols:
                continue
            if visited[nrow][ncol] or matrix_maze[nrow][ncol] == 1:
                continue
            visited[nrow][ncol] = True
            parent[nrow][ncol] = node
            if dfs(neighbor):
                return True
        return False

    visited[start[0]][start[1]] = True
    if dfs(start):
        path = []
        node = end
        while node != start:
            path.append(node)
            node = parent[node[0]][node[1]]
        path.append(start)
        path.reverse()
        return path
    else:
        return None

#test the maze
start = (0, 0)
end = (101,151)
shortest_path = find_shortest_path(matrix_maze, start, end)
if shortest_path:
    for row in range(len(matrix_maze)):
        for col in range(len(matrix_maze[0])):
            if (row, col) in shortest_path:
                print('X', end='')
            else:
                print(matrix_maze[row][col], end='')
        print()
else:
    print('No path found')








#%%%%%%


#%%%%

#%%%%%%%%%Job 15
# Écrire un programme qui demande à l’utilisateur de fournir une première chaîne de caractères, puis une seconde. 
# Le programme affiche 1 si les 2 chaines sont identiques ou 0 si les chaînes ne sont pas identiques. Les chaînes 
# ne sont constituées que de lettres minuscules. La deuxième chaîne de caractères peut contenir un ou plusieurs ‘ * ‘. 
# Chaque ‘ * ‘ peut remplacer 0 ou plusieurs caractères. Par exemple, si la chaîne 1 est “laplateforme” et la 
# chaine 2 “lap*”, le programme affiche 1 car l’ ‘ * ‘ remplace ‘ lateforme ‘. Si la chaîne 1 est “laplateforme” et 
# la chaîne 2 “l*a*pla*te*form***e” le programme renvoie 1 car les ‘ * ‘ ne remplace rien.
print("entre two string :")
print("string 1: ")
x1=input().lower()

print("string 2: ")
x2=input().lower()

def compare(chain1,chain2):
    if chain1 and (chain1[0] == chain2[0] or chain2[0]=="*"):
        return compare(chain1[1:],  chain2[1:])
    elif chain2[0]=="*":
        return compare(chain1,  chain2[1:])  or  compare(chain1[1:],  chain2)
    elif not chain1 and not chain2:
        return True
    
    elif not chain2:
        return True
    else:
        return False
    
test=compare(x1,x2)
if test:
    print("1")
else:
    print("2")
    

    
     
            
         
            
    
    