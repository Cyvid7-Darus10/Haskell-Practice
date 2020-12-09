{-
  ---------Lab Exercise 2-------
  Name: Cyrus David G. Pastelero
  Subject: Programming Paradigms
  Section: A
  Date: Oct 1, 2020
  ------------------------------
-}

---------------Easy Functions-------------------
-- Consumes an integer and produces the cube of that integer
cube :: Int -> Int
cube n = n * n * n

-- Consumes an integer and produces the 2 times that integer
double :: Int -> Int
double n = n * 2


----------------Recursive Functions-------------
-- Consumes two integers n and m and produces xmodm
modulus :: Int -> Int -> Int
modulus n m = n `mod` m

-- Consumes an integer and produces the factorial of the integer
factorial :: Int -> Int
factorial n = if (n == 0) then 1 else (n * (factorial(n - 1)))

-- Consumes a natural number and produces the summation of numbers from 1 to n. ∑ni=1i.
summation :: Int -> Int
summation n = if (n <= 1) then n else (n + (summation (n-1)))


-------High Order Functions-------------------------
-- Consumes two functions f:Z→Z, and g:Z→Z and produces the function f∘g.
compose :: (Int -> Int) -> (Int -> Int) -> (Int -> Int)
compose func1 func2 = (func1 . func2)

-- Consumes an integer x and produces a function that consumes an integer y and produces x−y
subtractMaker :: Int -> (Int -> Int)
subtractMaker x = (\y -> x - y)

-- Consumes a function f:Z→Z and and two integers n and x.
-- applyNTimes produces an integer which is the result of the function applied to x, n-times.
-- If n is less than or equal to 0 it must produce zero applications of f therefore it produces x.
applyNTimes :: (Int -> Int) -> Int -> Int -> Int
applyNTimes f n x = if (n <= 0) then x else ((applyNTimes f (n - 1) (f x)))
