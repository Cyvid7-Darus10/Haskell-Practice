
-- ---------- MATH ----------
-- Something crazy to start
sumOfVals = sum [1..1000]

addEx = 5 + 4
subEx = 5 - 4
multEx = 5 * 4
divEx = 5 / 4

-- mod is a prefix operator
modEx = mod 5 4

-- With back ticks we can use it as an infix operator
modEx2 = 5 `mod` 4

-- Negative numbers must be surrounded with parentheses
negNumEx = 5 + (-4)

-- If you define an Int you must use fromIntegral to use it with sqrt
-- :t sqrt shows that it returns a floating point number
num9 = 9 ::Int
sqrtOf9 = sqrt (fromIntegral num9)

-- Built in math functions
piVal = pi
ePow9 = exp 9
logOf9 = log 9
squared9 = 9 ** 2
truncateVal = truncate 9.999
roundVal = round 9.999
ceilingVal = ceiling 9.999
floorVal = floor 9.999

-- Also sin, cos, tan, asin, atan, acos, sinh, tanh, cosh, asinh, atanh, acosh

trueAndFalse = True && False
trueOrFalse = True || False
notTrue = not(True)

-- Remember you use :t in the terminal to get the data type (:t value)
-- You can also see how functions use data types with :t

-- :t (+) = Num a => a -> a -> a
-- Type a is in the type class num, we receive 2 of them and return 1

-- :t truncate = (RealFrac a, Integral b) => a -> b

