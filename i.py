from main import Block
from Chain import Chain


chain = Chain()
chain.get_genesis_block()
loop = True
while loop ==True:

    n = input("name")
    l = input("second name")
    dp = input("doctor or patient?")
    data = [n,l,dp]
    chain.add_block(data)
    new = input("Enter another?")
    if new =='n':
        print(chain.get_chain_size())
        chain.verify()
        chain.print_block()
        loop = False
