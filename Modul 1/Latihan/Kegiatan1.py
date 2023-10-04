#Fungsi Penjumlahan
def add(x,y):
    return x+y

#Fungsi Pengurangan
def minus(x,y):
    return x-y

#Fungsi Perkalian
def mult(x,y):
    return x*y

#Fungsi Pembagian
def div(x,y):
    if y==0:
        print("Operasi pembagian tidak bisa jika penyebutnya 0")
    else:
        return x/y

#Tree
def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        if operator == '+':
            return add(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':

            return div(tree(left_operand), tree(right_operand))
    
# Contoh pohon ekspresi
expression_tree = ((2, '+', 3), '*', (5, '-', 1))
# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)
    
print("Hasil evaluasi pohon ekspresi:", result)