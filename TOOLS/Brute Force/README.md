# BRUTE FORCE ATTACK

A brute force attack is a method used to gain unauthorized access to a system by systematically attempting all possible 
combinations of passwords or keys until the correct one is found. It's one of the simplest forms of attacks, 
relying on the power of computing to exhaustively try every possibility.

## Limitations and Ethical Considerations

- Time-Consuming: Brute force attacks can be very slow, especially if the password is long and complex.
- Detection: Many systems can detect brute force attempts and may lock accounts or take other actions to prevent unauthorized access.
- Legality: Performing brute force attacks on systems without permission is illegal and unethical. 
Only use this knowledge on systems you own or have explicit permission to test.

## Base Script

Just for visualization and understanding of what is our object, this first version of my script is based on
checking every possibility within a range, using all kinds of combinations.

Combinations are defined on the variable `charset`.

A built in python method is used to test all combinations within a range. The method is `itertools.product`.

## Considerations

This is a very very slow attempt to break a password, and statistically, it has almost zero chance to crack a real
case scenario, due to a lot of variables.

To work properly, it should be used together with another tools, like well projected social engineering questions,
almost like creating a funnel strategy to increase chances and probabilities of guessing it correctly.

The next level is to use dictionary attacks, which are generally faster and based on a large amount of data.