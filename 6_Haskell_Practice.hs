
-- ---------- HIGHER ORDER FUNCTIONS ----------
-- Passing of functions as if they are variables

times4 :: Int -> Int
times4 x = x * 4

-- map applies a function to every item in the list
listTimes4 = map times4 [1,2,3,4,5]

-- Let's make map
multBy4 :: [Int] -> [Int]
multBy4 [] = []

-- Takes the 1st value off the list x, multiplies it by 4 and stores it in the
-- new list
-- xs is then passed back into multBy4 until there is nothing left of the list -- to process (Recursion)
multBy4 (x:xs) = times4 x : multBy4 xs

-- Check if strings are equal with recursion
areStringsEq :: [Char] -> [Char] -> Bool
areStringsEq [] [] = True
areStringsEq (x:xs) (y:ys) = x == y && areStringsEq xs ys
areStringsEq _ _ = False

-- PASSING A FUNCTION INTO A FUNCTION
-- (Int -> Int) says we expect a function that receives an Int and returns an
-- Int
doMult :: (Int -> Int) -> Int

-- We receive the function and pass 3 into it
doMult func = func 3

-- We pass in the function that multiplies by 4
num3Times4 = doMult times4

-- RETURNING A FUNCTION FROM A FUNCTION
getAddFunc :: Int -> (Int -> Int)

-- We can pass in the values to the function
getAddFunc x y = x + y

-- We could also get a function that adds 3 for example
adds3 = getAddFunc 3

fourPlus3 = adds3 4

-- We could use this function with map as well
threePlusList = map adds3 [1,2,3,4,5]

-- ---------- LAMBDA ----------
-- How we create functions without a name
-- \ represents lambda then you have the arguments -> and result

dbl1To10 = map (\x -> x * 2) [1..10]

