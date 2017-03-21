"""
-----------------------------------------------------------------------
Question 1.

Given two int values, return True if one is negative and one is
positive. Except if the parameter "negative" is True, then return True
only if both are negative.
-----------------------------------------------------------------------

"""

def int(1, 2):
if(not 1 or 2):
return True
else:
return False


def pos_neg(a, b, negative):
    pass

def pos_neg(1,-2, negative))
    pass
def pos_neg(1,2, positive))
    pass

# Expected outputs:

print(pos_neg(1, -1, False))
# True
print(pos_neg(-1, 1, False))
# True
print(pos_neg(-4, -5, True))
# True
print(pos_neg(-2, -5, False))
# False
print(pos_neg(1, 2, False))
# False


"""
-----------------------------------------------------------------------
Question 2.

A year with 366 days is called a leap year. Leap years are necessary to
keep the calendar synchronized with the sun because the earth revolves
around the sun once every 365.25 days. Actually, that figure is not
entirely precise, and for all dates after 1582 the Gregorian correction
applies. Usually years that are divisible by 4 are leap years, for
example 1996. However, years that are divisible by 100 (for example,
1900) are not leap years, but years that are divisible by 400 are leap
years (for example, 2000).
-----------------------------------------------------------------------

"""



 #include <stdio.h>
#include <stdbool.h>

bool is_leap_year(int year)
{
    return !(year % 4) && year % 100 || !(year % 400);
}

int main()
{
    int test_case[] = {1900, 1994, 1996, 1997, 2000}, key, end;
    for (key = 0, end = sizeof(test_case)/sizeof(test_case[0]); key < end; ++key) {
        int year = test_case[key];
        printf('d is a leap year.\n", year, is_leap_year(year) ? "" : "not "); }


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(leap_year(1900))
# print(leap_year(2016))
# print(leap_year(2017))
# print(leap_year(2000))




"""
-----------------------------------------------------------------------
Question 3:

Write a function with loops that computes the sum of all squares between
1 and n (inclusive).
-----------------------------------------------------------------------



def sum_squares(n):
    pass

def sum_squares(1, n)
    pass

def sum_squares(1)
    def sum_squares(2)
        def sum_squares(100)

# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(sum_squares(1))
# print(sum_squares(100))
