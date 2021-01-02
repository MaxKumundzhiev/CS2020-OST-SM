<h1>Classification Models</h1>
<p>
  This file ,at the time of writing, contains 3 offline pre-trained classification models on the Non-vpn dataset inside a jupyter notebook using sci-kit learn library, namely are:
</p>
<ul>
  <li>Logistic Regression</li>
  <li>Decision Tree</li>
  <li>Random Forest</li>
</ul>
<p>
  We divided the data set into 80% training, and 20% test set ( for final evaluation ). We used a cross-validation approach with grid search (to perform simple hyper-parameter tuning),
  and picked the best model
</p>
<h2>
  The results for Test set evaluation of each class are included in the following table
</h2>
<table>
  <thead>
    <tr>
      <th> model </th>
      <th> Test accuracy </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Logistic Regression</td>
      <td>70.17</td>
    </tr>
    <tr>
      <td>Decision Tree</td>
      <td>72.93</td>
    </tr>
    <tr>
      <td>Random Forest</td>
      <td>75.46</td>
    </tr>
  </tbody>
</table>
<p>
  In addition to classification models, we trained a Vanilla Generative Adversarial Network on the aforementioned data set. We can clearly monitor how the discriminator and generator
  losses are converging indicating that the discriminator cannot distinguish between real and fake outputs.
</p>
<img width="500" height="500" src="Vanilla GAN - Non VPN.png" alt="Flink workflow" title="Flink Workflow" />
<p>The generator model in the most basic test case can be used to generate synthetic data from any class using it in inference mode after passing the preferred class label</p>
