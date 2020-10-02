-- Haskell is a functional programming language
-- Everything is immutable so once a value is set it is set forever
-- Functions can be passed as a parameter to other functions
-- Recursion is used often
-- Haskell has no for, while, or technically variables, but it does have
-- constants
-- Haskell is lazy in that it doesn't execute more then is needed and instead
-- just checks for errors

-- Type ghci to open it up in your terminal
-- Load script with :l haskelltut
-- :quit exits the GHCi

-- Import a module
import Data.List
import System.IO


{-
Beginning of multiline comment
-}

-- ---------- DATA TYPES ----------
-- Haskell uses type inference meaning it decides on the data type based on the
-- value stored in it
-- Haskell is statically typed and can't switch type after compiling
-- Values can't be changed (Immutable)
-- You can use :t in the terminal to get the data type (:t value)

-- Int : Whole number -2^63 - 2^63
-- :: Int defines that maxInt is an Int
maxInt = maxBound :: Int
minInt = minBound :: Int

-- Integer : Unbounded whole number

-- Float : Single precision floating point number
-- Double : Double precision floating point number (11 pts precision)
bigFloat = 3.99999999999 + 0.00000000005

-- Bool : True or False
-- Char : Single unicode character denoted with single quotes
-- Tuple : Can store a list made up of many data types

-- You declare the permanent value of a variable like this
always5 :: Int
always5 = 5

