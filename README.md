# Bevm Ecosystem Project List

Welcome to the Bevm Ecosystem Project List! This repository is dedicated to listing projects within the Bevm ecosystem. If you have a project that you'd like to include, please follow the instructions below to submit it.

## How to Submit Your Project

To submit your project to this list, please follow these steps:

1. **Fork the Repository**: Start by forking this repository to your account.
2. **Add Your Project Information**: Fill in the details of your project according to the format provided below.
3. **Submit a Pull Request**: Once you've added your project, create a Pull Request for review.

## Submission Format

When adding your project, please use the following format:

- **Project Type**: Choose from Bridge, Dev Tools, Infra, NFT, Wallet, Social, Identity, Defi, Data Service, CEX, Security, Funding, Launchpad, Entertainment, Inscription.
- **Project Icon**: Upload your project logo in the asset file, then copy the path and fill it in json.

Here is an example in JSON format:

```json
{
  "bevm": [
    {
      "name": "OmniBTC",
      "types": ["Bridge", "Tools"],
      "icon": "https://raw.githubusercontent.com/btclayer2/ecosystem/main/assets/omnibtc.png",
      "description": "The first decentralized full-chain financial platform.",
      "link": "https://www.omnibtc.finance/"
    }
  ],
  "bevm-testnet": [
    {
      "name": "OmniBTC",
      "types": ["DEFI", "Tools"],
      "icon": "https://raw.githubusercontent.com/btclayer2/ecosystem/main/assets/omnibtc.png",
      "description": "The first decentralized full-chain financial platform.",
      "link": "https://www.omnibtc.finance/"
    }
  ]
}

