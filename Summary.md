# Pharmacy Inventory System

## 1. Project Overview

The **Pharmacy Inventory System** is a console-based application
developed using **Python 3**. It helps manage the stock of medicines in
a pharmacy.

The program stores medicine details in a CSV file named `medicines.csv`.
Each medicine has an ID, name, quantity and price. Medicine IDs are
generated automatically, starting from `M1`.

The system provides the following features:

-   Add a new medicine to the inventory.
-   View all available medicines.
-   Sell medicines, calculate the bill and update the stock.
-   Delete a medicine using its ID.
-   Display a low-stock report for medicines with fewer than 10 units.
-   Calculate the total inventory value.

The project uses Python concepts such as **lists, dictionaries,
functions, loops, conditional statements, exception handling and CSV
file handling**.

## 2. Problems Faced and Their Solutions

While developing the project, I faced some challenges. I solved them
using Python programming concepts.

  ---------------------------------------------------------------------------
  No.                     Problem faced           How it was solved
  ----------------------- ----------------------- ---------------------------
  1                       Creating and managing   I used Python's `csv`
                          the CSV file was        module to read data from
                          difficult at first.     and write data to
                                                  `medicines.csv`.

  2                       Generating a unique ID  I created a function that
                          for every new medicine  checks the existing
                          was challenging.        medicine IDs and generates
                                                  the next ID, such as `M1`,
                                                  `M2` and `M3`.

  3                       Updating the stock      I reduced the medicine
                          after a medicine was    quantity only after
                          sold needed careful     checking that enough stock
                          handling.               was available.

  4                       The program needed to   I added a condition to
                          prevent sales when the  compare the requested
                          requested quantity was  quantity with the available
                          greater than the        quantity and display an
                          available stock.        insufficient-stock message
                                                  when necessary.

  5                       Calculating the bill    I used the formula
                          for each sale was       `Bill = Quantity × Price`
                          required.               and displayed the result up
                                                  to two decimal places.

  6                       Finding medicines with  I used a loop and a
                          low stock was difficult condition to display
                          when there were many    medicines whose quantity
                          medicines.              was below 10.

  7                       The data needed to      I called the save function
                          remain saved after      after every inventory
                          closing the program.    change so that the updated
                                                  data was written to the CSV
                                                  file.

  8                       Invalid and negative    I used `try-except` blocks
                          inputs could cause      and validation conditions
                          errors or incorrect     to reject invalid numbers
                          data.                   and negative quantity or
                                                  price values.

  9                       Deleting the correct    I searched for the medicine
                          medicine required       using its unique ID and
                          identifying it          removed the matching record
                          accurately.             from the list.

  10                      Calculating the total   I multiplied each
                          inventory value         medicine's quantity by its
                          required adding the     price and added the
                          value of every          results.
                          medicine.               
  ---------------------------------------------------------------------------

## 3. Testing

The program was tested using different inputs to check whether all
features worked correctly.

  -------------------------------------------------------------------------------------
  Test case               Operation               Expected result
  ----------------------- ----------------------- -------------------------------------
  1                       Add Paracetamol with    Medicine is added with ID `M1`.
                          quantity 50 and price   
                          2.50.                   

  2                       Sell 10 units of `M1`   Sale is completed, bill is `25.00`,
                          when 50 units are       and stock becomes 40.
                          available.              

  3                       Try to sell 8 units     The program displays
                          when only 5 units are   `Insufficient stock. Available: 5`.
                          available.              

  4                       Display the low-stock   Cetirizine is displayed as low stock.
                          report when Cetirizine  
                          has quantity 8.         

  5                       Delete medicine `M3`    The program displays
                          and calculate the       `Medicine M3 deleted.` and the
                          inventory value using   inventory value is `165.00` when the
                          the assigned data.      remaining records are M1 (50 × 2.50)
                                                  and M2 (8 × 5.00).
  -------------------------------------------------------------------------------------

## 4. Test Case Screenshots

Add screenshots of the actual program output for the assigned test cases
in this section.

If screenshots cannot be embedded in this file, save them in a separate
folder named `testcases` or `Screenshots` in the project repository.

Suggested folder structure:

``` text
Pharmacy-Inventory-System/
│
├── one.py
├── medicines.csv
├── Summary.md
└── testcases/
    ├── test-case-1.png
    ├── test-case-2.png
    ├── test-case-3.png
    ├── test-case-4.png
    └── test-case-5.png
```

Replace the example screenshot names above with your actual screenshot
files. Do not use sample or imagined screenshots; capture the output
after running the program.

## 5. Conclusion

The Pharmacy Inventory System provides a simple way to manage medicine
stock through a Python console application. While developing this
project, I learned how to use lists and dictionaries to organize data,
functions to divide a program into smaller tasks, and CSV file handling
to store information permanently.

I also learned how to validate user input, update stock after sales,
calculate bills and inventory value, and identify medicines that need
restocking. This project helped me understand how Python programming
concepts can be applied to a practical inventory-management problem.
