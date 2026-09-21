# GCD & LCM

## GCD Logic (Euclid)
gcd(a, b) = gcd(b, a % b)

## LCM Logic
lcm(a, b) = (a × b) / gcd(a, b)

## Time Complexity
O(log n)





## What is GCD?
GCD (Greatest Common Divisor) is the largest number that divides both numbers completely.

Example:
GCD of 12 and 18 = 6  
Because the common divisors are:  
12 → 1, 2, 3, 4, 6, 12  
18 → 1, 2, 3, 6, 9, 18  
Largest common divisor = 6

---

## Manual Method (School Method)
### Step 1: Write all factors of both numbers
12 → 1, 2, 3, 4, 6, 12  
18 → 1, 2, 3, 6, 9, 18  

### Step 2: Pick the largest common factor  
Common: 1, 2, 3, 6  
GCD = **6**

This is the method we used in school.

---

## Mathematical Method Used in Python (Euclid’s Algorithm)
Instead of listing all factors, Euclid discovered a faster way:

### Rule:
gcd(a, b) = gcd(b, a % b)

This works because:
- When you divide a by b, the remainder contains the “extra part” that still needs to be checked.
- The GCD of two numbers is the same as the GCD of the smaller number and the remainder.

### Example:
Find GCD(12, 18):

1. gcd(12, 18)  
2. gcd(18, 12)  
3. gcd(12, 6)  
4. gcd(6, 0) → STOP  
GCD = **6**

When remainder becomes 0, the other number is the GCD.

### Why this works?
Because:
- Divisors of (a, b) are the same as divisors of (b, a % b)
- So we keep reducing the problem until remainder becomes 0

This is the fastest known method.

---






## What is LCM?
LCM (Least Common Multiple) is the smallest number that both numbers divide into.

Example:
LCM of 12 and 18 = 36  
Because multiples are:  
12 → 12, 24, 36, 48, ...  
18 → 18, 36, 54, ...  
Smallest common multiple = 36

---

## Mathematical Formula Used in Python
LCM is related to GCD:

### Formula:
lcm(a, b) = (a × b) / gcd(a, b)

### Why this formula works?
Because:
- a × b contains all prime factors of both numbers
- gcd(a, b) removes the repeated common factors
- What remains is the least common multiple

Example:
LCM(12, 18) = (12 × 18) / 6 = 216 / 6 = **36**

---

## Time Complexity
Euclid’s GCD: O(log n)  
LCM uses GCD → O(log n)

---

## Summary
- School method: list factors → pick largest  
- Python method: Euclid’s algorithm → fast, mathematical  
- LCM uses GCD formula → avoids listing multiples

This README explains both the **manual school method** and the **mathematical algorithm** used in programming.
