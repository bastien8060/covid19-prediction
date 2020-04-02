# Covid19 prediction

Predicts Covid19 case number for next day for any countries

<h1> Installation </h1>
<h2> Linux </h2>
run:
<pre>$ git clone https://github.com/bastien8060/covid19-prediction </pre>
<pre>$ cd covid19-prediction/ </pre>
<br>
<h3>Dependencies</h3>
<ul>
  <li>statsmodels <pre>pip install statsmodels</pre></li>
    <li>pandas <pre>pip install statsmodels</pre></li>
    <li>numpy <pre>pip install numpy</pre></li>
 </ul>
<h1>Usage</h1>
<h2> Install country </h2>
<pre>$ ./init.py (country to download) </pre>
<br>
<h2>Predict</h2>
<pre>$ ./predict.py (country name)</pre>
<br>
<h2>Update </h2>
<pre>$ cd utils/</pre>
<pre>$ ./update.py (country name)</pre>
<br>
<h2> Remove country </h2>
<pre>$ cd utils/</pre>
<pre>$ ./reset.sh (country name)</pre>
