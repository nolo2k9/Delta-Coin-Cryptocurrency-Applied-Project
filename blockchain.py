from block import Block


class Blockchain:
    """
    This class contains the code for the blockchain.
    A blockchain is a public ledger that contains transactional data.
    These transactions are implemented as a list of blocks.
    Blocks are data sets of transactions.
    """
    # init method

    def __init__(self):
        # Every blockchain instance will contain a chain attribute implemented as a list. The list will be a list of blocks,consisting of block items
        self.chain = []

    # Method to enable the blockchain to add blocks
    def add_block(self, data):
        # instance of block class containing the data
        # append this block and data to the chain
        self.chain.append(Block(data))
    # Test

    def __repr__(self):
        # returning a formatted string containing the local chain list
        return f'Blockchain: {self.chain}'


def main():
    # Experimenting adding blocks
    blockchain = Blockchain()
    blockchain.add_block('One')
    blockchain.add_block('Two')
    blockchain.add_block('Three')

    print(blockchain)
    print(f'blockchain.py __name__:{__name__}')


if __name__ == '__main__':
    main()
