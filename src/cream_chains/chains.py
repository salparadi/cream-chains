import os
from eth_typing import ChainId
from eth_utils.address import to_checksum_address

from .abis import *

chain_factories = {
    "arbitrum": {
        "v2": {
            "camelot": {
                "factory_address": to_checksum_address(
                    "0x6EcCab422D763aC031210895C81787E87B43A652"
                ),
                "pool_init_hash": "a856464ae65f7619087bc369daaf7e387dae1e5af69cfa7935850ebf754b04c1",
                "factory_deployment_block": 35061163,
                "fee": 3000,
            },
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0xc35DADB65012eC5796536bD9864eD8773aBc74C4"
                ),
                "pool_init_hash": "0xe18a34eb0e04b04f7a0ac29a6e80748dca96319b42c54d679cb821dca90c6303",
                "factory_deployment_block": 70,
                "fee": 3000,
            },
        },
        "v3": {
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0x1af415a1EbA07a4986a52B6f2e7dE7003D82231e"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0x8516944E89f296eb6473d79aED1Ba12088016c9e"
                ),
                "factory_deployment_block": 75998697,
            },
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x1F98431c8aD98523631AE4a59f267346ea31F984"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0xbfd8137f7d1516D3ea5cA83523914859ec47F573"
                ),
                "factory_deployment_block": 165,
            },
        },
    },
    "avalanche": {
        "v2": {
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0xc35DADB65012eC5796536bD9864eD8773aBc74C4"
                ),
                "pool_init_hash": "0xe18a34eb0e04b04f7a0ac29a6e80748dca96319b42c54d679cb821dca90c6303",
                "factory_deployment_block": 506190,
                "fee": 3000,
            },
            "traderjoe": {
                "factory_address": to_checksum_address(
                    "0x9Ad6C38BE94206cA50bb0d90783181662f0Cfa10"
                ),
                "pool_init_hash": "0x68c513b5446532a422cc30be2fad6d70336473f62c353084fbc7355683a33708",
                "factory_deployment_block": 2486392,
                "fee": 3000,
            },
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x9e5A52f57b3038F1B8EeE45F28b3C1967e22799C"
                ),
                "pool_init_hash": "0x96e8ac4277198ff8b6f785478aa9a39f403cb768dd02cbee326c3e7da348845f",
                "factory_deployment_block": 37767795,
                "fee": 3000,
            },
        },
        "v3": {
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0x3e603C14aF37EBdaD31709C4f848Fc6aD5BEc715"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0xDdC1b5920723F774d2Ec2C3c9355251A20819776"
                ),
                "factory_deployment_block": 28186391,
            },
        },
    },
    "base": {
        "v2": {
            "baseswap": {
                "factory_address": to_checksum_address(
                    "0xFDa619b6d20975be80A10332cD39b9a4b0FAa8BB"
                ),
                "pool_init_hash": "0xb618a2730fae167f5f8ac7bd659dd8436d571872655bcb6fd11f2158c8a64a3b",
                "factory_deployment_block": 2059124,
                "fee": 3000,
            },
            "pancakeswap": {
                "factory_address": to_checksum_address(
                    "0x02a84c1b3BBD7401a5f7fa98a384EBC70bB5749E"
                ),
                "pool_init_hash": "0x57224589c67f3f30a6b0d7a1b54cf3153ab84563bc609ef41dfb34f8b2974d2d",
                "factory_deployment_block": 2910387,
                "fee": 3000,
            },
            "rocketswap": {
                "factory_address": to_checksum_address(
                    "0x1B8128c3A1B7D20053D10763ff02466ca7FF99FC"
                ),
                "pool_init_hash": "0x32d4b730a0e562de3cbe5b62b68f3312e55fab8d511c97e70928147f673be977",
                "factory_deployment_block": 1732443,
                "fee": 3000,
            },
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0x71524B4f93c58fcbF659783284E38825f0622859"
                ),
                "pool_init_hash": "0xe18a34eb0e04b04f7a0ac29a6e80748dca96319b42c54d679cb821dca90c6303",
                "factory_deployment_block": 2631214,
                "fee": 3000,
            },
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x8909Dc15e40173Ff4699343b6eB8132c65e18eC6"
                ),
                "pool_init_hash": "0x96e8ac4277198ff8b6f785478aa9a39f403cb768dd02cbee326c3e7da348845f",
                "factory_deployment_block": 6601915,
                "fee": 3000,
            },
        },
        "v3": {
            "pancakeswap": {
                "factory_address": to_checksum_address(
                    "0x0BFbCF9fa4f9C56B0F40a671Ad40E0805A091865"
                ),
                "pool_init_hash": "0x6ce8eb472fa82df5469c6ab6d485f17c3ad13c8cd7af59b3d4a8026c5ce0f7e2",
                "tick_lens": to_checksum_address(
                    "0x9a489505a00cE272eAa5e07Dba6491314CaE3796"
                ),
                "factory_deployment_block": 2912007,
            },
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0xc35DADB65012eC5796536bD9864eD8773aBc74C4"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0xF4d73326C13a4Fc5FD7A064217e12780e9Bd62c3"
                ),
                "factory_deployment_block": 1759510,
            },
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x33128a8fC17869897dcE68Ed026d694621f6FDfD"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0x0CdeE061c75D43c82520eD998C23ac2991c9ac6d"
                ),
                "factory_deployment_block": 1371680,
            },
        },
    },
    "ethereum": {
        "v2": {
            "pancakeswap": {
                "factory_address": to_checksum_address(
                    "0x1097053Fd2ea711dad45caCcc45EfF7548fCB362"
                ),
                "pool_init_hash": "0x57224589c67f3f30a6b0d7a1b54cf3153ab84563bc609ef41dfb34f8b2974d2d",
                "factory_deployment_block": 15614590,
                "fee": 3000,
            },
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac"
                ),
                "pool_init_hash": "0xe18a34eb0e04b04f7a0ac29a6e80748dca96319b42c54d679cb821dca90c6303",
                "factory_deployment_block": 10794229,
                "fee": 3000,
            },
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
                ),
                "pool_init_hash": "0x96e8ac4277198ff8b6f785478aa9a39f403cb768dd02cbee326c3e7da348845f",
                "factory_deployment_block": 10000835,
                "fee": 3000,
            },
        },
        "v3": {
            "pancakeswap": {
                "factory_address": to_checksum_address(
                    "0x0BFbCF9fa4f9C56B0F40a671Ad40E0805A091865"
                ),
                "pool_init_hash": "0x6ce8eb472fa82df5469c6ab6d485f17c3ad13c8cd7af59b3d4a8026c5ce0f7e2",
                "tick_lens": to_checksum_address(
                    "0x9a489505a00cE272eAa5e07Dba6491314CaE3796"
                ),
                "factory_deployment_block": 16950686,
            },
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0xbACEB8eC6b9355Dfc0269C18bac9d6E2Bdc29C4F"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0xFB70AD5a200d784E7901230E6875d91d5Fa6B68c"
                ),
                "factory_deployment_block": 16955547,
            },
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x1F98431c8aD98523631AE4a59f267346ea31F984"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0xbfd8137f7d1516D3ea5cA83523914859ec47F573"
                ),
                "factory_deployment_block": 12369621,
            },
        },
    },
    "optimism": {
        "v2": {
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x0c3c1c532F1e39EdF36BE9Fe0bE1410313E074Bf"
                ),
                "pool_init_hash": "0x5b83bdbcc56b2e630f2807bbadd2b0c21619108066b92a58de081261089e9ce5",
                "factory_deployment_block": 112197986,
                "fee": 3000,
            },
        },
        "v3": {
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0x9c6522117e2ed1fE5bdb72bb0eD5E3f2bdE7DBe0"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0x0367a647A68f304f2A6e453c25033a4249d7F2C6"
                ),
                "factory_deployment_block": 85432013,
            },
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x1F98431c8aD98523631AE4a59f267346ea31F984"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0xbfd8137f7d1516D3ea5cA83523914859ec47F573"
                ),
                "factory_deployment_block": 1,
            },
        },
    },
    "polygon": {
        "v2": {
            "quickswap": {
                "factory_address": to_checksum_address(
                    "0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32"
                ),
                "pool_init_hash": "0x96e8ac4277198ff8b6f785478aa9a39f403cb768dd02cbee326c3e7da348845f",
                "fee": 3000,
                "factory_deployment_block": 4931780,
            },
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0xc35DADB65012eC5796536bD9864eD8773aBc74C4"
                ),
                "pool_init_hash": "0xe18a34eb0e04b04f7a0ac29a6e80748dca96319b42c54d679cb821dca90c6303",
                "fee": 3000,
                "factory_deployment_block": 11333218,
            },
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x9e5A52f57b3038F1B8EeE45F28b3C1967e22799C"
                ),
                "pool_init_hash": "0x96e8ac4277198ff8b6f785478aa9a39f403cb768dd02cbee326c3e7da348845f",
                "fee": 3000,
                "factory_deployment_block": 49948178,
            },
        },
        "v3": {
            "sushiswap": {
                "factory_address": to_checksum_address(
                    "0x917933899c6a5F8E37F31E19f92CdBFF7e8FF0e2"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0x9fdeA1412e50D78B25aCE4f96d35801647Fdf7dA"
                ),
                "factory_deployment_block": 41024971,
            },
            "uniswap": {
                "factory_address": to_checksum_address(
                    "0x1F98431c8aD98523631AE4a59f267346ea31F984"
                ),
                "pool_init_hash": "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54",
                "tick_lens": to_checksum_address(
                    "0xbfd8137f7d1516D3ea5cA83523914859ec47F573"
                ),
                "factory_deployment_block": 22757547,
            },
        },
    },
}

