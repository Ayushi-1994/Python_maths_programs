# Reverse Number

## Logic
Build reversed number digit by digit.

Example:
123 → 321

## Steps
1. digit = n % 10
2. reversed = reversed * 10 + digit
3. n //= 10
4. Repeat

## Time Complexity
O(d)
