# MoMo Payment Tracker
*Simple mobile money transaction tracking for everyday Rwandans*

## African Context

In Rwanda and some countries across Africa, mobile money has revolutionized financial inclusion, with millions of people using services like MTN MoMo, Airtel Money, and M-Pesa daily. However, many users struggle to keep track of their transactions, leading to:

- **Lost receipts** and difficulty reconciling accounts
- **Unexpected charges** due to unclear fee structures
- **Budget challenges** from lack of spending visibility
- **Disputes** that are hard to resolve without transaction history

**MoMo Payment Tracker** addresses these challenges by providing a simple, offline-first tool that helps users:
- Track all mobile money transactions in one place
- Understand transaction fees before completing transfers
- Monitor spending patterns and maintain budgets
- Keep a reliable record for personal or small business use

This is particularly valuable for:
- Small business owners who receive many daily payments
- Students managing limited budgets
- Families coordinating shared expenses
- Anyone wanting better control of their mobile money usage

## Team Members

- **Yusuf** - DevOps Engineer & Backend Developer 
- **Yvette** - Backend Developer & QA Lead 
- **Simeon** - Full-Stack Developer & Database Manager 

## Project Overview

MoMo Payment Tracker is a command-line application that simulates and tracks mobile money transactions. The application provides a user-friendly interface for managing four core transaction types: sending money, receiving money, buying airtime, and withdrawing cash.

Built with Python, the application uses an in-memory database for transaction storage, making it fast and simple to use without requiring complex database setup. The colored terminal interface provides clear visual feedback, making it accessible even for users with limited technical experience.

The application calculates realistic transaction fees based on Rwanda's mobile money fee structure, helping users understand the true cost of their transactions before committing. All transactions are timestamped and stored with complete details, providing a comprehensive transaction history that can be viewed and analyzed at any time.

## Target Users

- **Small Business Owners**: Market vendors, shop owners, and service providers who process multiple mobile money transactions daily
- **Students**: Young people managing pocket money and tracking expenses
- **Families**: Households coordinating shared expenses and money transfers
- **Mobile Money Agents**: Agents who need to track and reconcile daily transactions
- **Budget-Conscious Individuals**: Anyone wanting better visibility into their mobile money spending

## Core Features

### Feature 1: Transaction Management
Complete transaction lifecycle management including sending money, receiving payments, buying airtime, and withdrawing cash. Each transaction includes automatic fee calculation, balance validation, and confirmation prompts to prevent errors.

### Feature 2: Real-Time Balance Tracking
Instant balance updates after every transaction with clear display of current funds. The system starts users with RWF 10,000 and automatically adjusts balances based on transaction types (debits for sends/withdrawals, credits for receives).

### Feature 3: Comprehensive Transaction History
View all transactions in a formatted table showing ID, type, amount, recipient/sender, timestamp, and status. Search and filter capabilities help users find specific transactions quickly.

### Feature 4: Smart Fee Calculator
Transparent fee calculation based on Rwanda's mobile money fee structure. Users see the exact fee before confirming transactions, helping them make informed decisions about transfer amounts.

### Feature 5: Transaction Analytics
Summary dashboard displaying total transactions, total money sent, total money received, and current balance. Helps users understand their mobile money usage patterns at a glance.

## Technology Stack

- **Backend**: Python 3.9+
- **CLI Enhancement**: Colorama (colored terminal output)
- **Data Presentation**: Tabulate (formatted tables)
- **Database**: In-memory Python data structures (lists and dictionaries)
- **Version Control**: Git & GitHub
- **Development Environment**: VS Code

## Getting Started

### Prerequisites

Before running this application, ensure you have:

- **Python 3.9 or higher** installed on your system
  - Check by running: `python --version` or `python3 --version`
  - Download from: https://www.python.org/downloads/
- **Git** installed for version control
  - Check by running: `git --version`
  - Download from: https://git-scm.com/downloads/
- **Terminal/Command Prompt** access
- **Text editor** (VS Code recommended)

### Installation

Follow these steps to set up the project on your local machine:

#### Step 1: Clone the Repository

```bash
git clone https://github.com/yusufmolumo/momo-payment-tracker.git
cd momo-payment-tracker
```

#### Step 2: Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt.

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `colorama` - for colored terminal output
- `tabulate` - for formatted table display

#### Step 4: Verify Installation

Check that all dependencies are installed:
```bash
pip list
```

You should see `colorama` and `tabulate` in the list.

### Run the Application

Start the MoMo Payment Tracker:

```bash
python -m app.main
```

Or alternatively:

```bash
python app/main.py
```

You should see the welcome screen with the main menu.

## Usage

### Basic Workflow

1. **Start the application** - Run the command above
2. **Choose an option** - Enter a number (1-8) from the menu
3. **Follow prompts** - Enter requested information (phone numbers, amounts, etc.)
4. **Confirm transactions** - Review details before confirming
5. **View results** - See updated balance and transaction confirmation

### Example Usage Scenarios

#### Sending Money
```
Choose option 1
Enter recipient: 0788123456
Enter amount: 5000
Description: Lunch money
Confirm: yes
✅ Transaction successful!
```

#### Checking Balance
```
Choose option 6
💵 CURRENT BALANCE: RWF 10,000
```

#### Viewing Transaction History
```
Choose option 5
[Displays formatted table of all transactions]
```

### Understanding Fees

The application uses Rwanda's typical mobile money fee structure:

| Amount Range | Fee |
|--------------|-----|
| Up to 1,000 | 50 |
| 1,001 - 5,000 | 100 |
| 5,001 - 10,000 | 200 |
| 10,001 - 50,000 | 500 |
| Above 50,000 | 1,000 |

**Note**: Receiving money and buying airtime have no fees in this application.

## 📁 Project Structure

```
momo-payment-tracker/
│
├── app/                          # Main application package
│   ├── __init__.py              # Package initializer
│   ├── main.py                  # Main application entry point & CLI interface
│   ├── transaction.py           # Transaction class and fee calculator
│   └── database.py              # In-memory database manager
│
├── tests/                        # Test files (to be implemented)
│   └── __init__.py
│
├── .github/                      # GitHub configuration
│   └── CODEOWNERS               # Code ownership definitions
│
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── LICENSE                       # MIT License
```

## Links

- **GitHub Repository**: https://github.com/yusufmolumo/momo-payment-tracker
- **Project Board**: https://github.com/yusufmolumo/momo-payment-tracker/projects/1
- **Issues**: https://github.com/yusufmolumo/momo-payment-tracker/issues


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
