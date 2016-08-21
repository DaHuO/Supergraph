import Control.Monad
import Data.Function
import Data.List
import Data.Char
import Numeric

import Data.Numbers.Primes --cabal install primes-0.2.1.0

----------------
--] TEMPLATE [--
----------------

printCase :: Int -> String -> IO ()
printCase probi solution = putStrLn $ "Case #" ++ (show probi) ++ ": " ++ solution

solveAll :: Int -> Int -> IO ()
solveAll probc probi
	| probi <= probc = do
		solve probi
		solveAll probc (probi + 1)
	| otherwise = return ()

main = do
	probc <- readLn :: IO Int
	solveAll probc 1

--------------------
--] END TEMPLATE [--
--------------------

getJCoin :: Integer -> Integer -> Integer -> Integer -> [Integer] -> [Integer] -> [Integer]
getJCoin _ _ 0 _ _ jcoins = jcoins
getJCoin minCoin maxCoin coinCount jcoin primesSubset jcoins
	| jcoin > maxCoin = getJCoin minCoin maxCoin coinCount minCoin (take ((length primesSubset) + 1) primes) jcoins
	| otherwise =
		if -1 `elem` (map (\x -> getWitness_Cheap jcoin x primesSubset) [2..10]) || (jcoin `elem` jcoins)
		then getJCoin minCoin maxCoin coinCount (jcoin + 2) primesSubset jcoins
		else getJCoin minCoin maxCoin (coinCount - 1) (jcoin + 2) primesSubset (jcoin:jcoins)

proveJCoin :: Integer -> IO ()
proveJCoin j =
	putStrLn $ (concat . map show . reverse . untens $ j) ++ " " ++ (unwords . map (show . getWitness j) $ [2..10])
 
getWitness_Cheap :: Integer -> Integer -> [Integer] -> Integer
getWitness_Cheap jcoin base primesSubset =
	let 
		jcoin' = jcoinToBase jcoin base
		witness = dropWhile (\x -> jcoin' `mod` x /= 0) $ primesSubset
		witness' =
			if null witness
			then -1
			else head witness
	in
		if witness' == jcoin
		then -1
		else witness'

getWitness :: Integer -> Integer -> Integer
getWitness jcoin base = getWitness_Cheap jcoin base primes 

jcoinToBase :: Integer -> Integer -> Integer
jcoinToBase jcoin base = sum $ zipWith (*) (untens jcoin) (tens base)

tens :: Integer -> [Integer]
tens x = map (x^) [0..]

untens :: Integer -> [Integer]
untens x = reverse . map (toInteger . digitToInt) $ showIntAtBase 2 intToDigit x ""

solve :: Int -> IO ()
solve probi = do
	printCase probi ""
	problem <- getLine
	let (coinLength:coinCount:[]) = map read . words $ problem
	let minCoin = 2^(coinLength-1) + 1
	let maxCoin = 2^(coinLength)-1
	let jcoinv = getJCoin minCoin maxCoin coinCount minCoin [2,3,5,7] []
	mapM_ proveJCoin jcoinv

