<div class="cell markdown" jp-MarkdownHeadingCollapsed="true" tags="[]">

## Problem Set 2

### Problem 1.28 

Estimate how long it should take to bring a cup of water to boiling temperature in a typical 600-watt microwave oven, assuming that all the energy ends up in the water. (Assume any reasonable initial temperature for the water.) Explain why no heat is involved in this process.

### Problem 1.33 a

We did this in class already, but just make sure you have it written down, so we can come back and finish the rest later.

### Problem 1.34 a 

But ONLY the work done on each stage of the cycle. We'll come back and talk about the heat added and the change in th eenergy content later. Express your answers in terms of $P_1, P_2, V_1, V_2.$ 

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

<div class="cell code">

``` python
```

</div>
