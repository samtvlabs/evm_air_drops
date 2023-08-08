## Original Requirements
The boss has requested the creation of a command-line interface (CLI) that can airdrop tokens to Ethereum Virtual Machine (EVM) chains.

## Product Goals
```python
[
    "Create a CLI tool that can airdrop tokens to EVM chains",
    "Ensure the tool is user-friendly and easy to use",
    "Ensure the tool is secure and reliable"
]
```

## User Stories
```python
[
    "As a user, I want to input the number of tokens I want to airdrop so that the correct amount is distributed",
    "As a user, I want to specify the EVM chain I want to airdrop tokens to",
    "As a user, I want to receive confirmation that the airdrop was successful",
    "As a user, I want to be able to see a list of all past airdrops I have made",
    "As a user, I want to be able to cancel an airdrop if I made a mistake"
]
```

## Competitive Analysis
```python
[
    "Airdrop Tool A: Offers similar functionality but lacks user-friendly interface",
    "Airdrop Tool B: Provides airdrop functionality but only for specific EVM chains",
    "Airdrop Tool C: Offers airdrop functionality but lacks robust security measures",
    "Airdrop Tool D: Provides airdrop functionality but lacks a history feature",
    "Airdrop Tool E: Offers similar functionality but lacks a cancellation feature"
]
```

## Competitive Quadrant Chart
```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    "Airdrop Tool A": [0.3, 0.6]
    "Airdrop Tool B": [0.45, 0.23]
    "Airdrop Tool C": [0.57, 0.69]
    "Airdrop Tool D": [0.78, 0.34]
    "Airdrop Tool E": [0.40, 0.34]
    "Our Target Product": [0.6, 0.7]
```

## Requirement Analysis
The product should be a CLI tool that can airdrop tokens to EVM chains. It should be user-friendly, secure, and reliable. The tool should allow users to input the number of tokens they want to airdrop, specify the EVM chain, receive confirmation of successful airdrops, see a list of past airdrops, and cancel an airdrop if necessary.

## Requirement Pool
```python
[
    ("User can input the number of tokens to airdrop", "P0"),
    ("User can specify the EVM chain for the airdrop", "P0"),
    ("User receives confirmation of successful airdrops", "P0"),
    ("User can see a list of past airdrops", "P1"),
    ("User can cancel an airdrop", "P1")
]
```

## UI Design draft
As a CLI tool, the interface will be text-based. The tool will prompt the user for the necessary information (number of tokens, EVM chain) and provide clear instructions for each step. Confirmation messages will be displayed after successful actions, and error messages will be displayed in case of issues. The history of airdrops will be displayed in a clear, easy-to-read format.

## Anything UNCLEAR
The specific EVM chains that the tool should support are not specified. We will assume for now that it should support all major EVM chains.