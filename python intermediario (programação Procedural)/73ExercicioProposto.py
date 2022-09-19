

carrinho = []
carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 20.50))
carrinho.append(('produto 4', '15'))

print(carrinho)

produto, preco = carrinho [0]
print(produto, preco)

total = [float((x[1])) for x in carrinho]
print(f'Total: {total}')
print(f'Resultado do exercicio: {sum(total)}')


print()
print('-------------------')
print()

total = [(x, y) for x, y in carrinho]
print(total) #Vai imprimir: [('produto 1', 30), ('produto 2', 20)]

print()
print('-------------------')
print()

# total = []
# for produto in carrinho:
#     total.append(produto[1])
# print(sum(total))

