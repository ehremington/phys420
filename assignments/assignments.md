<div class="cell markdown">

## Problem Set 11

### Problem 3.31

### Problem 3.32
We have already done this one in class.

----

</div>

<div class="cell markdown">

## Problem Set 10

### Problem 3.24

### Problem 3.25 (but not f)

----

</div>

<div class="cell markdown">

## Problem Set 9

### Problem 3.1

### Problem 3.10

### Problem 3.14

---

</div>

<div class="cell markdown">

## Problem Set 8

### Problem 2.26

### Problem 2.32

----

</div>

<div class="cell markdown">

## Problem Set 7

### Problem 2.16

### Problem 2.18
The "hint" in this problem probably needs another hint. Think about the fact that you can express $N!$ as $N\times (N-1)!$, and that means you can rearrange that formula to write
$$ (N-1)! = \frac{N!}{N} $$ 

Use a similar technique on $(q+N-1!)$ and then simplify.

Also another hint for later on, don't forget that $N = N^1 = N^{2/2}$. 

### Problem 2.22
Your hint for this one is in part (d). The question asks, "Out of all the macrostates, what fraction have reasonably large probabilities?" What he is getting at is you have found in part (c) how tall the multiplicity peak is, and in part (b) you have found the area under the multiplicity curve so using the loose approximation of the area as a thin rectangle the width of that rectangle would correspond to the number of macrostates that have a reasonable change of occuring. The "fraction" that have a reasonable chance of occuring is just this number divided by the total number of macrostates. This will be a very small number. This small number represents the fraction of all the macrostates that are reasonably likely to occur.

### Problem 2.28

### Problem 2.29
I have already done this in jupyter, so just make sure you have added it to your personal version of that file and know how it works. 

There is a question at the end of this problem that says, "Also compute the entropy over long time scales, assuming that all microstates are accessible." What this means is that instead of plugging in the multiplicity of the of the most likely macrostate into the entropy formula, you are pluggin in the total multiplicity of all the macrostates. This is just the sum of the multiplicities of the macrostates. 

Another way you can get this number is to think about the system as a *single* solid (of 500 particles) with a 100 packets of enery to share. What is the multiplicity of this single solid. This number is equal to the sum of the total multiplicities of the two solids in contact. Show yourself that this is true.

In jupyter to get this to work on the pandas dataframe that we made a couple of things may be handy. First, make sure your dataframe expresses all of its values as *float numbers* (which just means scientific notation) rather than *integers* which is so long your computer can not display it. To do this run something like this on your table (mine was called `table2`).

    table2 = table2.astype(float)

Next, you can sum up the `multi_total` column using this function:

    table2['multi_total'].sum()

Hope this helps.

-----

</div>

<div class="cell markdown">

## Problem Set 6

### Problem 2.1

### Problem 2.5 a and b

### Problem 2.9
We have done the first part of this in Google Sheets and in Jupyter. You can do the second part in either. Just copy the results of the table and graph into your homework.

### Problem 2.10
This is also easy to do in Jupyter now that we have the code written.

### Problem 2.12 d
Do this by graph this function $y=ln(1+x)$ in the vicinity near x = 0 and then use the result from part (c) which is that the derivative of natural log is the inverse function:

$$ \frac{d \ln(x)}{dx} = \frac{1}{x} $$

Think about the slope of the function and what the equation of a line that approximates this would be.

### Problem 2.13 b
I already used this trick in the notes, but I want you identify it and to write it down.

-----

</div>

<div class="cell markdown">

## Problem Set 5

### Finish problem 1.34

You have done the work part of (a), so use the equipartition theorem to finish the rest. Don't forget it is a diatomic gas.

### Problem 1.36

It might help to do 1.35 first but I'll tell you the gist and then you can just use the results. We derived an expression in class for initial and final volume and temperature ratios for an adiabatic compression: 

$$ \left(\frac{T_f}{T_i}\right)^{f/2}=\frac{V_i}{V_f}$$

This is also the same information as equation 1.38 and 1.39 from the book. Use your proportionalities from the ideal gas law to get $T\propto PV$, and then plug that in and simplify. You will get equation 1.40 from the book, as long as you let $\gamma = (f+2)/f$. Use this form to help with Problem 1.36.

### Problem 1.38

Great conceptual question. Think about which bubble with expand more, the one that experienced isothermal expansion, or the one that experienced adiabatic expansion. They experience the same change in pressure since they start at the same level in the water and both reach the surface.

------------

</div>

<div class="cell markdown">

