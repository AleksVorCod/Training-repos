/*You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.
Implement a function likes :: [String] -> String, which must take in input array, 
containing the names of people who like an item.
For 4 or more names, the number in and 2 others simply increases.*/
function likes (names) {
  return {
    0 : 'no one likes this',
    1 : `${names[0]} likes this`,
    2 : `${names[0]} and ${names[1]} like this`,
    3 : `${names[0]}, ${names[1]} and ${names[2]} like this`,
    4 : `${names[0]}, ${names[1]} and ${names.length - 2} others like this`,
  }[Math.min(4, names.length)]
}