chain_routers = {
    "arbitrum": {
        to_checksum_address("0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"): {
            "name": "Sushiswap: Router",
            "exchange": "sushiswap",
            "abi": UNISWAP_V2_ROUTER2_ABI,
            "w3": None,
            "factories": {2: chain_factories["arbitrum"]["v2"]["sushiswap"]},
        },
        to_checksum_address("0x8A21F6768C1f8075791D08546Dadf6daA0bE820c"): {
            "name": "Sushiswapv3: Router",
            "exchange": "sushiswap",
            "abi": UNISWAP_V3_ROUTER2_ABI,
            "w3": None,
            "factories": {3: chain_factories["arbitrum"]["v3"]["sushiswap"]},
        },
        to_checksum_address("0xE592427A0AEce92De3Edee1F18E0157C05861564"): {
            "name": "Uniswapv3: Router",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER_ABI,
            "w3": None,
            "factories": {3: chain_factories["arbitrum"]["v3"]["uniswap"]},
        },
        to_checksum_address("0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"): {
            "name": "Uniswapv3: Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER2_ABI,
            "w3": None,
            "factories": {3: chain_factories["arbitrum"]["v3"]["uniswap"]},
        },
        to_checksum_address("0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B"): {
            "name": "Universal Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_UNIVERSAL_ROUTER_ABI,
            "w3": None,
            "factories": {3: chain_factories["arbitrum"]["v3"]["uniswap"]},
        },
        to_checksum_address("0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD"): {
            "name": "Universal Router 3",
            "exchange": "uniswap",
            "abi": UNISWAP_UNIVERSAL_ROUTER2_ABI,
            "w3": None,
            "factories": {3: chain_factories["arbitrum"]["v3"]["uniswap"]},
        },
        to_checksum_address("0x5E325eDA8064b456f4781070C0738d849c824258"): {
            "name": "Universal Router 4",
            "exchange": "uniswap",
            "abi": UNISWAP_UNIVERSAL_ROUTER2_ABI,
            "w3": None,
            "factories": {3: chain_factories["arbitrum"]["v3"]["uniswap"]},
        },
    },
    "avalanche": {
        to_checksum_address("0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"): {
            "name": "Sushiswap: Router",
            "exchange": "sushiswap",
            "abi": AVALANCHE_SUSHISWAP_ROUTER_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["avalanche"]["v2"]["sushiswap"],
            },
        },
        to_checksum_address("0x60aE616a2155Ee3d9A68541Ba4544862310933d4"): {
            "name": "TraderJoe: Router",
            "exchange": "traderjoe",
            "abi": TRADERJOE_ROUTER_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["avalanche"]["v2"]["traderjoe"],
            },
        },
    },
    "base": {
        to_checksum_address("0x0389879e0156033202C44BF784ac18fC02edeE4f"): {
            "name": "BaseSwapV4: Router",
            "exchange": "baseswap",
            "abi": BASESWAP_ROUTER4_ABI,
            "w3": None,
            "factories": {2: chain_factories["base"]["v2"]["baseswap"]},
        },
        to_checksum_address("0x6BDED42c6DA8FBf0d2bA55B2fa120C5e0c8D7891"): {
            "name": "Sushiswapv2: Router",
            "exchange": "sushiswap",
            "abi": UNISWAP_V2_ROUTER2_ABI,
            "w3": None,
            "factories": {2: chain_factories["base"]["v2"]["sushiswap"]},
        },
        to_checksum_address("0xFB7eF66a7e61224DD6FcD0D7d9C3be5C8B049b9f"): {
            "name": "Sushiswapv3: Router",
            "exchange": "sushiswap",
            "abi": UNISWAP_V3_ROUTER2_ABI,
            "w3": None,
            "factories": {3: chain_factories["base"]["v3"]["sushiswap"]},
        },
        to_checksum_address("0xE592427A0AEce92De3Edee1F18E0157C05861564"): {
            "name": "Uniswapv3: Router",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER_ABI,
            "w3": None,
            "factories": {3: chain_factories["base"]["v3"]["uniswap"]},
        },
        to_checksum_address("0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"): {
            "name": "Uniswapv3: Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER2_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["base"]["v2"]["uniswap"],
                3: chain_factories["base"]["v3"]["uniswap"],
            },
        },
        to_checksum_address("0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD"): {
            "name": "Universal Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_UNIVERSAL_ROUTER2_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["base"]["v2"]["uniswap"],
                3: chain_factories["base"]["v3"]["uniswap"],
            },
        },
    },
    "ethereum": {
        to_checksum_address("0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F"): {
            "name": "Sushiswap: Router",
            "exchange": "sushiswap",
            "abi": UNISWAP_V2_ROUTER2_ABI,
            "w3": None,
            "factories": {2: chain_factories["ethereum"]["v2"]["sushiswap"]},
        },
        to_checksum_address("0xf164fC0Ec4E93095b804a4795bBe1e041497b92a"): {
            "name": "Uniswapv2: Router",
            "exchange": "uniswap",
            "abi": UNISWAP_V2_ROUTER_ABI,
            "w3": None,
            "factories": {2: chain_factories["ethereum"]["v2"]["uniswap"]},
        },
        to_checksum_address("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"): {
            "name": "Uniswapv2: Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_V2_ROUTER2_ABI,
            "w3": None,
            "factories": {2: chain_factories["ethereum"]["v2"]["uniswap"]},
        },
        to_checksum_address("0xE592427A0AEce92De3Edee1F18E0157C05861564"): {
            "name": "Uniswapv3: Router",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER_ABI,
            "w3": None,
            "factories": {3: chain_factories["ethereum"]["v3"]["uniswap"]},
        },
        to_checksum_address("0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"): {
            "name": "Uniswapv3: Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER2_ABI,
            "w3": None,
            "factories": {3: chain_factories["ethereum"]["v3"]["uniswap"]},
        },
        to_checksum_address("0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B"): {
            "name": "Universal Router 1",
            "exchange": "uniswap",
            "abi": UNISWAP_UNIVERSAL_ROUTER_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["ethereum"]["v2"]["uniswap"],
                3: chain_factories["ethereum"]["v3"]["uniswap"],
            },
        },
        to_checksum_address("0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD"): {
            "name": "Universal Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_UNIVERSAL_ROUTER2_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["ethereum"]["v2"]["uniswap"],
                3: chain_factories["ethereum"]["v3"]["uniswap"],
            },
        },
        to_checksum_address("0x3F6328669a86bef431Dc6F9201A5B90F7975a023"): {
            "name": "Universal Router 3",
            "exchange": "uniswap",
            "abi": UNISWAP_UNIVERSAL_ROUTER3_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["ethereum"]["v2"]["uniswap"],
                3: chain_factories["ethereum"]["v3"]["uniswap"],
            },
        },
    },
    "optimism": {
        to_checksum_address("0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"): {
            "name": "Sushiswapv2: Router",
            "exchange": "sushiswap",
            "abi": UNISWAP_V2_ROUTER2_ABI,
            "w3": None,
            "factories": {3: chain_factories["optimism"]["v3"]["sushiswap"]},
        },
        to_checksum_address("0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"): {
            "name": "Sushiswapv3: Router",
            "exchange": "sushiswap",
            "abi": UNISWAP_V3_ROUTER2_ABI,
            "w3": None,
            "factories": {3: chain_factories["optimism"]["v3"]["sushiswap"]},
        },
        to_checksum_address("0xE592427A0AEce92De3Edee1F18E0157C05861564"): {
            "name": "Uniswapv3: Router",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER_ABI,
            "w3": None,
            "factories": {3: chain_factories["optimism"]["v3"]["uniswap"]},
        },
        to_checksum_address("0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"): {
            "name": "Uniswapv3: Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER2_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["optimism"]["v2"]["uniswap"],
                3: chain_factories["optimism"]["v3"]["uniswap"],
            },
        },
        to_checksum_address("0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD"): {
            "name": "Universal Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_UNIVERSAL_ROUTER2_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["optimism"]["v2"]["uniswap"],
                3: chain_factories["optimism"]["v3"]["uniswap"],
            },
        },
    },
    "polygon": {
        to_checksum_address("0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff"): {
            "name": "Quickswapv2: Router",
            "exchange": "quickswap",
            "abi": UNISWAP_V2_ROUTER2_ABI,
            "w3": None,
            "factories": {2: chain_factories["polygon"]["v2"]["quickswap"]},
        },
        to_checksum_address("0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"): {
            "name": "Sushiswapv2: Router",
            "exchange": "sushiswap",
            "abi": UNISWAP_V2_ROUTER2_ABI,
            "w3": None,
            "factories": {2: chain_factories["polygon"]["v2"]["sushiswap"]},
        },
        to_checksum_address("0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"): {
            "name": "Sushiswapv3: Router",
            "exchange": "sushiswap",
            "abi": UNISWAP_V3_ROUTER2_ABI,
            "w3": None,
            "factories": {3: chain_factories["polygon"]["v3"]["sushiswap"]},
        },
        to_checksum_address("0xE592427A0AEce92De3Edee1F18E0157C05861564"): {
            "name": "Uniswapv3: Router",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER_ABI,
            "w3": None,
            "factories": {3: chain_factories["polygon"]["v3"]["uniswap"]},
        },
        to_checksum_address("0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"): {
            "name": "Uniswapv3: Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_V3_ROUTER2_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["polygon"]["v2"]["uniswap"],
                3: chain_factories["polygon"]["v3"]["uniswap"],
            },
        },
        to_checksum_address("0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD"): {
            "name": "Universal Router 2",
            "exchange": "uniswap",
            "abi": UNISWAP_UNIVERSAL_ROUTER2_ABI,
            "w3": None,
            "factories": {
                2: chain_factories["polygon"]["v2"]["uniswap"],
                3: chain_factories["polygon"]["v3"]["uniswap"],
            },
        },
    },
}