## Problem Set 4

### Problem 1.7

### Problem 1.16

### Problem 1.17

Additional Hint: you can use pressure in atm and volume in cm$^3$ if you use the gas constant $ R=83.1$ which has units of $\frac{atm \cdot cm^3}{mol K}$.

----------

</div>

<div class="cell markdown" jp-MarkdownHeadingCollapsed="true" tags="[]">

## Problem Set 3

### Equilibrium Temperature

A 5kg block of aluminum ($c_{Al} = 0.9 kJ/kgK$) at 500C is in thermal contact with a 5kg block of lead ($c_{Pb} = 0.13kJ/kgK$) at 75C. What is their equilibrium temperature?

### Problem 1.41

### Problem 1.47 or 1.48 your choice

---------

</div>

<div class="cell markdown" jp-MarkdownHeadingCollapsed="true" tags="[]">

## Problem Set 2

### Problem 1.28 

Estimate how long it should take to bring a cup of water to boiling temperature in a typical 600-watt microwave oven, assuming that all the energy ends up in the water. (Assume any reasonable initial temperature for the water.) Explain why no heat is involved in this process.

### Problem 1.33 a

We did this in class already, but just make sure you have it written down, so we can come back and finish the rest later.

### Problem 1.34 a 

But ONLY the work done on each stage of the cycle. We'll come back and talk about the heat added and the change in th eenergy content later. Express your answers in terms of $P_1, P_2, V_1, V_2.$ 


-----

</div>

<div class="cell markdown" tags="[]">

## Problem Set 1

### Problem 1.1

### Problem 1.3

### Problem 1.12

### Proportionality

Proportionality is a very convenient way to summarize a relationship, but its the kind of thing that everyone assumes someone else taught you. 

So when we see an equation like the ideal gas law $P V = N k_B T$ this equation contains many relationships that can be stated as *ratios*. As an example, imagine we are conducting an experiment where we vary the temperature of a gas, but we do not change the number of particles or the volume of the container. The question is what happens to the pressure? We can relate the *ratio* of the two temperatures to the *ratio* of the two different pressures. Here is how:

Solve for the Pressure: 

$$ P = \frac{N k_B}{V} T $$

and then see that this general equation must be satisfied in the specific instances of $T_1, T_2, P_1, P_2$:
$$ P_1 = \frac{N k_B}{V} T_1 $$
$$ P_2 = \frac{N k_B}{V} T_2 $$

Dividing the two equations as 2/1, shows that all of the constant things ($N, k_b, V$) cancel out and we are left with a proportion

$$\frac{P_2}{P_1} = \frac{T_2}{T_1}$$

This type of proportionality is called *directly proportional* or *linearly proportional* since if you double the temperature $T_2/T_1 = 2$ then the equation says that the pressure would double as well $P_2/P_1 = 2$.

The fancy/mathy way of writing this is $P \propto T$. When you see that statement, it means you can write down $$\frac{P_2}{P_1} = \frac{T_2}{T_1}$$

Other types of proportionality follow from this logic. So for example

$$ y \propto \frac{1}{x} $$ 

is called *inverse proportionality*. It is also sometimes written as $y \propto x^{-1}$. From these statements, you can write down 

$$ \frac{y_2}{y_1} = \frac{x_1}{x_2} = \left(\frac{x_2}{x_1}\right)^{-1} $$

There are other proportionality statements that are very important in physics like the famous *inverse square law* which comes in the form $y \propto x^{-2}$. These kinds of proportionality statements can also be written as an equation with a *constant of proportionality* which is often the mores familiar form to us. So for example the law of Universal Gravitation can be written like 

$$ F = \frac{G m_1 m_2}{r^2} $$

We could say the the force is directly proportional to each mass, and inversely proportional to the square of the distance between them. The constant of proportionality is *G*. 

Ok, now go back to the ideal gas law and imagine the following scenarios:

1. By what factor does the pressure change if the temperature triples (here we assume that all other things are unchanged)? (that language of "by what factor" is just another way of saying "whats the ratio of pressures")
2. By what factors does the pressure change if the number of particles doubles? What about halving? (remember that this is only true if the temperature is the same as well as the volume - how would you do that?).
3. By what factor does the pressure change if the volume doubles?
4. By what factor does the pressure change if the volume doubles and the temperature triples?
5. By what factors would the temperature change if the volume doubled and the pressure tripled?
6. By what factors would the volume change if the number of particles halved and the pressure doubled and the temperature *decreased* by a factor of 10? How would you do this in the lab?

</div>
