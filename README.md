# Customer Invitation

Challenge proposed in a job interview.

## The Challenge

We have some customer records in a text file [customers.txt](customers.txt) - one customer per line, JSON lines formatted. We want to invite any customer within 100km of our Dublin office for some food and drinks on us. Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending).

You can use the first formula from [this Wikipedia article](https://en.wikipedia.org/wiki/Great-circle_distance) to calculate distance. Don't forget, you'll need to convert degrees to radians.
The GPS coordinates for our Dublin office are 53.339428, -6.257664.
You can find the Customer list [here](customers.txt).

We're looking for you to produce working code, with enough room to demonstrate how to structure components in a small program.

- Poor answers will be in the form of one big function. It’s impossible to test anything smaller than the entire operation of the program, including reading from the input file. Errors are caught and ignored.
- Good answers are well composed. Calculating distances and reading from a file are separate concerns. Classes or functions have clearly defined responsibilities. Test cases cover likely problems with input data.
- It’s an excellent answer if we've learned something from reading the code.

We recommend you use whatever language you feel strongest in. It doesn't have to be one we use!

**Please submit code as if you intended to ship it to production.** The details matter. Tests are expected, as is well written, simple idiomatic code. Please include the output of your program with your code

### The Solution

I've opted for using Python because of more friendly lists and file operations

App uses [Haversine Formule](https://en.wikipedia.org/wiki/Haversine_formula) as suggested to calculate the smallest distance between 2 points on Earth surface.

![Great Circle Distance](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Illustration_of_great-circle_distance.svg/447px-Illustration_of_great-circle_distance.svg.png)

So we have the following files:
- **[customers_invitation.py](customers_invitation)** - Main app that filters customers list and display the results on screen and save it to [invitation.txt](invitation.txt) file.
- **[utils.py](utils.py)** - Helper functions with Haversine formule and file operations
- **[tests.py](tests.py)** - Unit tests with some case validations
- **[customers.txt](customers.txt)** - Customer data file in JSON format
- **[invitation.txt](invitation.txt)** - Filtered invitation list according to maximum distance provided

## To run:

You need to have [Python](https://www.python.org/) installed. Open a terminal and type these commands:
- `python customers_invitation.py` - Run main app to generate the invitation list
- `python tests.py` - Run some unit tests

All code follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.

## Copyright

This app was developed by Márcio Souza de Oliveira.
