import argparse
from airdrop import Airdrop
from database import Database

def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(prog='evm_airdrop_cli')
    subparsers = parser.add_subparsers(dest='command')

    # Create the parser for the "airdrop" command
    parser_airdrop = subparsers.add_parser('airdrop', help='airdrop tokens to an EVM chain')
    parser_airdrop.add_argument('evm_chain', type=str, help='the EVM chain to airdrop tokens to')
    parser_airdrop.add_argument('number_of_tokens', type=int, help='the number of tokens to airdrop')

    # Create the parser for the "history" command
    parser_history = subparsers.add_parser('history', help='view the history of airdrops')

    # Parse the arguments
    args = parser.parse_args()

    # Create the database
    db = Database()

    if args.command == 'airdrop':
        # Create the airdrop
        airdrop = Airdrop(args.evm_chain, args.number_of_tokens)

        # Add the airdrop to the database
        db.add_airdrop(airdrop)

        # Perform the airdrop
        airdrop.airdrop_tokens()

        # Update the airdrop in the database
        db.add_airdrop(airdrop)

        print(f"Airdropped {airdrop.number_of_tokens} tokens to {airdrop.evm_chain}.")
    elif args.command == 'history':
        # Get the history of airdrops
        airdrops = db.get_all_airdrops()

        for airdrop in airdrops:
            print(airdrop)

if __name__ == '__main__':
    main()
