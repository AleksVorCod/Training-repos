<?php /*Your task is to make a function that can take any non-negative integer as an argument 
and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.*/?>
function descendingOrder(int $number): int {
  if($number < 0) {
    throw new InvalidArgumentException("The param \$number must be a positive integer");
  }
  $numarray = str_split($number);
  rsort($numarray);
  return (int) join($numarray);
}