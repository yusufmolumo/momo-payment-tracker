"""
Transaction class for handling mobile money transactions
"""
from datetime import datetime


class Transaction:
    """Represents a mobile money transaction"""
    
    def __init__(self, trans_id, trans_type, amount, recipient, description=""):
        """
        Initialize a transaction
        
        Args:
            trans_id: Unique transaction ID
            trans_type: Type of transaction ('send', 'receive', 'airtime', 'withdraw')
            amount: Amount in RWF
            recipient: Recipient phone number or name
            description: Optional transaction description
        """
        self.trans_id = trans_id
        self.trans_type = trans_type
        self.amount = float(amount)
        self.recipient = recipient
        self.description = description
        self.timestamp = datetime.now()
        self.status = "completed"
    
    def to_dict(self):
        """Convert transaction to dictionary"""
        return {
            'id': self.trans_id,
            'type': self.trans_type,
            'amount': self.amount,
            'recipient': self.recipient,
            'description': self.description,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'status': self.status
        }
    
    def __str__(self):
        """String representation of transaction"""
        return f"Transaction {self.trans_id}: {self.trans_type} RWF {self.amount:,.0f} to {self.recipient}"
    
    @staticmethod
    def calculate_fee(amount, trans_type):
        """
        Calculate transaction fee based on amount and type
        Rwanda MoMo typical fee structure (simplified)
        """
        if trans_type == 'receive':
            return 0
        elif trans_type == 'airtime':
            return 0
        elif amount <= 1000:
            return 50
        elif amount <= 5000:
            return 100
        elif amount <= 10000:
            return 200
        elif amount <= 50000:
            return 500
        else:
            return 1000