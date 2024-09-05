--  https://codeinplace.stanford.edu/public/learn


> [!NOTE]
> Conditions

> That last example used a new condition. Here is a list of all of the conditions that Karel knows of:

> Test	Opposite	What it checks
> front_is_clear() 	front_is_blocked() 	Is there a wall in front of Karel?
> beepers_present() 	no_beepers_present() 	Are there beepers on this corner?
> left_is_clear() 	left_is_blocked() 	Is there a wall to Karel’s left?
> right_is_clear() 	right_is_blocked() 	Is there a wall to Karel’s right?
> beepers_in_bag() 	no_beepers_in_bag() 	Does Karel have any beepers in its bag?
> facing_north() 	not_facing_north() 	Is Karel facing north?
> facing_south() 	not_facing_south() 	Is Karel facing south?
> facing_east() 	not_facing_east() 	Is Karel facing east?
> facing_west() 	not_facing_west() 	Is Karel facing west?


|   |   |
| --- | --- |
|  Base Karel commnds:

move()
turn_left()
put_beeper()
pick_beeper()   |  Karel program structures:

#### Comments can be included in any part
#### of a program. They start with a #
#### and include the rest of the line.

def main() :
   code to execute

declarations of other functions   |


| Karel program structures:

#### Comments can be included in any part
#### of a program. They start with a '#'
#### and include the rest of the line.

def main() :
   code to execute

declarations of other functions   |     |

|  Names of the conditions:
front_is_clear()
beepers_present()
beepers_in_bag()
left_is_clear()
right_is_clear()
facing_north()
facing_south()
facing_east()
facing_west()
front_is_blocked() no_beepers_present()
no_beepers_in_bag()
left_is_blocked()
right_is_blocked()
not_facing_north()
not_facing_south()
not_facing_east()
not_facing_west()   |   Function Declaration:

defname():
code in the body of the function.  |

|     |    Extra Karel Commands:

paint_corner(COLOR_NAME)
corner_color_is(COLOR_NAME)
  |