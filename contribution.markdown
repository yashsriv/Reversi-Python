# Contribution ~~Rules~~ Guidelines
> "the code is more what you'd call "guidelines" than actual rules"  
> \- Pirates of the Caribbean  

Compiled set of relevant style guides from [Google Python StyleGuide](https://google.github.io/styleguide/pyguide.html)

## Committing Rules

* Commit messages should be meaningful
  and should properly mention changes to the code.


## Python Language Rules

* Python Version;  
  All code should be **python3**

* Global Variables:  
  Avoid global variables in favor of class variables. Some exceptions are: 
  * Constants: Should be named using all caps with underscores between words;  
    For Example : `PI = 3.14159`
  * Storing values for functions which cannot be achieved in any other way


* List Comprehensions:  
  Use List comprehensions for efficient code.  
  ```python
  squares = [x * x for x in range(10)]  #for an array of squares of numbers.
  ```


## Python Style Rules

* Semicolons:  
  Do not terminate lines with semi-colons and do not use
  semi-colons to put two commands on the same line.

* Line length:  
  Maximum line length should be 80 characters unless it is not possible to do so.

* Parentheses:  
  Do not use them in return statements or conditional statements.  
  Should be used only for tuples.  
  ```python
  if a > b:  # This should be used
    return a
  if (a > b):  # This should not be done
    return(a)
  ```

* Indentation:  
  Indent your code blocks with 4 spaces.  
  Do not use tabs.  
  Please ensure that your code uses spaces instead of tabs.  
  (All major text editors support this feature to insert spaces when you press tab)

* Blank Lines:  
  One blank line between method definitions.

* Whitespace:  
  Follow standard typographic rules for the use of spaces around punctuation.  
  For more info : [See This](https://google.github.io/styleguide/pyguide.html?showone=Whitespace#Whitespace)

* Files and sockets:  
  Implicitly close Files and sockets when done with them.

* Comments:  
  Non-Trivial portions of the code should be commented properly.

* Naming:  
  
  Variable Names,class names and function names should be meaningful.

  |       Type       |        Typographic Rule        |            Example           |
  | :--------------: | :----------------------------: | :--------------------------: |
  |      Classes     |        Upper Camel Case        |     `class ThisIsAClass:`    |
  |     Functions    | lowercase,words separated by _ |  `def this_is_a_function():` |
  | Global Constants | Uppercase,words separated by _ | `THIS_IS_A_CONSTANT = 'foo'` |
  |     Variables    | lowercase,words separated by _ | `this_is_a_variable = 'bar'` |

* Main:  
  The main functionality should be in a main() function.

  ```python
  def main():
    ...

  if __name__ == '__main__':
      main()
  ```
