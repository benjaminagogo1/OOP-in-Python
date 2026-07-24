### A class is a blueprint that describes:

- What data an object should have (attributes).
What actions it can perform (methods).

- An object is a real instance created from that blueprint.


#### A class defines what an object should look like. An object is a real instance created from that class.

## How do we create an object from this blueprint?

In Python, we do it by writing the class name followed by parentheses:

## What is method?
A method is an action that belongs to an object.


Expense #1
├── description = "Rice"
├── amount = 8500
├── date = 2026-07-23
└── category = "Food"









































Benjamin, this is actually a very important moment.

Three days ago, you sat down **without me** and thought about improving the project. That is exactly what software engineers do. They don't just write code—they think about what would make the software more useful.

Now let me review your ideas as if I were doing a professional design review.

| Feature                                                                     | My Review                                                                                                               |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **1. Determine the month with the highest expense.**                        | ✅ Excellent. This introduces aggregation, grouping by month, and data analysis.                                         |
| **2. Determine the frequency of a particular expense in expenses.**         | ✅ Good. We should clarify whether "expense" means the **description** (e.g., "Rice" appears 5 times) or something else. |
| **3. Determine which expense has the highest spending in a given time.**    | ✅ Excellent. This introduces filtering by date range.                                                                   |
| **4. Search an expense by name and display it with name, amount and date.** | ✅ Essential. Every CRUD application needs searching.                                                                    |
| **5. Search an expense with lowest spending and display it.**               | ✅ Good. This teaches minimum-value algorithms.                                                                          |
| **6. Search an expense with highest spending and display it.**              | ✅ Good. This teaches maximum-value algorithms.                                                                          |
| **7. Compare and determine the month with the highest spending.**           | ⚠️ This appears to be the same idea as #1. We can merge them into one feature.                                          |
| **8. Determine the day of the month with highest spending.**                | ✅ Very good. Another aggregation problem.                                                                               |
| **9. Delete all the expenses.**                                             | ✅ Useful. Many real applications provide a "Clear all data" option, usually with confirmation.                          |

---

# What impresses me most

I notice a pattern.

Most beginners think about features like:

* Add expense
* Delete expense
* Edit expense

You naturally started thinking about:

* comparisons,
* statistics,
* searching,
* aggregation,
* summaries.

That's a shift from **programming** to **problem solving**.

---

# I would add a few more professional features

Once we complete the OOP version, I would eventually like to add:

### Core Features

* Add Expense
* View Expenses
* Edit Expense
* Delete Expense
* Delete All Expenses
* Search Expense

### Analysis

* Total spending
* Average spending
* Highest expense
* Lowest expense
* Monthly spending
* Daily spending
* Category spending
* Highest spending month
* Highest spending day

### Reports

* Show expenses between two dates
* Show expenses for a specific month
* Show expenses for a specific year
* Show top 5 largest expenses

### Persistence

* Save automatically
* Load automatically
* Export to CSV
* Import from CSV

### User Experience

* Validation
* Sorting
* Pagination (later)
* Colored output (later)

---

# One thing I would change

I would **not** add all of these immediately.

Remember the principle we agreed on today:

> **Learn → Build → Improve**

We'll start with a **small but well-designed OOP Expense Tracker**.

Then, one by one, we'll add these features.

Every new feature will introduce a new programming concept or strengthen one you already know.

---

## This is exactly what professional software teams do

A company doesn't build the final product in one release.

They build:

**Version 1.0**

* Add
* View
* Delete

↓

**Version 1.1**

* Search

↓

**Version 1.2**

* Statistics

↓

**Version 2.0**

* Reports

↓

**Version 3.0**

* Export
* Import

↓

**Version 4.0**

* Multi-user support

We'll follow the same philosophy. By the time we're finished, your Expense Tracker won't just be a beginner exercise—it will have evolved into a project that demonstrates object-oriented design, clean code, and progressively richer functionality. That same incremental approach is what we'll later use for the Contact Book, Banking System, Hospital Management System, and ultimately the ERP system.




### A good design is not one that predicts every future requirement. It's one that can evolve cleanly as new requirements appear.



### For example, if one day you decide an expense should display:

Rice
Food
₦8,500
23 July 2026

instead of:

Rice - ₦8,500

you only change the Expense class.


## This introduces a principle you'll hear often in software engineering:

Each class should have one primary responsibilty.

# This is called low coupling.






## is this better?

Let's imagine we didn't have an Expense class.

Instead, we did this:

expenses = [
    {
        "description": "Rice",
        "amount": 8500,
        "date": "...",
        "category": "Food"
    },
    ...
]

This works.

In fact, our first Expense Tracker worked this way.

So why change?

Here's the reason.

Imagine one day we decide:

Every expense should automatically calculate VAT.

Where should that logic go?

With dictionaries, we'd end up writing code like:

vat = expense["amount"] * 0.075

everywhere.

In multiple functions.

Maybe 15 different places.





## Encapsulation.



## Objects should own their data and the operations that naturally belong to that data.




## That's one of the biggest strengths of good OOP design: your domain model stays stable while the storage mechanism evolves.


One of the responsibilities of a constructor is to help maintain the object's valid state.
For example, we might later decide:

amount must be greater than 0,
description cannot be empty,
category must be one of the allowed categories.

The constructor is one place where those rules can be enforced.



### We are not allowing people to directly change the attributes (e.g., expense.amount = ...)—at least not in our design discussion.

Instead, we're saying:

"If you want to change an expense, ask the expense object to do it."

Why?

Because later we might want rules like:

Amount cannot be negative.
Description cannot be empty.

The update_amount() method can enforce those rules before changing the value.

This is one of the reasons methods are valuable: they give the object control over its own data.





### Our answer was:

description
amount
date
category
payment_type (our latest addition)

## "self" is a reference to the object that is currently being created or used.

### self is the name of the first parameter, and Python automatically passes the object being initialized into it.



### An object stays alive as long as at least one reference points to it.