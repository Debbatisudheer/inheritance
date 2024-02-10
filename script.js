class Account {
    constructor(account_number, balance) {
        this.account_number = account_number;
        this.balance = balance;
    }

    deposit(amount) {
        this.balance += amount;
        console.log(`Deposit of $${amount} successful. New balance: $${this.balance}`);
    }

    withdraw(amount) {
        if (amount <= this.balance) {
            this.balance -= amount;
            console.log(`Withdrawal of $${amount} successful. New balance: $${this.balance}`);
        } else {
            console.log("Insufficient funds.");
        }
    }

    display_balance() {
        console.log(`Account Balance: $${this.balance}`);
    }
}

class SavingsAccount extends Account {
    constructor(account_number, balance, interest_rate) {
        super(account_number, balance);
        this.interest_rate = interest_rate;
    }

    add_interest() {
        let interest_amount = this.balance * this.interest_rate;
        this.deposit(interest_amount);
        console.log(`Interest of $${interest_amount} added. New balance: $${this.balance}`);
    }
}

function deposit(accountType) {
    // Dummy logic for depositing funds
    let amount = 0;
    switch (accountType) {
        case 'savings':
            amount = 200;
            break;
        case 'fixedDeposit':
            amount = 500; // Assuming a fixed deposit requires a minimum deposit of $500
            break;
        case 'personalLoan':
            alert("Cannot deposit into a loan account.");
            return;
        case 'carLoan':
            alert("Cannot deposit into a loan account.");
            return;
        default:
            alert("Invalid account type.");
            return;
    }
    alert(`Deposited $${amount} into ${accountType} account.`);
    // Update account balance display
    const balanceElement = document.getElementById(`${accountType}Balance`);
    const currentBalance = parseFloat(balanceElement.innerText.split('$')[1]);
    balanceElement.innerText = `Balance: $${currentBalance + amount}`;
}

function withdraw(accountType) {
    // Dummy logic for withdrawing funds
    let amount = 0;
    switch (accountType) {
        case 'checking':
            amount = 100; // Withdraw $100 from checking account
            break;
        case 'personalLoan':
            amount = 200; // Pay $200 installment for personal loan
            break;
        case 'carLoan':
            amount = 300; // Pay $300 installment for car loan
            break;
        default:
            alert("Invalid account type.");
            return;
    }
    alert(`Withdrawn $${amount} from ${accountType} account.`);
    // Update account balance display
    const balanceElement = document.getElementById(`${accountType}Balance`);
    const currentBalance = parseFloat(balanceElement.innerText.split('$')[1]);
    balanceElement.innerText = `Balance: $${currentBalance - amount}`;
}

// Function to add interest to savings account
function addInterest() {
    // Create a new SavingsAccount object
    const savingsAccount = new SavingsAccount("SA001", 1000, 0.05);
    // Add interest to the account
    savingsAccount.add_interest();
}