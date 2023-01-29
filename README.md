**kidBank**

Since no one in our family ever carries cash anymore, my kids each have an "account" that I keep track of. When they do their chores, I add the money they earned to their accounts. When they want to buy something, I subtract the cost from their accounts.

I had been keeping track of this in my notes app, which is less than ideal. For one, the kids have no way to know how much is in their accounts without pestering me to look it up. Additionally, there's no recordkeeping to speak of, so I can't tell if their balance is huge because they earned a lot, or if my fat fingers accidently added a zero.

This is a very simple Django app to fix these issues. It uses Django's built-in authorization to create individual accounts for the kids and the adults. Kids can log in and view their balance at any time. Adults can log in and make deposits or withdrawals for any of the kid accounts. Every transaction is tracked so there's no funny business.

To manage users, in the Django admin I created two groups: Kids and Adults.  Kids have view-only privledges, while Adults can add/delete transactions. 