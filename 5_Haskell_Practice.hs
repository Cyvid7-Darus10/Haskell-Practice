
-- ---------- FUNCTIONS ----------
-- ghc --make haskelltut compiles your program and executes the main function

-- Functions must start with lowercase letters

-- We can define functions and values in the GHCi with let
-- let num7 = 7
-- let getTriple x = x * 3

-- getTriple num7 = 21

-- main is a function that can be called in the terminal with main
main = do
	-- Prints the string with a new line
	putStrLn "What's your name: "

	-- Gets user input and stores it in name
	-- <- Pulls the name entered from an IO action
	name <- getLine

	putStrLn ("Hello " ++ name)

-- Create function addMe
-- x is a parameter and the operation follows the equals sign
-- The data type passed in will work if it makes sense
-- Every function must return something
-- A function name can't begin with a capital letter
-- A function that doesn't receive parameters is called a definition or name

-- You can define a type declaration for functions
-- funcName :: param1 -> param2 -> returnType
addMe :: Int -> Int -> Int

-- funcName param1 param2 = operations (Returned Value)
-- Execute with : addMe 4 5
addMe x y = x + y

-- Without type declaration you can add floats as well
sumMe x y = x + y

-- You can also add tuples : addTuples (1,2) (3,4) = (4,6)
addTuples :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuples (x, y) (x2, y2) = (x + x2, y + y2)

-- You can perform different actions based on values
whatAge :: Int -> String
whatAge 16 = "You can drive"
whatAge 18 = "You can vote"
whatAge 21 = "You're an adult"

-- The default
whatAge x = "Nothing Important"

-- Define that we expect an Int in and out
factorial :: Int -> Int

-- If 0 return a 1 (Recursive Function)
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- 3 * factorial (2) : 6
-- 2 * factorial (1) : 2
-- 1 * factorial (0) : 1

-- You could also use product to calculate factorial
productFactorial n = product [1..n]

-- We can use guards that provide different actions based on conditions
isOdd :: Int -> Bool
isOdd n
	-- if the modulus using 2 equals 0 return False
	| n `mod` 2 == 0 = False

	-- Else return True
	| otherwise = True

-- This could be shortened to
isEven :: Int -> Bool
isEven n = n `mod` 2 == 0

-- Use guards to define the school to output
whatGrade :: Int -> String
whatGrade age
	| (age >= 5) && (age <= 6) = "Kindergarten"
	| (age > 6) && (age <= 10) = "Elementary School"
	| (age > 10) && (age <= 14) = "Middle School"
	| (age > 14) && (age <= 18) = "High School"
	| otherwise = "Go to college"

-- The where clause keeps us from having to repeat a calculation
batAvgRating :: Double -> Double -> String
batAvgRating hits atBats
	| avg <= 0.200 = "Terrible Batting Average"
	| avg <= 0.250 = "Average Player"
	| avg <= 0.280 = "Your doing pretty good"
	| otherwise = "You're a Superstar"
	where avg = hits / atBats

-- You can access list items by separating letters with : or get everything but
-- the first item with xs
getListItems :: [Int] -> String
getListItems [] = "Your list is empty"
getListItems (x:[]) = "Your list contains " ++ show x
getListItems (x:y:[]) = "Your list contains " ++ show x ++ " and " ++ show y
getListItems (x:xs) = "The first item is " ++ show x ++ " and the rest are "
	++ show xs

-- We can also get values with an As pattern
getFirstItem :: String -> String
getFirstItem [] = "Empty String"
getFirstItem all@(x:xs) = "The first letter in " ++ all ++ " is "
	++ [x]
