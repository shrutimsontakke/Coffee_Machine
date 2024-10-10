# Coffee Machine Project ☕️

Welcome to the **Coffee Machine Project**! This Python application simulates a coffee vending machine, allowing users to order their favorite coffee drinks. The machine efficiently manages its resources, processes payments, and offers a refill option to keep ingredients stocked.


<!--![Coffee Machine]() Replace with a relevant image URL -->

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Sample Interaction](#sample-interaction)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Features

- **Drink Options**: Choose from three delicious coffee drinks:
  - **Espresso**: A strong coffee brewed by forcing hot water through finely-ground coffee beans.
  - **Latte**: A smooth blend of espresso and steamed milk, topped with a light layer of foam.
  - **Cappuccino**: A rich combination of espresso, steamed milk, and a thick layer of foamed milk.

- **Resource Management**: Automatically tracks available resources (water, milk, coffee) and checks for sufficient ingredients.

- **Payment Processing**: Accepts various coin payments and calculates the required change.

- **Refill Functionality**: Easily refill resources as needed, ensuring that the machine is always ready to serve.

- **Report Generation**: Generate a report showing the current status of resources and the total profit earned.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure that Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/shrutimsontakke/coffee-machine.git
   cd coffee-machine
   ```

2. **Run the Application**:

   ```bash
   python run.py
   ```

## Usage

Once you run the application, you can choose from the following options:

- **Order a Drink**: Type the name of the drink you want (espresso, latte, cappuccino).
- **Refill Resources**: Type `refill` to add more ingredients to the machine.
- **Check Resources**: Type `report` to see the current status of resources and total profit.
- **Turn Off**: Type `off` to exit the program.

## Sample Interaction

```plaintext
What would you like? (espresso/latte/cappuccino/refill/report): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is your latte ☕️. Enjoy!
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements! 

## Acknowledgments

- Inspired by the coffee-making process and the joy of programming!

