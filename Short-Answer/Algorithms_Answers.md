#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
I think the runtime for this problem is: O(n^2)

I think this because:
The actual math problem is: a + n^2, using my logic from below (c), n^2 is the most significant term.

<!-- Each time the problem is ran, the same amount gets added each time. So, when I look at the graph on the iterative sorting page in the TK, n goes up one and over one each time creating a linear "curve". In my example where n = 5, the points are (a, a+n^3) (0, 25), (25, 50), (50, 75), (75, 100), and (100, 125). I get a linear line when I plot them. (I think i changed my mind. My previous answer was O(n) -->

Here is a repl.it I created to work out the problem visually.
I gave n a value of 5 and printed a.
https://repl.it/@maggieprice/GenuineThirdProcessor

b)
I think the runtime for this problem is: O(n^2)

I think this because:
Only 2 lines depend on the input size. The rest are constant. J increases as n increases. As n increases, the loops increase multiple times but n has to incrememnt multiple times for J to increase. So, if n = 4, j returns 2 & 4 and loops through 4 cycles. if n = 5, j returns 2, 4, and 8 and loops through 5 cycles. But J doesn't increase to 2, 4, 8, and 16 until n = 9. Before that, it just add an extra loop. This type of cycle continues as you increase n. The next value of n that increases j is 17 (increases to 32). So it took 4 incrememnts before. This time it took 7. The next time, n has to = 33 for J to increase to 64. So it took 16 increments. So my conclusion is that n has to increase more and more each time for j to increase. Based on the description for the polynomial in the TK ("As the size of the input increases, the runtime or space used will grow at a faster rate"), I chose this classification. Honestly, I chose ^2 because there were 2 n's in the problem and it was my best guess.

Here is a repl.it I created to work out the problem visually.
I changed the value of n several times to get a feel for what it was doing and printed j.
https://repl.it/@maggieprice/AssuredHeartyCoderesource

c)
I think the runtime for this problem is: O(n)

I think this because:
The input is bunnies (n). The first part of the code is constant but the last line basically equalls n-1. In the TK under iterative sorting, it talks about the most significant term. It says that as n grows, the less significant term has less of an effect so we only need to consider what n does.

I did create a repl.it for this one but found it less helpful on this problem.
https://repl.it/@maggieprice/EvenRespectfulWearable

## Exercise II
