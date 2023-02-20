Description of the Project:
This project is a command-line interface (CLI) tool that provides a simplified version of Airbnb's booking management system. The CLI tool allows users to create, read, update, and delete booking-related data, including properties, bookings, guests, and hosts. Users can interact with the tool using a set of pre-defined commands, which are documented in the command interpreter section.

Description of the Command Interpreter:
The command interpreter is the core component of the CLI tool. It receives user input in the form of commands and arguments and performs actions based on those inputs. The interpreter is designed to be user-friendly and intuitive, with easy-to-understand commands and error messages. It supports a variety of commands related to properties, bookings, guests, and hosts. These commands are documented in the "How to Use It" section below.

How to Start It:
To start the CLI tool, follow these steps:

Clone the project repository to your local machine.
Open a terminal window and navigate to the project directory.

Run the following command to install the project dependencies:
npm install

Run the following command to start the CLI tool:
npm start

How to Use It:
Once the CLI tool is started, you can use the following commands to interact with it:

create-property: Creates a new property with the specified details.
read-property: Displays the details of a specific property.
update-property: Updates the details of a specific property.
delete-property: Deletes a specific property.
create-booking: Creates a new booking for a specific property and guest.
read-booking: Displays the details of a specific booking.
update-booking: Updates the details of a specific booking.
delete-booking: Deletes a specific booking.
create-guest: Creates a new guest with the specified details.
read-guest: Displays the details of a specific guest.
update-guest: Updates the details of a specific guest.
delete-guest: Deletes a specific guest.
create-host: Creates a new host with the specified details.
read-host: Displays the details of a specific host.
update-host: Updates the details of a specific host.
delete-host: Deletes a specific host.
help: Displays a list of available commands and their descriptions.
quit or exit: Exits the CLI tool.
Examples:
Here are some examples of how to use the CLI tool:

To create a new property, run the following command:
create-property --name "Cozy Cabin" --type "Cabin" --city "Asheville" --state "NC" --country "USA" --max-guests 4 --price-per-night 100

To read the details of a specific property, run the following command:
read-property --id 123

To update the details of a specific property, run the following command:
update-property --id 123 --name "Updated Name"

To delete a specific property, run the following command:
delete-property --id 123

To display a list of available commands, run the following command:
help