chain_aggregators = {
    "arbitrum": None,
    "avalanche": None,
    "base": None,
    "ethereum": {
        to_checksum_address("0x111111125421cA6dc452d289314280a0f8842A65"): {
            "name": "1Inch v6: Router",
            "aggregator": "oneinch",
            "abi": ONE_INCH_ROUTER_V6_ABI,
            "w3": None,
        },
        to_checksum_address("0x1111111254EEB25477B68fb85Ed929f73A960582"): {
            "name": "1Inch v5: Router",
            "aggregator": "oneinch",
            "abi": ONE_INCH_ROUTER_V5_ABI,
            "w3": None,
        },
        to_checksum_address("0x1111111254fb6c44bAC0beD2854e76F90643097d"): {
            "name": "1Inch v4: Router",
            "aggregator": "oneinch",
            "abi": ONE_INCH_ROUTER_V4_ABI,
            "w3": None,
        },
        to_checksum_address("0xDEF171Fe48CF0115B1d80b88dc8eAB59176FEe57"): {
            "name": "Paraswap: Router",
            "aggregator": "paraswap",
            "abi": PARASWAP_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0x4FF0dEC5f9a763Aa1E5C2a962aa6f4eDFeE4f9eA"): {
            "name": "Paraswap Uniswap V2: Router",
            "aggregator": "paraswap",
            "abi": PARASWAP_UNISWAP_V2_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0xdffd706ee98953d3d25a3b8440E34e3A2C9BEb2C"): {
            "name": "Paraswap Directswap: Router",
            "aggregator": "paraswap",
            "abi": PARASWAP_DIRECTSWAP_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0xbD7b550d2E7571383d84ACF597a00d341E5C406E"): {
            "name": "Paraswap Multipath: Router",
            "aggregator": "paraswap",
            "abi": PARASWAP_MULTIPATH_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0x881D40237659C251811CEC9c364ef91dC08D300C"): {
            "name": "Metamask: Router",
            "aggregator": "metamask",
            "abi": METAMASK_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0x6131B5fae19EA4f9D964eAc0408E4408b66337b5"): {
            "name": "KyberSwap v2: Router",
            "aggregator": "kyberswap",
            "abi": KYBERSWAP_ROUTER_V2_ABI,
            "w3": None,
        },
        to_checksum_address("0x00000047bB99ea4D791bb749D970DE71EE0b1A34"): {
            "name": "TransitSwap v5: Router",
            "aggregator": "transitswap",
            "abi": TRANSITSWAP_ROUTER_V5_ABI,
            "w3": None,
        },
        to_checksum_address("0xdef1c0ded9bec7f1a1670819833240f027b25eff"): {
            "name": "0x: Router",
            "aggregator": "zerox",
            "abi": ZEROX_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0xf9b30557AfcF76eA82C04015D80057Fa2147Dfa9"): {
            "name": "0x Uniswap v2: Router",
            "aggregator": "zerox",
            "abi": ZEROX_UNISWAP_V2_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0x0e992C001E375785846EEb9cd69411B53f30f24B"): {
            "name": "0x Uniswap v3: Router",
            "aggregator": "zerox",
            "abi": ZEROX_UNISWAP_V3_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0x27a688d1F6D2794D0580F04DfC0fcafD0a40c59D"): {
            "name": "0x Metatransaction: Router",
            "aggregator": "zerox",
            "abi": ZEROX_METATRANSACTION_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0xc8c10815bE32536685d12cE8305425163f0c6897"): {
            "name": "0x Multiplex: Router",
            "aggregator": "zerox",
            "abi": ZEROX_MULTIPLEX_ROUTER_ABI,
            "w3": None,
        },
        to_checksum_address("0x44A6999Ec971cfCA458AFf25A808F272f6d492A2"): {
            "name": "0x Transform: Router",
            "aggregator": "zerox",
            "abi": ZEROX_TRANSFORM_ROUTER_ABI,
            "w3": None,
        },
    },
    "optimism": None,
    "polygon": None,
}

