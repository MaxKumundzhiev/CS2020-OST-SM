# Models Description
MK-KIT module is represented as 2 submodules based on datasets types.    
1. Malware Detection (cicids, netml datasets)
2. Traffic Classification (non-vpn dataset)

<h1>Traffic Classification</h1>
Within Traffic Classification problem it was utilized 3 dedicated models. 
<ul>
  <li>Logistic Regression</li>
  <li>Decision Tree</li>
  <li>Random Forest</li>
</ul>
<p>
  We divided the data set into 80% training, and 20% test set ( for final evaluation ). We used a cross-validation approach with grid search (to perform simple hyper-parameter tuning),
  and picked the best model.
</p>
<h2>
  The results for Test set evaluation of each class are included in the following table
</h2>
<table>
  <thead>
    <tr>
      <th> Model name </th>
      <th> Test accuracy </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Logistic Regression</td>
      <td>70.17%</td>
    </tr>
    <tr>
      <td>Decision Tree</td>
      <td>72.93%</td>
    </tr>
    <tr>
      <td>Random Forest</td>
      <td>75.46%</td>
    </tr>
  </tbody>
</table>
<p>
  In addition to classification models, we trained a Vanilla Generative Adversarial Network on the aforementioned data set. We can clearly monitor how the discriminator and generator
  losses are converging indicating that the discriminator cannot distinguish between real and fake outputs.
</p>
<img width="700" height="500" src="./diagrams/GAN.png" alt="Flink workflow" title="Flink Workflow" />
<p>The generator model in the most basic test case can be used to generate synthetic data from any class using it in inference mode after passing the preferred class label</p>
