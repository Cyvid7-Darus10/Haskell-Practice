
-- ---------- TYPE CLASSES ----------
-- Num, Eq, Ord and Show are type classes
-- Type classes correspond to sets of types which have certain operations
-- defined for them.
-- Polymorphic functions, which work with multiple parameter types, define
-- the types it works with through the use of type classes
-- For example (+) works with parameters of the type Num
-- :t (+) = Num a => a -> a -> a
-- This says that for any type a, as long as a is an instance of Num, + can take
-- 2 values and return an a of type Num

-- Create an Employee and add the ability to check if they are equal
data Employee = Employee { name :: String,
						   position :: String,
						   idNum :: Int
						   } deriving (Eq, Show)

samSmith = Employee {name = "Sam Smith", position = "Manager", idNum = 1000}
pamMarx = Employee {name = "Pam Marx", position = "Sales", idNum = 1001}

isSamPam = samSmith == pamMarx

-- We can print out data because of show
samSmithData = show samSmith

-- Make a type instance of the typeclass Eq and Show
data ShirtSize = S | M | L

instance Eq ShirtSize where
	S == S = True
	M == M = True
	L == L = True
	_ == _ = False

instance Show ShirtSize where
	show S = "Small"
	show M = "Medium"
	show L = "Large"

-- Check if S is in the list
smallAvail = S `elem` [S, M, L]

-- Get string value for ShirtSize
theSize = show S

-- Define a custom typeclass that checks for equality
-- a represents any type that implements the function areEqual
class MyEq a where
	areEqual :: a -> a -> Bool

-- Allow Bools to check for equality using areEqual
instance MyEq ShirtSize where
	areEqual S S = True
	areEqual M M = True
	areEqual L L = True
	areEqual _ _ = False

newSize = areEqual M M

-- ---------- I/O ----------

sayHello = do
	-- Prints the string with a new line
	putStrLn "What's your name: "

	-- Gets user input and stores it in name
	name <- getLine

	-- $ is used instead of the parentheses
	putStrLn $ "Hello " ++ name

-- File IO
-- Write to a file
writeToFile = do

	-- Open the file using WriteMode
	theFile <- openFile "test.txt" WriteMode

	-- Put the text in the file
	hPutStrLn theFile ("Random line of text")

	-- Close the file
	hClose theFile

readFromFile = do

	-- Open the file using ReadMode
	theFile2 <- openFile "test.txt" ReadMode

	-- Get the contents of the file
	contents <- hGetContents theFile2
	putStr contents

	-- Close the file
	hClose theFile2

-- ---------- EXAMPLE : FIBONACCI SEQUENCE ----------

-- Calculate the Fibonacci Sequence
-- 1, 1, 2, 3, 5, 8, ...

-- 1 : 1 : says to add 2 1s to the beginning of a list
-- | for every (a, b) add them
-- <- stores a 2 value tuple in a and b
-- tail : get all list items minus the first
-- zip creates pairs using the contents from 2 lists being the lists fib and the
-- list (tail fib)

fib = 1 : 1 : [a + b | (a, b) <- zip fib (tail fib) ]

-- First time through fib = 1 and (tail fib) = 1
-- The list is now [1, 1, 2] because a: 1 + b: 1 = 2

-- The second time through fib = 1 and (tail fib) = 2
-- The list is now [1, 1, 2, 3] because a: 1 + b: 2 = 3

fib300 = fib !! 300 -- Gets the value stored in index 300 of the list

-- take 20 fib returns the first 20 Fibonacci numbers
