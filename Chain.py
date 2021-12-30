import copy
import datetime

from main import Block


class Chain():

    def __init__(self):
        self.blocks = [self.get_genesis_block()]

    def get_genesis_block(self):
        return Block(0,
                     datetime.datetime.utcnow(),
                     'Genisis',
                     'arb')
    def add_block(self, data):
        self.blocks.append(Block(len(self.blocks),
                                 datetime.datetime.utcnow(),
                                 data,
                                 self.blocks[len(self.blocks)-1].hash))

        print(Block.__hash__(self))
    def print_block(self):
        for i in range(len(self.blocks)):
           print(self.blocks[i].hashing())


    def get_chain_size(self):
        return len(self.blocks)-1


    def verify(self, verbose=True):
        flag = True
        for i in range(1, len(self.blocks)):
            if self.blocks[i].index != i:
                flag = False
                if verbose:
                    print(f'Wrong hash at block {i}.')
            if self.blocks[i-1].timestamp >= self.blocks[i].timestamp:
                flag = False
                if verbose:
                    print(f'Backdating at block {i}.')
        return flag

    def fork(self, head='latest'):
        if head in ['latest', 'whole', 'all']:
            return copy.deepcopy(self)
        else:
            c = copy.deepcopy(self)
            c.blocks = c.blocks[0:head+1]
            return c

    def get_root(self, chain_2):
        min_chain_size = min(self.get_chain_size(), chain_2.get_chain_size())
        for i in range(1, min_chain_size+1):
            if self.blocks[i] != chain_2.blockls[i]:
                return self.fork(i-1)
        return self.fork(min_chain_size)