chain_data = {
    "arbitrum": {
        "name": "arbitrum",
        "sequencer_uri": "wss://arb1.arbitrum.io/feed",
        "chain_id": ChainId.ARB1,
        "wrapped_token": to_checksum_address(
            "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1"
        ),
        "wrapped_token_oracle": to_checksum_address(
            "0x639Fe6ab55C921f74e7fac1ee960C0B6293ba612"
        ),
        "aggregators": chain_aggregators["arbitrum"],
        "factories": chain_factories["arbitrum"],
        "routers": chain_routers["arbitrum"],
        "node": os.getenv("ARBITRUM_NODE", "alchemy"),
        "ape_network": os.getenv("ARBITRUM_APE_NETWORK", "arbitrum:mainnet:alchemy"),
        "http_uri": os.getenv(
            "ARBITRUM_HTTP_URI",
            "https://arb-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_ARBITRUM_MAINNET_ALCHEMY_API_KEY"),
        ),
        "websocket_uri": os.getenv(
            "ARBITRUM_WEBSOCKET_URI",
            "wss://arb-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_BASE_MAINNET_ALCHEMY_API_KEY"),
        ),
    },
    "avalanche": {
        "name": "avalanche",
        "sequencer_uri": None,
        "chain_id": ChainId.AVAX,
        "wrapped_token": to_checksum_address(
            "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7"
        ),
        "wrapped_token_oracle": to_checksum_address(
            "0x0A77230d17318075983913bC2145DB16C7366156"
        ),
        "aggregators": chain_aggregators["avalanche"],
        "factories": chain_factories["avalanche"],
        "routers": chain_routers["avalanche"],
        "node": os.getenv("AVALANCHE_NODE", "infura"),
        "ape_network": os.getenv("AVALANCHE_APE_NETWORK", "avalanche:mainnet:infura"),
        "http_uri": os.getenv(
            "AVALANCHE_HTTP_URI",
            "https://avalanche-mainnet.infura.io/v3/"
            + os.getenv("WEB3_INFURA_PROJECT_ID"),
        ),
        "websocket_uri": os.getenv(
            "AVALANCHE_WEBSOCKET_URI",
            "wss://avalanche-mainnet.infura.io/ws/v3/"
            + os.getenv("WEB3_INFURA_PROJECT_ID"),
        ),
    },
    "base": {
        "name": "base",
        "sequencer_uri": None,
        "chain_id": ChainId.BASE,
        "wrapped_token": to_checksum_address(
            "0x4200000000000000000000000000000000000006"
        ),
        "wrapped_token_oracle": to_checksum_address(
            "0x71041dddad3595F9CEd3DcCFBe3D1F4b0a16Bb70"
        ),
        "aggregators": chain_aggregators["base"],
        "factories": chain_factories["base"],
        "routers": chain_routers["base"],
        "node": os.getenv("BASE_NODE", "alchemy"),
        "ape_network": os.getenv("BASE_APE_NETWORK", "base:mainnet:alchemy"),
        "http_uri": os.getenv(
            "BASE_HTTP_URI",
            "https://base-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_BASE_MAINNET_ALCHEMY_API_KEY"),
        ),
        "websocket_uri": os.getenv(
            "BASE_WEBSOCKET_URI",
            "wss://base-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_BASE_MAINNET_ALCHEMY_API_KEY"),
        ),
    },
    "ethereum": {
        "name": "ethereum",
        "sequencer_uri": None,
        "chain_id": ChainId.ETH,
        "wrapped_token": to_checksum_address(
            "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
        ),
        "wrapped_token_oracle": to_checksum_address(
            "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"
        ),
        "aggregators": chain_aggregators["ethereum"],
        "factories": chain_factories["ethereum"],
        "routers": chain_routers["ethereum"],
        "node": os.getenv("ETHEREUM_NODE", "alchemy"),
        "ape_network": os.getenv("ETHEREUM_APE_NETWORK", "ethereum:mainnet:alchemy"),
        "http_uri": os.getenv(
            "ETHEREUM_HTTP_URI",
            "https://eth-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_ETHEREUM_MAINNET_ALCHEMY_API_KEY"),
        ),
        "websocket_uri": os.getenv(
            "ETHEREUM_WEBSOCKET_URI",
            "wss://eth-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_ETHEREUM_MAINNET_ALCHEMY_API_KEY"),
        ),
    },
    "optimism": {
        "name": "optimism",
        "sequencer_uri": None,
        "chain_id": ChainId.OETH,
        "wrapped_token": to_checksum_address(
            "0x4200000000000000000000000000000000000006"
        ),
        "wrapped_token_oracle": to_checksum_address(
            "0x13e3Ee699D1909E989722E753853AE30b17e08c5"
        ),
        "aggregators": chain_aggregators["optimism"],
        "factories": chain_factories["optimism"],
        "routers": chain_routers["optimism"],
        "node": os.getenv("OPTIMISM_NODE", "alchemy"),
        "ape_network": os.getenv("OPTIMISM_APE_NETWORK", "optimism:mainnet:alchemy"),
        "http_uri": os.getenv(
            "OPTIMISM_HTTP_URI",
            "https://opt-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_OPTIMISM_MAINNET_ALCHEMY_API_KEY"),
        ),
        "websocket_uri": os.getenv(
            "OPTIMISM_WEBSOCKET_URI",
            "wss://opt-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_OPTIMISM_MAINNET_ALCHEMY_API_KEY"),
        ),
    },
    "polygon": {
        "name": "polygon",
        "sequencer_uri": None,
        "chain_id": ChainId.MATIC,
        "wrapped_token": to_checksum_address(
            "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619"
        ),
        "wrapped_token_oracle": to_checksum_address(
            "0xF9680D99D6C9589e2a93a78A04A279e509205945"
        ),
        "aggregators": chain_aggregators["polygon"],
        "factories": chain_factories["polygon"],
        "routers": chain_routers["polygon"],
        "node": os.getenv("POLYGON_NODE", "alchemy"),
        "ape_network": os.getenv("POLYGON_APE_NETWORK", "polygon:mainnet:alchemy"),
        "http_uri": os.getenv(
            "POLYGON_HTTP_URI",
            "https://polygon-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_POLYGON_MAINNET_ALCHEMY_API_KEY"),
        ),
        "websocket_uri": os.getenv(
            "POLYGON_WEBSOCKET_URI",
            "wss://polygon-mainnet.g.alchemy.com/v2/"
            + os.getenv("WEB3_POLYGON_MAINNET_ALCHEMY_API_KEY"),
        ),
    },
}
