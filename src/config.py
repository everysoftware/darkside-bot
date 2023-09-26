from dataclasses import dataclass


@dataclass
class Config:
    token: str = 'YOUR_TOKEN'
    pay_token: str = 'YOUR_PAY_TOKEN'
